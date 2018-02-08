from bottle import route , run,request
import dataset
import json
import sys
import urllib.parse
import urllib.request
db = dataset.connect('mysql://roots:rootroot@127.0.0.1:3311/mysql')
table = db['sample']
keyid = "fdbe93860953f0d14f763117f55b38ab"
url = "https://api.gnavi.co.jp/RestSearchAPI/20150630/"



@route('/')
def normal_page():
    return 'wa-i'

@route('/<user_id>',method="get")
def modify_item(user_id):
    s_data = table.find_one(id=user_id)
    freeword = s_data['name']
    print (freeword)
    query = [
        ("format", "json"),
        ("keyid", keyid),
        ("freeword", freeword),
        ("freeword_condition", '2')
    ]
    url = "https://api.gnavi.co.jp/RestSearchAPI/20150630/"
    # URL生成
    url += "?{0}".format(urllib.parse.urlencode(query))
    # API実行
    try:
        result = urllib.request.urlopen(url).read()
        data = json.loads(result)
        print("繋がっている")
    except ValueError:
        print(u"APIアクセスに失敗しました。")
        sys.exit()

    ####
    # 取得した結果を解析
    ####
    data = json.loads(result)
    print(data)
    # エラーの場合
    if "error" in data:
        if "message" in data:
            print(u"{0}".format(data["message"]))
        else:
            print (u"データ取得に失敗しました。")
        sys.exit()

    # ヒット件数取得
    total_hit_count = None
    if "total_hit_count" in data:
        total_hit_count = data["total_hit_count"]

    # レストランデータがなかったら終了
    if not "rest" in data:
        print(u"レストランデータが見つからなかったため終了します。")
        sys.exit()

    # ヒット件数表示
    print("{0}件ヒットしました。".format(total_hit_count))
    print("----")

    # 出力件数
    disp_count = 0

    # レストランデータ取得
    for rest in data["rest"]:
        line = []
        id = ""
        name = ""
        access_line = ""
        access_station = ""
        access_walk = ""
        code_category_name_s = []
        # タブ区切りで出力
        print("\t".join(line))
        disp_count += 1

    # 出力件数を表示して終了
    print("----")
    print(u"{0}件出力しました。".format(disp_count))


@route('/', method="post")
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