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
		p = steem.post(title=title,body=content,author=author,tags=tags)
		return p
	except Exception as e:
		print(e)
json_dict = {
		"tags": ['cn','life'],
		"content": '来两张图片给大家'+'  '+'https://ipfs.busy.org/ipfs/QmdXEj3eyCX76MGaZRL8vMr45ts6xBRnqo9W6D7D2fuNtZ'+'  '+'https://ipfs.busy.org/ipfs/QmREWeH3kHQ4DXbS2DBxL3tmRkCkTkwzc6aCgmL4YPVA8r',
		"title": "python api test",
		"author": "changeday",
		"permlink": "29qby5",
		'wif': {"posting": "5JQznmiJ5qGqCk6LuKd1dXbkR4F2epm6VmqwGGRjPMfJVyggxNN"},
	}
p = bitalk_log(json_dict)
print(p)
# if __name__ == '__main__':
# 	json_dict = {
# 		"tags": ['cn','life'],
# 		"content": "'来两张图片给大家'+'  '+'https://ipfs.busy.org/ipfs/QmdXEj3eyCX76MGaZRL8vMr45ts6xBRnqo9W6D7D2fuNtZ'+'  '+'https://ipfs.busy.org/ipfs/QmREWeH3kHQ4DXbS2DBxL3tmRkCkTkwzc6aCgmL4YPVA8r'",
# 		"title": "'love'",
# 		"author": "'changeday'",
# 		"permlink": "'29qby5'",
# 		'wif': {"posting": "5JQznmiJ5qGqCk6LuKd1dXbkR4F2epm6VmqwGGRjPMfJVyggxNN"},
# 	}
# 	bitalk_log(json_dict)

