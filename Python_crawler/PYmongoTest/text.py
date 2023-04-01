import redis
from pymongo import MongoClient

client=MongoClient("mongodb://127.0.0.1:27017")
database=client['Chapter6']
collection=database['spider']

# data=[{'id':1323,'name':'kingn34ame','age':20,'salary':999999},
#       {'id':12233,'name':'king34name','age':20,'salary':999999},
#       {'id':123243,'name':'kin34gname','age':20,'salary':999999},
#       {'id':122343,'name':'kin34gname','age':20,'salary':999999},
#       ]
# x=collection.insert_many(data)
# print(x)


# content=[x for x in collection.find({'id':123})]
# print(content)

client=redis.StrictRedis()
# client.lpush('Chapter6',123)
# print(content)
print(client.llen('Chapter6'))
value=client.lpop('Chapter6')
print(value)
print(client.llen('Chapter6'))
