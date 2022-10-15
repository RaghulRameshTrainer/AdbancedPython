import json
with open(r'C:\Users\RaghulRamesh\PycharmProjects\pythonProject\trainer_info.json','r') as fo:
    data=json.load(fo)
    info=''
    for k in data.keys():
        info+=','+k+','+str(data[k])
    print(info.lstrip(','))


# trans_data={
#      'product':'mobile',
#      'price':30000,
#      'location':'chennai',
#      'warranty':'1 year',
#      'discount':False,
#      'gift':None
# }
#
# with open('transaction.json','w') as fo:
#     json.dump(trans_data,fo,indent=5,sort_keys=True)