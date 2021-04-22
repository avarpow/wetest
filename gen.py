import pandas as pd
import json
danxuan_raw=pd.read_excel("danxuan.xlsx")
duoxuan_raw=pd.read_excel("duoxuan.xlsx")
out={}
out["test1"]=[]
for i in range(0,len(danxuan_raw)):
    t={}
    t["question"]=danxuan_raw['problem'][i]
    t["option"]={}
    t["option"]["A"]=danxuan_raw['cha'][i]
    t["option"]["B"]=danxuan_raw['chb'][i]
    t["option"]["C"]=danxuan_raw['chc'][i]
    t["option"]["D"]=danxuan_raw['chd'][i]
    t["true"]=danxuan_raw['real'][i]
    t["type"]=1
    t["scores"]=10
    t['checked']=False
    out["test1"].append(t)
for i in range(0,len(duoxuan_raw)):
    t={}
    t["question"]=duoxuan_raw['problem'][i]
    t["option"]={}
    t["option"]["A"]=duoxuan_raw['cha'][i]
    t["option"]["B"]=duoxuan_raw['chb'][i]
    t["option"]["C"]=duoxuan_raw['chc'][i]
    t["option"]["D"]=duoxuan_raw['chd'][i]
    t["true"]=duoxuan_raw['real'][i]
    t["type"]=2
    t["scores"]=10
    t['checked']=False
    out["test1"].append(t)
out_danxuan_rawa=json.dumps(out,ensure_ascii=False,indent=4)
with open("test.json",'w') as fs:
    fs.write(out_danxuan_rawa)
print(danxuan_raw)