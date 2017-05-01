#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from main import app
# from .models import set_user_info, get_user_student_info, get_user_library_info
from .utils import AESCipher, init_wechat_sdk
from .plugins.state import set_user_state, get_user_state, \
    set_user_last_interact_time, get_user_last_interact_time
# from .plugins import simsimi, sign, express, music, score, library, \
#     school_news, weather, wechat_custom
from .plugins.state import wechat_custom

def wechat_response(data):
    """微信消息处理回复"""
    global message, openid, wechat

    wechat = init_wechat_sdk()
    wechat.parse_data(data)
    message = wechat.get_message()
    # openid = message.source
    # # 用户信息写入数据库
    # set_user_info(openid)

    try:
        get_resp_func = msg_type_resp[message.type]
        response = get_resp_func()
    except KeyError:
        # 默认回复微信消息
        response = 'success'

    # 保存最后一次交互的时间
    set_user_last_interact_time(openid, message.time)
    return response

# 储存微信消息类型所对应函数（方法）的字典
msg_type_resp = {}


def set_msg_type(msg_type):
    """
    储存微信消息类型所对应函数（方法）的装饰器
    """
    def decorator(func):
        msg_type_resp[msg_type] = func
        return func
    return decorator


@set_msg_type('text')
def text_resp():
    """文本类型回复"""
    # 默认回复微信消息
    response = 'success'
    # 替换全角空格为半角空格
    message.content = message.content.replace(u'　', ' ')
    # 清除行首空格
    message.content = message.content.lstrip()
    # 指令列表
    commands = {
        u'取消': cancel_command,
        u'^\?|^？': all_command,
        # u'^雷达|^雷達': weather_radar,
        # u'^電話|^电话': phone_number,
        # u'^公交|^公车|^公車': bus_routes,
        # u'^放假|^校历|^校曆|^校歷': academic_calendar,
        # u'合作': contact_us,
        # u'明信片': postcard,
        # u'^游戏|^遊戲': html5_games,
        # u'^成绩|^成績|^补考|^補考': exam_grade,
        # u'^新闻|^新聞': get_school_news,
        # u'^天气|^天氣': get_weather_news,
        # u'陪聊': enter_chat_state,
        # u'^四级|^六级|^四六级|^四級|^六級|^四六級': cet_score,
        # u'^图书馆|^找书|^圖書館|^找書': search_books,
        # u'^借书|^借書': borrowing_record,
        # u'^续借|^續借': renew_books,
        # u'^签到|^起床|^簽到': daily_sign,
        # u'^音乐|^音樂': play_music,
        # u'^论坛|^論壇': bbs_url,
        # u'^快递|^快遞': enter_express_state,
        # u'^绑定|^綁定': auth_url,
        # u'更新菜单': update_menu_setting
    }
    # 状态列表
    # state_commands = {
    #     'chat': chat_robot,
    #     'express': express_shipment_tracking
    # }
    # 匹配指令
    command_match = False
    for key_word in commands:
        if re.match(key_word, message.content):
            # 指令匹配后，设置默认状态
            set_user_state(openid, 'default')
            response = commands[key_word]()
            command_match = True
            break
    if not command_match:
        # 匹配状态
        state = get_user_state(openid)
        # 关键词、状态都不匹配，缺省回复
        if state == 'default' or not state:
            response = command_not_found()
        # else:
            # response = state_commands[state]()
    return response


# @set_msg_type('click')
# def click_resp():
#     """菜单点击类型回复"""
#     commands = {
#         'phone_number': phone_number,
#         'express': enter_express_state,
#         'score': exam_grade,
#         'borrowing_record': borrowing_record,
#         'renew_books': renew_books,
#         'sign': daily_sign,
#         'chat_robot': enter_chat_state,
#         'music': play_music,
#         'weather': get_weather_news
#     }
#     # 匹配指令后，重置状态
#     set_user_state(openid, 'default')
#     response = commands[message.key]()
#     return response


@set_msg_type('subscribe')
def subscribe_resp():
    """订阅类型回复"""
    set_user_state(openid, 'default')
    response = subscribe()
    return response


def command_not_found():
    """非关键词回复"""
    # 客服接口回复信息
    content = app.config['COMMAND_NOT_FOUND_TEXT'] + app.config['HELP_TEXT']
    wechat_custom.send_text(openid, content)
    # 转发消息到微信多客服系统
    return wechat.group_transfer_message()


def all_command():
    """回复全部指令列表"""
    content = app.config['COMMAND_TEXT']
    return wechat.response_text(content)


def subscribe():
    """回复订阅事件"""
    content = app.config['WELCOME_TEXT'] + app.config['COMMAND_TEXT']
    return wechat.response_text(content)

    return wechat.response_text(content)
