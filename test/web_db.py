from bottle import route , run,request
import dataset
import json
db = dataset.connect('mysql://roots:rootroot@127.0.0.1:3311/mysql')
table = db['sample']


@route('/')
def normal_page():
    return 'wa-i'

@route('/<user_id>',method="get")
def modify_item(user_id):
    result = table.find_one(id=user_id)

    # print (result['id'])

    return ' <form method="post">ID:<input type="text" name="id" value="'+str(result['id'])+'">名前：<input type="text" name="name" value="'+result['name']+'"><br><input type="submit"></form>'
    # return result['name']+',get'

@route('/<user_id>/<user_name>',method="post")
def post_page(user_id,user_name):
    table.insert(dict(id=user_id, name=user_name))
    return user_id+',post'

@route('/<user_id>',method="delete")
def delete_page(user_id):
    table.delete(id=user_id)
    return user_id+',delete'

@route('/<user_id>/<user_name>',method="put")
def put_page(user_id,user_name):
    data = dict(id=user_id, name=user_name)
    table.upsert(data, ['id'])
    return user_id+',put'



# #insert
# table.insert(dict(id=4,name='arakita'))
# #update
# data = dict(id=4, name='arakita')
# table.upsert(data, ['id'])
# #delete
# table.delete(name='arakita')
# #select
# results = table.find(order_by='id')
# for r in results:
#     print(r)

run(host='localhost', port=3309)