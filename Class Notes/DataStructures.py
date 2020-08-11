simple_list = [1,2,3,4]
simple_list.extend([5,6,7])
print(simple_list)  # [1, 2, 3, 4, 5, 6, 7]
del simple_list[0]
print(simple_list)  # [2, 3, 4, 5, 6, 7]

d = {'name': 'Rich'}
print(d.items())  # dict_items([('name', 'Rich')])
for k, v in d.items():
    print(k, v)  # name Rich
del(d['name'])
print(d)  # {}
    
t = (1,2,3)
print(t.index(1))  # 0  ** index of 1 is 0

s = {'Max', 'Anna', 'Rich'}
print(s)  # {'Max', 'Anna', 'Rich'}