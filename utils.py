import time

from config import *
from gtaasmysql import MySQL


def js_convert_to_comm(str):
    for key, value in JS_TO_CONVERT.items():
        if key in str:
            str = str.replace(key, value)
    return str


def monitor_qqshare(q):
    obj_mysql = MySQL(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_PORT, MYSQL_DATABASE)
    while True:
        ids = obj_mysql.query('select id from {}'.format(MYSQL_TABLE_QQSHARE))
        global ICA_QQSHARE_LIST
        templist = []
        for i in range(0, len(ids)):
            templist.append(ids[i][0])
        rlist = list(set(templist).difference(set(ICA_QQSHARE_LIST)))
        ICA_QQSHARE_LIST.clear()
        ICA_QQSHARE_LIST = templist[:]
        global ICA_QQSHARE_FLAG
        if ICA_QQSHARE_FLAG:
            ICA_QQSHARE_FLAG = False
            continue
        if rlist:
            for id in rlist:
                result = obj_mysql.query(
                    "select owner_nick,owner_uin,upload_nick,upload_uin,gc,create_time,modify_time,filename, url from %s where id='%s'" % (
                        MYSQL_TABLE_QQSHARE, id))
                content = '【qq群共享文件】【苏宁】' + result[0][0] + '--' + result[0][1] + '--' + result[0][2] + '--' + result[0][
                    3] + '--' + result[0][4] + '--' + result[0][5] + '--' + result[0][6] + '--' + result[0][7] + '--' + \
                          result[0][8]
                q.put(content, block=False)
        time.sleep(300)


def monitor_tuan_xianbao(q):
    obj_mysql = MySQL(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_PORT, MYSQL_DATABASE)
    while True:
        ids = obj_mysql.query('select id from {}'.format(MYSQL_TABLE_TUAN_XIANBAO))
        global TUAN_LIST
        templist = []
        for i in range(0, len(ids)):
            templist.append(ids[i][0])
        rlist = list(set(templist).difference(set(TUAN_LIST)))
        TUAN_LIST.clear()
        TUAN_LIST = templist[:]
        global TUAN_FLAG
        if TUAN_FLAG:
            TUAN_FLAG = False
            continue
        if rlist:
            for id in rlist:
                result = obj_mysql.query(
                    "select keyword, title, url from %s where id='%s'" % (MYSQL_TABLE_TUAN_XIANBAO, id))
                content = '【' + result[0][0] + '】' + result[0][1] + '\n' + result[0][2]
                q.put(content, block=False)
        time.sleep(5)


def monitor_just_xianbao(q):
    obj_mysql = MySQL(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_PORT, MYSQL_DATABASE)
    while True:
        ids = obj_mysql.query('select id from {}'.format(MYSQL_TABLE_JUST_XIANBAO))
        global JUST_LIST
        templist = []
        for i in range(0, len(ids)):
            templist.append(ids[i][0])
        rlist = list(set(templist).difference(set(JUST_LIST)))
        JUST_LIST.clear()
        JUST_LIST = templist[:]
        global JUST_FLAG
        if JUST_FLAG:
            JUST_FLAG = False
            continue
        if rlist:
            for id in rlist:
                result = obj_mysql.query(
                    "select keyword, title, url from %s where id='%s'" % (MYSQL_TABLE_JUST_XIANBAO, id))
                content = '【' + result[0][0] + '】' + result[0][1] + '\n' + result[0][2]
                q.put(content, block=False)
        time.sleep(5)


def monitor_zy_baicai(q):
    obj_mysql = MySQL(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_PORT, MYSQL_DATABASE)
    while True:
        ids = obj_mysql.query('select id from {}'.format(MYSQL_TABLE_ZY_BAICAI))
        global ZHUANYES_LIST
        templist = []
        for i in range(0, len(ids)):
            templist.append(ids[i][0])
        rlist = list(set(templist).difference(set(ZHUANYES_LIST)))
        ZHUANYES_LIST.clear()
        ZHUANYES_LIST = templist[:]
        global ZHUANYES_FLAG
        if ZHUANYES_FLAG:
            ZHUANYES_FLAG = False
            continue
        if rlist:
            for id in rlist:
                result = obj_mysql.query(
                    "select keyword, title, post_on, content from %s where id='%s'" % (MYSQL_TABLE_ZY_BAICAI, id))
                content = '【' + result[0][0] + '】' + '【' + result[0][1] + '】' + '\n' + '【优惠发布时间: ' + result[0][
                    2] + '】' + '\n' + result[0][3]
                q.put(content, block=False)
        time.sleep(5)


def monitor_zy_tenyuanstore(q):
    obj_mysql = MySQL(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_PORT, MYSQL_DATABASE)
    while True:
        ids = obj_mysql.query('select id from {}'.format(MYSQL_TABLE_ZY_TENYUANSTORE))
        global ZHUANYES_TENYUANSTORE_LIST
        templist = []
        for i in range(0, len(ids)):
            templist.append(ids[i][0])
        rlist = list(set(templist).difference(set(ZHUANYES_TENYUANSTORE_LIST)))
        ZHUANYES_TENYUANSTORE_LIST.clear()
        ZHUANYES_TENYUANSTORE_LIST = templist[:]
        global ZHUANYES_TENYUANSTORE_FLAG
        if ZHUANYES_TENYUANSTORE_FLAG:
            ZHUANYES_TENYUANSTORE_FLAG = False
            continue
        if rlist:
            for id in rlist:
                result = obj_mysql.query(
                    "select price, title, url, img from %s where id='%s'" % (MYSQL_TABLE_ZY_TENYUANSTORE, id))
                content = '【' + result[0][0] + '】' + '【' + result[0][1] + '】' + '\n' + result[0][2] + "\n" + result[0][
                    3]
                q.put(content, block=False)
        time.sleep(5)


def monitor_tao_clipcoupouns(q):
    obj_mysql = MySQL(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_PORT, MYSQL_DATABASE)
    while True:
        ids = obj_mysql.query('select id from {}'.format(MYSQL_TABLE_TAO_CLIPCOUPONS))
        global TAO_CLIPCOUPOUNS_LIST
        templist = []
        for i in range(0, len(ids)):
            templist.append(ids[i][0])
        rlist = list(set(templist).difference(set(TAO_CLIPCOUPOUNS_LIST)))
        TAO_CLIPCOUPOUNS_LIST.clear()
        TAO_CLIPCOUPOUNS_LIST = templist[:]
        global TAO_CLIPCOUPOUNS_FLAG
        if TAO_CLIPCOUPOUNS_FLAG:
            TAO_CLIPCOUPOUNS_FLAG = False
            continue
        if rlist:
            for id in rlist:
                result = obj_mysql.query(
                    "select price, title, url, img from %s where id='%s'" % (MYSQL_TABLE_TAO_CLIPCOUPONS, id))
                content = '【' + result[0][0] + '】' + '【' + result[0][1] + '】' + '\n' + result[0][2] + "\n" + result[0][
                    3]
                q.put(content, block=False)
        time.sleep(5)


def monitor_tao_rtinfo(q):
    obj_mysql = MySQL(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_PORT, MYSQL_DATABASE)
    while True:
        ids = obj_mysql.query('select id from {}'.format(MYSQL_TABLE_TAO_RTINFO))
        global TAO_RTINFO_LIST
        templist = []
        for i in range(0, len(ids)):
            templist.append(ids[i][0])
        rlist = list(set(templist).difference(set(TAO_RTINFO_LIST)))
        TAO_RTINFO_LIST.clear()
        TAO_RTINFO_LIST = templist[:]
        global TAO_RTINFO_FLAG
        if TAO_RTINFO_FLAG:
            TAO_RTINFO_FLAG = False
            continue
        if rlist:
            for id in rlist:
                result = obj_mysql.query(
                    "select title, url from %s where id='%s'" % (MYSQL_TABLE_TAO_RTINFO, id))
                content = '【' + result[0][0] + '】' + '\n' + result[0][1]
                q.put(content, block=False)
        time.sleep(5)


def monitor_tao_activityinfo(q):
    obj_mysql = MySQL(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_PORT, MYSQL_DATABASE)
    while True:
        ids = obj_mysql.query('select id from {}'.format(MYSQL_TABLE_TAO_ACTIVITYINFO))
        global TAO_ACTIVITYINFO_LIST
        templist = []
        for i in range(0, len(ids)):
            templist.append(ids[i][0])
        rlist = list(set(templist).difference(set(TAO_ACTIVITYINFO_LIST)))
        TAO_ACTIVITYINFO_LIST.clear()
        TAO_ACTIVITYINFO_LIST = templist[:]
        global TAO_ACTIVITYINFO_FLAG
        if TAO_ACTIVITYINFO_FLAG:
            TAO_ACTIVITYINFO_FLAG = False
            continue
        if rlist:
            for id in rlist:
                result = obj_mysql.query(
                    "select title, dt, url from %s where id='%s'" % (MYSQL_TABLE_TAO_ACTIVITYINFO, id))
                content = '【' + result[0][0] + '】' + '【发布时间：' + result[0][1] + '】' + '\n' + result[0][2]
                q.put(content, block=False)
        time.sleep(5)
