import random, time
from tabulate import tabulate
import pandas as pd
lst = ["Amazon","Flipkart","Myntra","Meesho"]
Z = {
     "Amazon" : {'Company Name':["Amazon"],"Date":["15-10-2021"],"Vendor Name":["Jim Carrey"], "Batch Number":["777"]},
     "Flipkart" : {'Company Name':["Flipkart"],"Date":["16-10-2021"],"Vendor Name":["Tom Cruise"],"Batch Number":["778"]},
     "Myntra" : {'Company Name' :["Myntra"],"Date":["17-10-2021"],"Vendor Name":["Chris Evans"], "Batch Number":["779"]},
     "Meesho" : {'Company Name' :["Meesho"],"Date":["18-10-2021"],"Vendor Name":["Johnny Depp"], "Batch Number":["800"]}

}
ans = []
flag = 0
for i in range(16):
    idx = random.randint(0,3)
    new = Z[lst[idx]]
    if(not flag):
        ans = pd.DataFrame(new)
        flag = 1
    else:
        ans = pd.concat([ans,pd.DataFrame(new)],ignore_index=True)
print("\n")
for i in ans.head(5):
    print(i)
print("\n")
print(tabulate(ans.head(16), headers='keys', tablefmt='fancy_grid'))
