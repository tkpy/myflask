from steem import Steem

wif = {
	"posting": "5JQznmiJ5qGqCk6LuKd1dXbkR4F2epm6VmqwGGRjPMfJVyggxNN",
}
steem = Steem(keys=wif)
# 主题
tags = ['cn','life']
# 内容
f = open('./liangzijinrong.jpg','r',encoding='UTF-8')
content = f.read()
# 标题
title = 'love'
author = 'changeday'
permline = ''
p = steem.post(title=title,body=content,author=author,tags=tags)
print(p)
