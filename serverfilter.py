import json
import os.path

path = "./split_data/"
fnames = ["11", "12", "17", "25", "26", "28"]
for fname in fnames:
    fname = path + fname
    # if os.path.exists(fname+"_http_5th_httponly.json"):
    #     continue
    print("Filtering {}".format(fname))
    with open(fname + "_http.json", 'r') as f:
        data = f.read()
    jsons = json.loads(data)
    jsons_5th = []
    for item in jsons:
        if "10.0.0.5" in json.dumps(item) and "404" not in list(item['_source']['layers']['http'].keys())[0]:
            jsons_5th.append(item)
    if len(jsons_5th) > 0:
        print(jsons_5th[0])
    with open(fname + "_http_5th_httponly.json", 'w') as f:
        for item in jsons_5th:
            f.write(json.dumps(item['_source']['layers']['http']))
            f.write('\n')
