from steem import Steem

wif = {
	"posting": "5JQznmiJ5qGqCk6LuKd1dXbkR4F2epm6VmqwGGRjPMfJVyggxNN",
}
steem = Steem(keys=wif)
# 主题
tags = ['cn','life']
# 内容
with open('./liangzijinrong.jpg','r') as fp:
	s = fp.read()
	content = s
# 标题
title = 'love'
p = steem.post(title,content,author='changeday',tags=tags)
print(p)
