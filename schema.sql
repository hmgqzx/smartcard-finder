drop table if exists USER;
drop table if exists LOST;
drop table if exists FOUND;


SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET TIME_ZONE = "+00:00";


CREATE TABLE `USERS` (
	`userid` int(10) PRIMARY KEY NOT NULL AUTO_INCREMENT,
	`wc_openid` varchar(50) NOT NULL COMMENT '用户的微信加密id',
	`wc_username` varchar(50) NOT NULL COMMENT '用户的微信用户名',
	`phone` varchar(11) NOT NULL COMMENT '用户手机号码',
	`email` varchar(50) NOT NULL COMMENT '用户邮箱',
	`roll_number` varchar(10) NOT NULL COMMENT '用户学号',
	`card_number` varchar(6) NOT NULL COMMENT '用户卡号'
)DEFAULT CHARSET=utf8;



CREATE TABLE `LOST` (
	`lid` int(10) PRIMARY KEY NOT NULL AUTO_INCREMENT,
	`owner_name` VARCHAR(50) NOT NULL COMMENT '失主的姓名',
	`lost_card_number` VARCHAR(6) NOT NULL COMMENT '丢失的卡号'
)DEFAULT CHARSET=utf8;



CREATE TABLE `FOUND` (
	`fid` int(10) PRIMARY KEY NOT NULL AUTO_INCREMENT,
	`picker_name` VARCHAR(50) NOT NULL COMMENT '拾主的姓名',
	`picked_card_number` VARCHAR(6) NOT NULL COMMENT '捡到的卡号',
	`picker_phone` VARCHAR(11) DEFAULT NULL COMMENT '可选:',
	`picker_email` VARCHAR(50) DEFAULT NULL COMMENT '可选:',
	`deposit_location` VARCHAR(255) DEFAULT NULL COMMENT '可选:'
)DEFAULT CHARSET=utf8;

