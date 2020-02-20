# 监测的网站
MYSQL_TABLE_TUAN_XIANBAO = 'tuan_xianbao'
MYSQL_TABLE_JUST_XIANBAO = 'just_xianbao'
MYSQL_TABLE_ZY_BAICAI = 'zy_baicai'
MYSQL_TABLE_ZY_TENYUANSTORE = 'zy_tenyuanstore'
MYSQL_TABLE_TAO_CLIPCOUPONS = 'tao_clipcoupons'
MYSQL_TABLE_TAO_RTINFO = 'tao_rtinfo'
MYSQL_TABLE_TAO_ACTIVITYINFO = 'tao_activityinfo'
MYSQL_TABLE_QQSHARE = 'qqshare'

# 接收消息的群
SEND_MSG_930342284 = '930342284'  # 工作线报群
SEND_MSG_860243037 = '860243037'  # JD毛宁当当每日白菜
SEND_MSG_299638181 = '299638181'  # 全网实时线报

# mysql configuration
MYSQL_HOST = '*'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '*'
MYSQL_PORT = 3306
MYSQL_DATABASE = 'ica'
MYSQL_TABLE = 'qqmsg'

SQL_CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS `qqmsg` (
  `id` varchar(50) NOT NULL,
  `source` varchar(50) NOT NULL,
  `msg_id` varchar(50) DEFAULT '',
  `type` varchar(25) NOT NULL,
  `qq` varchar(25) NOT NULL,
  `gc` varchar(25) DEFAULT '',
  `gn` varchar(255) DEFAULT '',
  `owner` varchar(25) DEFAULT '',
  `nick` varchar(255) DEFAULT '',
  `l_nick` text,
  `phone` varchar(25) DEFAULT '',
  `city` varchar(25) DEFAULT '',
  `occupation` varchar(25) DEFAULT '',
  `avatar` varchar(255) DEFAULT '',
  `email` varchar(50) DEFAULT '',
  `mobile` varchar(25) DEFAULT '',
  `image` varchar(255) DEFAULT '',
  `content` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB CHARSET=utf8mb4
"""

JS_TO_CONVERT = {'&nbsp;': ' ', '&lt;': '<', '&gt;': '>', '&amp;': '&', '&quot;': '"', '&copy;': '©',
                 '&reg;': '®', '&times;': '×', '&divide;': '÷'}

TUAN_LIST = []
JUST_LIST = []
ZHUANYES_LIST = []
ZHUANYES_TENYUANSTORE_LIST = []
TAO_CLIPCOUPOUNS_LIST = []
TAO_RTINFO_LIST = []
TAO_ACTIVITYINFO_LIST = []
ICA_QQSHARE_LIST = []

TUAN_FLAG = True
JUST_FLAG = True
ZHUANYES_FLAG = True
ZHUANYES_TENYUANSTORE_FLAG = True
TAO_CLIPCOUPOUNS_FLAG = True
TAO_RTINFO_FLAG = True
TAO_ACTIVITYINFO_FLAG = True
ICA_QQSHARE_FLAG = True
