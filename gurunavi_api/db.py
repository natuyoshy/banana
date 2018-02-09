import dataset
import mock

db = dataset.connect('mysql://roots:rootroot@127.0.0.1:3311/mysql')

table = db['sample']
print("最初")
#insert
table.insert(dict(id=4,name='arakita'))
#update
data = dict(id=4, name='arakita')
table.upsert(data, ['id'])
#delete
table.delete(name='arakita')
#select
results = table.find(order_by='id')
for r in results:
    print(r)