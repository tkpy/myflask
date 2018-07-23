from steem import Steem
import json,jsonpath
def bitalk_log(json_dict):
	try:
		# 私钥
		wif = json_dict['wif']
		steem = Steem(keys=wif)
		# 主题
		tags = json_dict['tags']
		# 内容
		content = json_dict['content']
		# 标题
		title = json_dict['title']
		# 作者
		author = json_dict['author']
		# 唯一标识
		permlink = json_dict['permlink']
		# 发帖
		p = steem.post(title=title,body=content,author=author,tags=tags,permlink=permlink)
		return p
	except Exception as e:
		print(e)
json_dict = {
		"tags": ['cn','life'],
		"content": '来两张图片给大家',
		"title": "python api test",
		"author": "changeday",
		"permlink": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
		'wif': {"posting": "5JQznmiJ5qGqCk6LuKd1dXbkR4F2epm6VmqwGGRjPMfJVyggxNN"},
	}
res = bitalk_log(json_dict)
print('发帖返回内容',res)

res =  {
	'ref_block_num':37897,
	'ref_block_prefix':119761435,
	'expiration':'2018-7-23T04:03:12',
	'operation':[['comment',{'parent_author':'','parent_permlink':'cn',
				'author':'changeday','permlink':'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
				'title':"python api test","body":'来两张图片给大家','json_metadata':'{"tags":["cn","life"]}'
				}]],
	'extensions':[],
	'signatures':['200e16ba4fba4fd6f0e1fddeedjsaou09172404p1joau971308bihyu00yjt8u9n7']
}



