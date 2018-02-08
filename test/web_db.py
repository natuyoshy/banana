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
    return table.find_one(id=user_id)

@route('/',method="post")
def post_page():
    json = request.json
    id = str(json['id'])
    name = json['name']
    table.insert(dict(id=id, name=name))
    # return id + "の" + name + 'さんを追加しました'

@route('/<user_id>',method="delete")
def delete_page(user_id):
    result = table.find_one(id=user_id)
    id = str(result['id'])
    name = result['name']
    table.delete(id=user_id)
    return id+"の"+name+'さんを削除しました'

@route('/<user_id>',method="put")
def put_page(user_id):
    json = request.json
    id = str(json['id'])
    name = json['name']
    data = dict(id=id,name=name)
    table.upsert(data, ['id'])
    return id+"の"+name+'の名前を変更しました'

run(host='localhost', port=3309)