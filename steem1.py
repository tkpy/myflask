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
content = {"image":'[https://ipfs.busy.org/ipfs/QmdXEj3eyCX76MGaZRL8vMr45ts6xBRnqo9W6D7D2fuNtZ]'}
# 标题
title = 'love'
author = 'changeday'
permline = ''
p = steem.post(title=title,body=content,author=author,tags=tags)
print(p)
