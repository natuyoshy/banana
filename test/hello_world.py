from bottle import route , run,request
import json

@route('/<item_id>')
def modify_item(item_id):

    return  item_id+'さんこんにちは！'
@route('/morning/<user>')
def morning_user(user):
    return user+'さん、おはよ！'
@route('/afternoon/<user>')
def api(user):
    # return data+'さん、こんにちは！'
    a =json.dumps([user+'hello!'])
    return a


run(hots='localhost',port=8088)

