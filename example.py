# -*- coding: utf-8 -*-
import logging
import os
import random
import time
import platform

from QQLightBot import ApiProtocol, MsgDict
from gtaasmysql import MySQL
from loggtaas import Log

logger = logging.getLogger('QQLightBot')
from datetime import datetime
import json
from config import *
from multiprocessing import Queue
import threading
from utils import *

g_obj_mysql = MySQL(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_PORT, MYSQL_DATABASE)
g_obj_mysql.create(SQL_CREATE_TABLE)

g_queue_tuan_xianbao = Queue()
g_queue_just_xianbao = Queue()
g_queue_zy_baicai = Queue()
g_queue_zy_tenyuanstore = Queue()
g_queue_tao_clipcoupouns = Queue()
g_queue_tao_rtinfo = Queue()
g_queue_tao_activityinfo = Queue()
g_queue_qqshare = Queue()


class ExampleProtocol(ApiProtocol):
    groupmap = {}
    msgmap = {
        1: '好友消息',
        2: '群消息',
        3: '临时消息',
        4: '讨论组消息',
        5: '讨论组临时消息',
        6: 'QQ临时消息'
    }

    @classmethod
    async def onConnect(cls):
        """连接成功
        """
        logger.info('connect succeed')
        result = await cls.getGroupList()
        for item in result['result']['join']:
            key = str(item['gc'])
            cls.groupmap[key] = []
            cls.groupmap[key].append(js_convert_to_comm(item['gn']))
            cls.groupmap[key].append(str(item['owner']))

        p_tuan = threading.Thread(target=monitor_tuan_xianbao, args=(g_queue_tuan_xianbao,))
        p_tuan.start()
        logger.info('Start thred monitor_tuan_xianbao')

        p_just = threading.Thread(target=monitor_just_xianbao, args=(g_queue_just_xianbao,))
        p_just.start()
        logger.info('Start thread monitor_just_xianbao')

        p_qqshare = threading.Thread(target=monitor_qqshare, args=(g_queue_qqshare,))
        p_qqshare.start()
        logger.info('Start thread monitor_qqshare')

        # p_zhuanyes = threading.Thread(target=monitor_zy_baicai, args=(g_queue_zy_baicai,))
        # p_zhuanyes.start()
        #
        # p_zhuanyes_tenyuanstore = threading.Thread(target=monitor_zy_tenyuanstore,
        #                                            args=(g_queue_zy_tenyuanstore,))
        # p_zhuanyes_tenyuanstore.start()
        #
        # p_tao_clipcoupouns = threading.Thread(target=monitor_tao_clipcoupouns, args=(g_queue_tao_clipcoupouns,))
        # p_tao_clipcoupouns.start()
        #
        p_tao_rtinfo = threading.Thread(target=monitor_tao_rtinfo, args=(g_queue_tao_rtinfo,))
        p_tao_rtinfo.start()
        logger.info('Start thread monitor_tao_rtinfo')

        p_tao_activityinfo = threading.Thread(target=monitor_tao_activityinfo, args=(g_queue_tao_activityinfo,))
        p_tao_activityinfo.start()
        logger.info('Start thread monitor_tao_activityinfo')

        while True:
            sms = ''
            if not g_queue_tuan_xianbao.empty():
                time.sleep(random.random())
                sms = g_queue_tuan_xianbao.get_nowait()
                logger.info(sms)
                await cls.sendMessage(2, SEND_MSG_930342284, '', sms)
                time.sleep(random.random())
                await cls.sendMessage(2, SEND_MSG_299638181, '', sms)
                time.sleep(random.random())
                await cls.sendMessage(2, SEND_MSG_860243037, '', sms)

            if not g_queue_just_xianbao.empty():
                time.sleep(random.random())
                sms = g_queue_just_xianbao.get_nowait()
                logger.info(sms)
                await cls.sendMessage(2, SEND_MSG_930342284, '', sms)
                time.sleep(random.random())
                await cls.sendMessage(2, SEND_MSG_299638181, '', sms)
                time.sleep(random.random())
                await cls.sendMessage(2, SEND_MSG_860243037, '', sms)

            if not g_queue_qqshare.empty():
                time.sleep(random.random())
                sms = g_queue_qqshare.get_nowait()
                logger.info(sms)
                await cls.sendMessage(2, SEND_MSG_930342284, '', sms)

            if not g_queue_tao_rtinfo.empty():
                time.sleep(random.random())
                sms = g_queue_tao_rtinfo.get_nowait()
                logger.info(sms)
                await cls.sendMessage(2, SEND_MSG_930342284, '', sms)
                time.sleep(random.random())
                await cls.sendMessage(2, SEND_MSG_299638181, '', sms)
                time.sleep(random.random())
                await cls.sendMessage(2, SEND_MSG_860243037, '', sms)

            if not g_queue_tao_activityinfo.empty():
                time.sleep(random.random())
                sms = g_queue_tao_activityinfo.get_nowait()
                logger.info(sms)
                await cls.sendMessage(2, SEND_MSG_930342284, '', sms)
                time.sleep(random.random())
                await cls.sendMessage(2, SEND_MSG_299638181, '', sms)
                time.sleep(random.random())
                await cls.sendMessage(2, SEND_MSG_860243037, '', sms)
            #
            # if not g_queue_tao_clipcoupouns.empty():
            #     sms = g_queue_tao_clipcoupouns.get_nowait()
            #     await cls.sendMessage(2, SEND_MSG_930342284, '', sms)
            #     await cls.sendMessage(2, SEND_MSG_860243037, '', sms)
            #     await cls.sendMessage(2, SEND_MSG_299638181, '', sms)
            #
            # if not g_queue_zy_baicai.empty():
            #     sms = g_queue_zy_baicai.get_nowait()
            #     await cls.sendMessage(2, SEND_MSG_860243037, '', sms)
            #     await cls.sendMessage(2, SEND_MSG_299638181, '', sms)
            #
            # if not g_queue_zy_tenyuanstore.empty():
            #     sms = g_queue_zy_tenyuanstore.get_nowait()
            #     await cls.sendMessage(2, SEND_MSG_860243037, '', sms)
            #     await cls.sendMessage(2, SEND_MSG_299638181, '', sms)

            time.sleep(5)

    @classmethod
    async def getGroupMemberList(cls, group):
        """接口.获取群成员列表
        :param cls:
        :param group:       群号或讨论组号
        """
        await cls._ws.send_json(cls._makeData(
            'getGroupMemberList', group=group))
        result = await cls._ws.receive()
        return MsgDict(json.loads(result.data))['result']['members']

    @classmethod
    async def message(cls, type=0, qq='', group='', msgid='', content=''):  # @ReservedAssignment
        """事件.收到消息
        :param cls:
        :param type:        1=好友消息、2=群消息、3=群临时消息、4=讨论组消息、5=讨论组临时消息、6=QQ临时消息
        :param qq:          消息来源QQ号，"10000"都是来自系统的消息（比如某人被禁言或某人撤回消息等）
        :param group:       类型为1或6的时候，此参数为空字符串，其余情况下为群号或讨论组号
        :param msgid:       消息id，撤回消息getNickname的时候会用到，群消息会存在，其余情况下为空
        :param content:     消息内容
        """
        result = await cls.getQQInfo(qq)
        try:
            dictData = result['result']['result']['buddy']['info_list'][0]
            data = {}
            data['id'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
            data['source'] = 'QQ'
            data['msg_id'] = msgid
            data['type'] = cls.msgmap[type]
            data['qq'] = qq
            data['gc'] = group
            if group:
                data['gn'] = js_convert_to_comm(cls.groupmap[group][0])
                data['owner'] = cls.groupmap[group][1]
            else:
                data['gn'] = ''
                data['owner'] = ''
            data['nick'] = dictData.get('nick', '')
            data['l_nick'] = dictData.get('lnick', '')
            data['phone'] = dictData.get('phone', '')
            data['city'] = dictData.get('city', '')
            data['occupation'] = dictData.get('occupation', '')
            data['avatar'] = dictData.get('url', '')
            data['email'] = dictData.get('email', '')
            data['mobile'] = dictData.get('mobile', '')

            beg_pos = content.find('QQ:pic=')
            if beg_pos != -1:
                end_pos = content.find(']')
                guid = content[beg_pos + len('QQ:pic='):end_pos]
                image = cls.getImageUrl(guid)
            else:
                image = ''
            data['image'] = image
            data['content'] = content
            logger.info(str(data))
            g_obj_mysql.insert(data, MYSQL_TABLE)
        except Exception as e:
            print(e.args)

    @classmethod
    async def friendRequest(cls, qq='', message=''):
        """事件.收到好友请求
        :param cls:
        :param qq:          QQ
        :param message:     验证消息
        """
        logger.info(
            str(dict(type=type, qq=qq, message=message)))

    @classmethod
    async def becomeFriends(cls, qq=''):
        """事件.成为好友
        :param cls:
        :param qq:          QQ
        """
        logger.info(
            str(dict(type=type, qq=qq)))

    @classmethod
    async def groupMemberIncrease(cls, type='', qq='',  # @ReservedAssignment
                                  group='', operator=''):
        """事件.群成员增加
        :param cls:
        :param type:        1=主动加群、2=被管理员邀请
        :param qq:          QQ
        :param group:       QQ群
        :param operator:    操作者QQ
        """
        logger.info(
            str(dict(type=type, qq=qq, group=group, operator=operator)))
        # 先判断是否是黑名单用户,感觉进群禁言比直接拒绝更好玩。
        black_list = ['1371087907', '1093780350', '884355421', '1151039635', '394354735', '3457219093',
                      '2375514923']  # 黑名单列表
        if group == '681882220' or group == '699188599' or group == '778577978':
            if str(qq) in black_list:
                await cls.sendMessage(2, group, '',
                                      "恭喜新进群的黑名单用户[QQ:face=144]，你将享受秒执行的无限期一个月禁言套餐哦，开心吧[QQ:face=14]" + "[QQ:at={0}]".format(
                                          qq))
                await cls.silence(qq, group, duration=2592000)
            else:
                await cls.sendMessage(2, group, '',
                                      "进群请改备注，如：20-软工专-张三[QQ:face=144]记得看群文件和群公告，可以解决大多数疑惑[QQ:face=183]不要发广告[QQ:face=181]" + "[QQ:at={0}]".format(
                                          qq))
        if group == '88145363':
            await cls.sendMessage(2, group, '',
                                  "进群请改备注，如：20-计算机-张三[QQ:face=144]记得看群文件，有今年的录取情况，不要发广告[QQ:face=181][QQ:emoji=14912151][QQ:emoji=15710351]一战成研\n" + "[QQ:at={0}]".format(
                                      qq))

    @classmethod
    async def groupMemberDecrease(cls, type='', qq='',  # @ReservedAssignment
                                  group='', operator=''):
        """事件.群成员减少
        :param cls:
        :param type:        1=主动退群、2=被管理员踢出
        :param qq:          QQ
        :param group:       QQ群
        :param operator:    操作者QQ，仅在被管理员踢出时存在
        """
        logger.info(
            str(dict(type=type, qq=qq, group=group, operator=operator)))
        if group == '681882220' or group == '699188599' or group == '778577978':
            fight_words = ['He laughs best who laughs last.', 'Talk is cheap,make the move.',
                           'Push yourself until the end.',
                           'Sticking to the end is the best.', 'Everything happens for a resaon.',
                           'Have faith in yourself.', 'I have got your back.', 'All things come to those who wait.',
                           'The shortest way to do many things is to only one thing at a time.',
                           'Nothing seek, nothing find.',
                           'If you are doing your best,you will not have to worry about failure.',
                           'Energy and persistence conquer all things.',
                           'Keep trying no matter how hard it seems. it will get easier.',
                           'Suffering is the most powerful teacher of life.',
                           'Constant dropping wears the stone.', 'Adversity is the midwife of genius.',
                           'If you are doing your best,you will not have to worry about failure.',
                           'Pain past is pleasure.',
                           'Our greatest glory consists not in never falling but in rising every time we fall.',
                           'When we start with a positive attitude and view themselves as successful when we start a success.',
                           "Don't aim for success if you want it; just do what you love and believe in, and it will come naturally."]
            random_num = random.randint(0, len(fight_words) - 1)
            await cls.sendMessage(2, group, '',
                                  "groupMembers--;\nsuccessRate++;\n[QQ:face=144]" + fight_words[
                                      random_num] + "[QQ:face=120]")

    @classmethod
    async def adminChange(cls, type=1, qq='', group=''):  # @ReservedAssignment
        """事件.群管理员变动
        :param cls:
        :param type:        1=成为管理 2=被解除管理
        :param qq:          QQ
        :param group:       QQ群
        """
        logger.info(
            str(dict(type=type, qq=qq, group=group)))

    @classmethod
    async def groupRequest(cls, type=1, qq='', group='',  # @ReservedAssignment
                           seq='', operator='', message=''):
        """事件.加群请求
        :param cls:
        :param type:        1=主动加群、2=被邀请进群、3=机器人被邀请进群
        :param qq:          QQ
        :param group:       QQ群
        :param seq:         序列号，处理加群请求时需要用到
        :param operator:    邀请者QQ，主动加群时不存在
        :param message:     加群附加消息，只有主动加群时存在
        """
        logger.info(
            str(dict(type=type, qq=qq, group=group,
                     seq=seq, operator=operator, message=message)))

    @classmethod
    async def receiveMoney(cls, type=1, qq='', group='',  # @ReservedAssignment
                           amount='', id='', message=''):  # @ReservedAssignment
        """事件.收款
        :param cls:
        :param type:        1=好友转账、2=群临时会话转账、3=讨论组临时会话转账
        :param qq:          转账者QQ
        :param group:       type为1时此参数为空，type为2、3时分别为群号或讨论组号
        :param amount:      转账金额
        :param id:          转账订单号
        :param message:     转账备注消息
        """
        logger.info(
            str(dict(type=type, qq=qq, group=group,
                     amount=amount, id=id, message=message)))

    @classmethod
    async def updateCookies(cls, *args, **kwargs):
        """事件.Cookies更新
        :param cls:
        """
        logger.info('args: {}, kwargs: {}'.format(str(args), str(kwargs)))
