from steem import Steem
def bitalk_log(json):
	try:
		wif = json['wif']
		steem = Steem(keys=wif)
		# 主题
		tags = json['tags']
		# 内容
		content = json['content']
		title = json['title']
		author = json['author']
		permlink = json['permlink']
		p = steem.post(title=title,body=content,author=author,tags=tags)
		print(p)
	except Exception as e:
		print(e)
json = {
	"tags":"['cn','life']",
	"content":"'来两张图片给大家'+'  '+'https://ipfs.busy.org/ipfs/QmdXEj3eyCX76MGaZRL8vMr45ts6xBRnqo9W6D7D2fuNtZ'+'  '+'https://ipfs.busy.org/ipfs/QmREWeH3kHQ4DXbS2DBxL3tmRkCkTkwzc6aCgmL4YPVA8r'",
	"title":"'love'",
	"author":"'changeday'",
	"permlink":"'29qby5'",
	'wif':'{"posting": "5JQznmiJ5qGqCk6LuKd1dXbkR4F2epm6VmqwGGRjPMfJVyggxNN"}',
}
bitalk_log(json)
if __name__ == '__main__':
	json = {
		"tags": "['cn','life']",
		"content": "'来两张图片给大家'+'  '+'https://ipfs.busy.org/ipfs/QmdXEj3eyCX76MGaZRL8vMr45ts6xBRnqo9W6D7D2fuNtZ'+'  '+'https://ipfs.busy.org/ipfs/QmREWeH3kHQ4DXbS2DBxL3tmRkCkTkwzc6aCgmL4YPVA8r'",
		"title": "'love'",
		"author": "'changeday'",
		"permlink": "'29qby5'",
		'wif': '{"posting": "5JQznmiJ5qGqCk6LuKd1dXbkR4F2epm6VmqwGGRjPMfJVyggxNN"}',
	}
	bitalk_log(json)

