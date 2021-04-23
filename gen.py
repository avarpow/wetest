import pandas as pd
import json
dangshi_raw=pd.read_excel("dangshi.xlsx")
xinzhongguo_raw=pd.read_excel("xinzhongguo.xlsx")
gaigekaifang_raw=pd.read_excel("gaigekaifang.xlsx")
fazhanshi_raw=pd.read_excel("fazhanshi.xlsx")
out={}
out["dangshi"]=[]
out["xinzhongguo"]=[]
out["gaigekaifang"]=[]
out["fazhanshi"]=[]
for i in range(0,len(dangshi_raw)):
    t={}
    t["question"]=dangshi_raw['problem'][i]
    t["option"]={}
    t["option"]["A"]=dangshi_raw['cha'][i]
    t["option"]["B"]=dangshi_raw['chb'][i]
    t["option"]["C"]=dangshi_raw['chc'][i]
    t["true"]=dangshi_raw['real'][i]
    t["type"]=1
    t["scores"]=10
    t['checked']=False
    out["dangshi"].append(t)
for i in range(0,len(xinzhongguo_raw)):
    t={}
    t["question"]=xinzhongguo_raw['problem'][i]
    t["option"]={}
    t["option"]["A"]=xinzhongguo_raw['cha'][i]
    t["option"]["B"]=xinzhongguo_raw['chb'][i]
    t["option"]["C"]=xinzhongguo_raw['chc'][i]
    t["true"]=xinzhongguo_raw['real'][i]
    t["type"]=1
    t["scores"]=10
    t['checked']=False
    out["xinzhongguo"].append(t)
for i in range(0,len(gaigekaifang_raw)):
    t={}
    t["question"]=gaigekaifang_raw['problem'][i]
    t["option"]={}
    t["option"]["A"]=gaigekaifang_raw['cha'][i]
    t["option"]["B"]=gaigekaifang_raw['chb'][i]
    t["option"]["C"]=gaigekaifang_raw['chc'][i]
    t["true"]=gaigekaifang_raw['real'][i]
    t["type"]=1
    t["scores"]=10
    t['checked']=False
    out["gaigekaifang"].append(t)

for i in range(0,len(fazhanshi_raw)):
    t={}
    t["question"]=fazhanshi_raw['problem'][i]
    t["option"]={}
    t["option"]["A"]=fazhanshi_raw['cha'][i]
    t["option"]["B"]=fazhanshi_raw['chb'][i]
    t["option"]["C"]=fazhanshi_raw['chc'][i]
    t["true"]=fazhanshi_raw['real'][i]
    t["type"]=1
    t["scores"]=10
    t['checked']=False
    out["fazhanshi"].append(t)

out_all=json.dumps(out,ensure_ascii=False,indent=4)
with open("test.json",'w') as fs:
    fs.write(out_all)
print(out_all)