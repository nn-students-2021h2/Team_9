"""
Flask
6.001084089279175 - запрос
5.958044767379761 - Вычисление

Pure
5.116491794586182 - вычисление
5.119417667388916 - запрос

Select
4.932390928268433 - вычисление
4.9333930015563965 - запрос

Selector

4.698530435562134 - запрос
4.682981252670288 - вычисление
"""

d_servers_time = {
    'Flask':{
        'req':6.001084089279175,
        'calculate':5.958044767379761,
    },
    'Pure':{
        'req':5.119417667388916,
        'calculate':5.116491794586182,
    },
    'Select':{
        'req':4.9333930015563965,
        'calculate':4.932390928268433,
    },
    'Selector':{
        'req':4.698530435562134,
        'calculate':4.682981252670288,   
    }
}

l_servers = [i for i in d_servers_time.keys()]
for i in l_servers:
    obj = d_servers_time[i]
    obj['per'] = str((obj['calculate']/(obj['req']/100))*100)
    #obj['per'] = (i['calculate']/i['req']/100)*100

for i in l_servers:
    print(i, " percent= ", d_servers_time[i]['per'])

