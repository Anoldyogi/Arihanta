#just a demo
supermarket={
    'store1':{
        "name":'durga Store',
        "item":[
            {'name':'soup','qty':20},
            {'name':'brush','qty':30},
            {'name':'pen','qty':40}
            ]
        },
    'store2':{
        "name":'sunny store',
        "item":[
            {'name':'python','qty':100},
            {'name':'django','qty':200},
            {'name':'flask','qty':300}
            ]
        }
    }


print(supermarket['store1']['name'])
print(supermarket.get('store1')['name'])
# name of all items present in store 1

for d in supermarket['store1']['item']:
    print(d['name'])


# how many django books are present
for d in supermarket['store2']['item']:
    if d['name']=='django':
        print(d['qty'])
