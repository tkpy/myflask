from steem import Steem

wif = {
	"posting": "5JQznmiJ5qGqCk6LuKd1dXbkR4F2epm6VmqwGGRjPMfJVyggxNN",
}
steem = Steem(keys=wif)
tags = ['cn','life']
content = 'l love life'
title = 'love'
p = steem.post(title,content,author='changeday',tags=tags)
print(p)
