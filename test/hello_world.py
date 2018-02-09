from bottle import route , run,request
import json

dict = {"meesage":"hello"}

@route('/<item_id>')
def modify_item(item_id):
    return  item_id+'さんこんにちは！'

@route('/morning/<user>')
def api(user):
    a = user+',good morning!'
    dict["meesage"] = a
    return dict

@route('/afternoon/<user>')
def api(user):
    a =json.dumps([user+',hello!'])
    dict["meesage"] = a
    return dict

run(host='0.0.0.0',port=3308)