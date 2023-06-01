import json
import os.path

from tqdm import tqdm

path = "./split_data/"
fnames = ["11", "12", "17", "25", "26", "28"]
for fname in fnames:
    fname = path + fname
    # if os.path.exists(fname+"_http_5th_httponly_suc.json"):
    #     continue
    print("Filtering {}".format(fname))
    with open(fname + "_http_5th_httponly.json", 'r') as f:
        lines = f.readlines()
    jsons = []
    for line in tqdm(lines, total=len(lines)):
        json_obj = json.loads(line.strip())
        jsons.append(json_obj)
    jsons_suc = []
    for item in jsons:
        j_str = json.dumps(item)
        if "zhangwei" in j_str or "load_data" in j_str or "etc/passwd" in j_str or ".DS_Store" in j_str or "flag" in j_str:
            jsons_suc.append(item)
    if len(jsons_suc) > 0:
        print(jsons_suc[0])
    with open(fname + "_http_5th_httponly_suc.json", 'w') as f:
        for item in jsons_suc:
            f.write(json.dumps(item))
            f.write('\n')
