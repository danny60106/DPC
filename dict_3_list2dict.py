"""
Converting list into dictionary with index as key

"""

list = [2, 55, 27, 15, 39]

dict1={}

for k, v in enumerate(list):
    print("k, v:", k, v)
    dict1[k] = v

print(dict1)    

#dict1 = {i:j for i,j in enumerate(list)}
#print(dict1)

dict2 = dict(enumerate(list))
print(dict2)

# 產生按原來數值排序後的 index list
# 第一個數字是最大值在原來list的index，其餘類推
sorted_index = sorted(dict2, key=dict2.get, reverse=True)
print(sorted_index) 

for i, v in enumerate(sorted_index[:2]):
    print("Top#%d: %2d" % (i+1, dict2[v]))  