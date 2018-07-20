from steem import Steem

def bitalk_log(json_dict):
	try:
		wif = json_dict['wif']
		steem = Steem(keys=wif)
		# 主题
		tags = json_dict['tags']
		# 内容
		content = json_dict['content']
		title = json_dict['title']
		author = json_dict['author']
		permlink = json_dict['permlink']
		# 发帖
		p = steem.post(title=title,body=content,author=author,tags=tags,permlink=permlink)
		# 回帖
		s = steem.post(title='',body='这是我的回帖',author=author,reply_identifier='@{}/{}'.format(author,permlink))
		res = {'p':p,'s':s}
		return res
	except Exception as e:
		print(e)
json_dict = {
		"tags": ['cn','life'],
		"content": '来两张图片给大家'+'  '+'https://ipfs.busy.org/ipfs/QmdXEj3eyCX76MGaZRL8vMr45ts6xBRnqo9W6D7D2fuNtZ'+'  '+'https://ipfs.busy.org/ipfs/QmREWeH3kHQ4DXbS2DBxL3tmRkCkTkwzc6aCgmL4YPVA8r',
		"title": "python api test",
		"author": "changeday",
		"permlink": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
		'wif': {"posting": "5JQznmiJ5qGqCk6LuKd1dXbkR4F2epm6VmqwGGRjPMfJVyggxNN"},
	}
res = bitalk_log(json_dict)
print('发帖返回内容',res['p'])
print('回帖返回内容',res['s'])


