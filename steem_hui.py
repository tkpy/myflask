from steem import Steem
import jsonpath,json
def bitalk_log(json_dict):
	try:
		wif = json_dict['wif']
		steem = Steem(keys=wif)
		# 内容
		content = json_dict['content']
		author = json_dict['author']
        # 唯一标识
		permlink = json_dict['permlink']
		# 回帖
		s = steem.post(title='',body='很好',author=author,reply_identifier='@{}/{}'.format(author,'4n3d2a'))
		return s
	except Exception as e:
		print(e)
json_dict = {
        "content": '很好',
		"author": "changeday",
		"permlink": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
		'wif': {"posting": "5JQznmiJ5qGqCk6LuKd1dXbkR4F2epm6VmqwGGRjPMfJVyggxNN"},
	}
res = bitalk_log(json_dict)
print('回帖返回内容',res)


