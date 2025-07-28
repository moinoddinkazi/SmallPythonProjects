list1 = [["Moin","85"],["Mufiz","65"],["Ashaz","35"],["Isaad","25"]]
for item in list1:
     print(item)
dict1 = dict(list1)
for item,weights in dict1.items():
    print(item,weights)

for item,weights in list1:
     print(item,weights)