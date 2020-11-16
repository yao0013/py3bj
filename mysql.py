import random
#from random import choice
import string
import pymysql
from faker import Faker
f = Faker('zh_CN')
#a = random.randint(100,700)
#b = ''.join(random.sample(string.ascii_letters + string.digits, 5))
# 打开数据库连接
db = pymysql.connect("127.0.0.1", "root", "root", "电网", charset='utf8' )
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
for i in range(1,10):
	a = random.randint(100,700)
	b = ''.join(random.sample(string.ascii_letters + string.digits, 5))
	sql = """
	INSERT INTO `电网`.`t_assets_vm_copy1` (
	`name`,
	`code`,
	`server_id`,
	`cpu_occupying`,
	`memory_occupying`,
	`harddisk_occupying`,
	`network_occupying`,
	`route`,
	`director`,
	`tel`,
	`movetime`,
	`lock`,
	`links`,
	`host`,
	`status`,
	`auto_disk_config`,
	`availability_zone`,
	`config_drive`,
	`changes-since`,
	`flavor`,
	`image`,
	`ip`,
	`ip6`,
	`kernel_id`,
	`key_name`,
	`launch_index`,
	`launched_at`,
	`locked_by`,
	`node`,
	`not-tags`,
	`not-tags-any`,
	`power_state`,
	`progress`,
	`project_id`,
	`ramdisk_id`,
	`sort_key`,
	`tags`,
	`task_state`,
	`terminated_at`,
	`user_id`
	)
	VALUES
	(
		"%s",
		"%s",
		"aa0d0e4ed58d11eabb6310bf48324232",
		"%s",
		"%s",
		"%s",
		"%s",
		"%s",
		"基于代价模型",
		"17827776665",
		"100",
		"0",
		'[{"href":"http:\/\/10.10.203.2:8774\/v2.1\/cea9d1e3863243e596af8657a6bab552\/servers\/821db4c8-9140-45a7-8cf9-54efbbfd471c","rel":"self"},{"href":"http:\/\/10.10.203.2:8774\/cea9d1e3863243e596af8657a6bab552\/servers\/821db4c8-9140-45a7-8cf9-54efbbfd471c","rel":"bookmark"}]',
		"node-4.domain.tld",
		"ACTIVE",
		"%s",
		"%s",
		"%s",
		"2020-11-01 15:21:23",
		"2020%s",
		"%s2020",
		"192.168.%s.%s",
		"fe80:0000:0001:0000:0440:44ff:1233:%s",
		"%s",
		"key%s",
		"%s",
		"2020-11-01 15:25:23",
		"name%s",
		"node%s",
		"tags%s",
		"tags-any%s",
		"%s",
		"%s",
		"project%s",
		"ramdisk%s",
		"550%s",
		"tags%s",
		"1",
		"2020-11-01 15:28:23",
		"user%s");"""%(b,b,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,a,)
	cursor.execute(sql)
cursor.close()  # 关闭游标
db.close()  # 关闭数据库连接