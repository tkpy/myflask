from steem import Steem
import jsonpath,json
def bitalk_log(json_dict):
	try:
		wif = json_dict['wif']
		steem = Steem(keys=wif)
		# 内容
		content = json_dict['content']
		# 用户名
		author = json_dict['author']
        # 唯一标识
		permlink = json_dict['permlink']
		# 作者
		writer = json_dict['writer']
		# 回帖
		s = steem.post(title='',body=content,author=author,reply_identifier='@{}/{}'.format(writer,permlink))
		return s
	except Exception as e:
		print(e)
json_dict = {
		# 回帖内容
        "content": '很好',
		# 用户名
		"author": "changeday",
		# 唯一标识
		"permlink": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
		# 私钥
		'wif': {"posting": "5JQznmiJ5qGqCk6LuKd1dXbkR4F2epm6VmqwGGRjPMfJVyggxNN"},
		# 作者
		'writer': 'changeday'
	}
res = bitalk_log(json_dict)
print('回帖返回内容',res)


