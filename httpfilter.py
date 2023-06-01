import json
import os.path

from tqdm import tqdm

path = "./split_data/"
fnames = ["11","12","17","25","26","28"]
for fname in fnames:
    fname = path + fname
    # if os.path.exists(fname+"_http.json"):
    #     continue
    print("Filtering {}".format(fname))
    with open(fname+".json", 'r') as f:
        lines = f.readlines()
    jsons = []
    for line in tqdm(lines, total=len(lines)):
        json_obj = json.loads(line.strip())
        if "http" not in json_obj['_source']['layers']:
            continue
        jsons.append(json_obj)
    with open(fname+"_http.json", 'w') as f:
        f.write(json.dumps(jsons))
