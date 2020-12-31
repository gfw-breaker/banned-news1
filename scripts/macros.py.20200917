#!/usr/bin/python
# coding: utf-8

git_base_url = "https://github.com/gfw-breaker/banned-news3/blob/master/pages"

head = ''

#head = "#### 由于频繁封锁，请参考 [手把手翻墙教程](https://github.com/gfw-breaker/guides/wiki/)，安卓用户请使用 [网门](https://github.com/gfw-breaker/bn-android/blob/master/ogate.md) 或 [禁闻聚合](https://github.com/gfw-breaker/bn-android) 免翻墙观看热门YouTube频道 \n\n"

#head += "#### 旧版本禁闻聚合安卓APP已经失效，请删除，然后重新[下载安装新版本](https://github.com/gfw-breaker/bn-android) \n\n"

#head += "#### [热点新闻](热点新闻.md)  &nbsp;&nbsp;|&nbsp;&nbsp; [明慧二十周年报告](https://github.com/gfw-breaker/mh-reports/blob/master/README.md) &nbsp;&nbsp;|&nbsp;&nbsp;[明慧期刊](https://github.com/gfw-breaker/mh-qikan) &nbsp;&nbsp;|&nbsp;&nbsp; [明慧海外之窗](https://github.com/gfw-breaker/mh-news/blob/master/README.md) &nbsp;&nbsp;|&nbsp;&nbsp; [神韵特别报道](https://github.com/gfw-breaker/mh-news/blob/master/shenyun.md) \n"

#head += "#### [法轮功真相](https://github.com/gfw-breaker/truth/blob/master/README.md) &nbsp;&nbsp;|&nbsp;&nbsp; [九评共产党](../../../../9ping.md/blob/master/README.md) &nbsp;|&nbsp; [解体党文化](../../../../jtdwh.md/blob/master/README.md)  &nbsp;|&nbsp; [共产主义的终极目的](../../../../gczydzjmd.md/blob/master/README.md) &nbsp;|&nbsp; [魔鬼在统治我们的世界](../../../../mgztzwmdsj.md/blob/master/README.md) \n"


menu = "#### [首页](https://github.com/gfw-breaker/banned-news3/blob/master/README.md) &nbsp;&nbsp;|&nbsp;&nbsp; [法轮功真相](https://github.com/begood0513/basic/blob/master/README.md)  &nbsp;&nbsp;|&nbsp;&nbsp; [手把手翻墙教程](https://github.com/gfw-breaker/guides/wiki)  &nbsp;&nbsp;|&nbsp;&nbsp; [一键翻墙软件](https://github.com/gfw-breaker/nogfw/blob/master/README.md)  \n\n"


tail = "#### [首页](https://github.com/gfw-breaker/banned-news3/blob/master/README.md) &nbsp;|&nbsp; [一键翻墙软件](https://github.com/gfw-breaker/nogfw/blob/master/README.md) &nbsp;| [《九评共产党》](https://github.com/gfw-breaker/9ping.md/blob/master/README.md#九评之一评共产党是什么) | [《解体党文化》](https://github.com/gfw-breaker/jtdwh.md/blob/master/README.md) | [《共产主义的终极目的》](https://github.com/gfw-breaker/gczydzjmd.md/blob/master/README.md)\n\n"

#proxy = "\n\n#### [翻墙必看视频（武汉肺炎、香港反送中、法轮功、八九六四...）](https://github.com/gfw-breaker/banned-news3/blob/master/pages/link3.md)\n\n"

proxy = "\n\n"
#proxy += "#### [ 🎬  《红墙的记忆》- 4.25中南海万人和平上访纪实](http://158.247.195.190:10000/videos/legend/425.html)\n\n"
#proxy += "#### [ 🎬  《永恒的五十分钟》（长春电视插播事件改编） ](http://158.247.195.190:10000/videos/news/ComingForYou-2.html)\n\n"
proxy += "#### 💥 [《伪火》 - 天安门自焚真相 ](http://158.247.195.190:10000/videos/blog/weihuo.html)&nbsp; |&nbsp; [“1400例”谎言揭秘  ](http://158.247.195.190:10000/videos/blog/jiexi1400.html)\n\n"
proxy += "#### [ 🎬  翻墙必看视频（八九六四、法轮功、709大抓捕、香港反送中 ...）](https://github.com/gfw-breaker/banned-news3/blob/master/pages/link4.md)\n\n"
proxy += "#### 网站代理：[大纪元新闻网](http://158.247.195.190:10080/gb/) &nbsp;|&nbsp; [新唐人电视台](http://158.247.195.190:8808/gb/)  &nbsp;|&nbsp; [YouTube热门频道](http://158.247.195.190/youtube.html) &nbsp;|&nbsp; [网门免翻墙](http://158.247.195.190:11000/show.aspx?name=ogHome)\n\n"
#proxy += "#### [ 💥 李锐评习近平：没想到文化程度这么低（李锐是毛泽东秘书、习仲勋挚友、前中组部副部长）](http://158.247.195.190:10000/videos/res/Communist/lirui-xi.html)\n\n"
#proxy += "#### [ 💥 江泽民失态怒斥并威胁香港记者（ “图样图森破”，“谈笑风生” ）](http://158.247.195.190:10000/videos/res/realjzm/naive.html)\n\n"
proxy += "#### 💥 [九评共产党](http://158.247.195.190:10000/videos/res/jiuping/)&nbsp; |&nbsp; [漫谈党文化](http://158.247.195.190:10000/videos/res/mtdwh/)&nbsp; |&nbsp; [共产主义的终极目的](http://158.247.195.190:10000/videos/res/zjmd/)&nbsp; |&nbsp; [魔鬼在統治著我們的世界](http://158.247.195.190:10000/videos/res/TheSpecter/)  \n\n"

def write_page(channel, f_name, f_path, title, link, content):
	new_link = git_base_url + '/' + channel + '/' + f_name
	body = '### ' + title
	body += "\n------------------------\n\n" + menu + "\n\n" +  content
	body += "\n<hr/>\n手机上长按并复制下列链接或二维码分享本文章：<br/>"
	body += "\n" + new_link + " <br/>"
	body += "\n<a href='" + new_link + "'><img src='" + new_link + ".png'/></a> <br/>"
	body += "\n原文地址（需翻墙访问）：" + link + "\n"
	body += "\n\n------------------------\n" + tail 
	body += "\n<img src='http://gfw-breaker.win/banned-news3/" + f_path[3:] + "' width='0px' height='0px'/>"
	fh = open(f_path, 'w')
	fh.write(body)
	fh.close()


def get_links():
	result = ""
	site_base_url = "http://158.247.195.190:10000/videos/news/"
	idx_file = '/usr/local/nginx/html/videos/news/readme.txt'
	lines = open(idx_file, "r").read().splitlines()
	for line in lines[1:4][::-1]:
		cols = line.split(',')
		url_path = site_base_url + cols[0] + '.html'
		title = cols[1]
		md_link = "#### [ 🔥 %s](%s)\n\n" % (title, url_path)
		result = result + md_link
	return result


proxy += get_links()

