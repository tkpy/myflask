from steem import Steem
import os
import os.path
wif = {
	"posting": "5JQznmiJ5qGqCk6LuKd1dXbkR4F2epm6VmqwGGRjPMfJVyggxNN",
}
steem = Steem(keys=wif)
# 主题
tags = ['cn','life']
# 内容
xiangdui = os.getcwd()
juedui = os.path.abspath(xiangdui)
path = os.path.join(juedui,'liangzijinrong.jpg')
content = path
# 标题
title = 'love'
author = 'changeday'
permline = ''
p = steem.post(title=title,body=content,author=author,tags=tags)
print(p)
