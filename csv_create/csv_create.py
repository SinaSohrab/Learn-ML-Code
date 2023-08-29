import pandas as pd
import random

random.seed()
name_list = [
    "sina",
    "mohamad",
    "amin",
    "ehsan",
    "setare",
    "zahra",
    "baran",
    "parisa",
    "shayan",
    "ali",
    "sahar",
    "nahal",
    "soroush",
    "gohar",
]
list_number = []
list_name = []
list_i=[]
for i in range(0, 100):
    random_number = random.randint(1, 100)
    list_number.append(random_number)

    random_name = random.choice(name_list)
    list_name.append(random_name)

    list_i.append(i)
data={"name":list_name,"number":list_number,"i":list_i}
df=pd.DataFrame(data)
df.to_csv("csv_create/test.csv",index=False)
