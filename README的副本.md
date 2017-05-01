# smartcard-finder

### 疑问

~~jsapi_ticket 是什么，怎么可以在 redis 里找到？~~

~~获取 jsapi 前端签名数据，是什么，是微信的 js 接口吗？~~

[微信JSSDK说明文档 - 微信公众平台开发者文档](http://mp.weixin.qq.com/wiki/7/aaa137b55fb2e0456bf8dd9148dd613f.html)

[wechatpy.client.api.jsapi — wechatpy 1.4.1 文档](http://docs.wechatpy.org/zh_CN/master/_modules/wechatpy/client/api/jsapi.html) #里面有相关参数解释



wechat_custom 是什么模块啊？是不是自己自定义写的啊？

# 笔记

### redis

set 方法

​    redis.set("wechat:access_token", access_token['access_token'], 7000)

7000 是什么？限定时间？应该是有效期，微信的限制是 7200



## wechat-sdk

### 被动回复消息 - 文本消息

将文字信息组装为符合微信服务器要求的响应数据

**调用方法：**`.response_text(content, escape=False)`

**参数说明：**

- `content`: 回复文字
- `escape`: 是否转义该文本内容 (默认不转义)

**调用前检查：**必须已经成功调用过 [`.parse_data()`](https://wechat-sdk.doraemonext.com/official/message/#xml) 方法。

**返回值：**组装好的 XML 字符串，可直接回复微信服务器。

**说明：**该方法会根据 WechatConf 实例化时的 `encrypt_mode` 参数自动组装普通消息或加密消息，无需干预。

