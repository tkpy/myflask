from steem import Steem
def bitalk_log():
	try:
		wif = {
			"posting": "5JQznmiJ5qGqCk6LuKd1dXbkR4F2epm6VmqwGGRjPMfJVyggxNN",
		}
		steem = Steem(keys=wif)
		# 主题
		tags = ['cn','life']
		# 内容
		content = '来两张图片给大家'+'  '+"https://ipfs.busy.org/ipfs/QmdXEj3eyCX76MGaZRL8vMr45ts6xBRnqo9W6D7D2fuNtZ"+'  '+'https://ipfs.busy.org/ipfs/QmREWeH3kHQ4DXbS2DBxL3tmRkCkTkwzc6aCgmL4YPVA8r'
		# 标题
		title = 'love'
		author = 'changeday'
		permlink = '29qby5'
		p = steem.post(title=title,body=content,author=author,tags=tags,permlink=permlink)
		print(p)
	except Exception as e:
		print(e)
bitalk_log()