
import requests
import os
import json
import time


#目录不存在则创建
hero_dir = 'F:/LocalData/WangzheImageSpider/'
if not os.path.exists(hero_dir):
	os.mkdir(hero_dir)
x = 0  # 用于记录下载的图片张数
start = time.time()  # 开始时间
JSONbase = requests.get('http://pvp.qq.com/web201605/js/herolist.json').content
JSONfile = json.loads(JSONbase)
print(JSONfile)

jsonRange = range(len(JSONfile))  # JSON文件的长度范围
# print(JSONfile, jsonRange)
for i in jsonRange:
	num = JSONfile[i]['ename']  # 编号
	name = JSONfile[i]['cname']  # 名称
	if num == 518:  # 原因是远程json数据中马超缺少skin_name字段,手动补全!
		JSONfile[i]['skin_name'] = "幸存者|神威"
	skinname = JSONfile[i]['skin_name'].split('|')  # 对应英雄的皮肤数量
	skinlen = range(1, len(skinname) + 1)    # 皮肤数量范围
	# 循环英雄范围
	for index in skinlen:
		pictureURL = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/' + str(num) + '/' + str(num) + '-bigskin-' + str(index) + '.jpg'
		# print('pictureURL', pictureURL, skinlen)
		picture = requests.get(pictureURL).content  # 获取到图片的二进制内容
		# 保存图片到本地
		with open(hero_dir + name + '_' + skinname[index - 1] + '.jpg', 'wb') as f:
			f.write(picture)
			x = x + 1
			print('正在下载第' + str(x) + '张照片', '英雄数量:', len(JSONfile), i)
end = time.time()  # 程序结束时间
time = (end - start) / 1000  # 程序用时 s/秒
print('下载完毕!!!', '路径:', hero_dir)

