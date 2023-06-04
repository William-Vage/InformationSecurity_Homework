import json
import os

def remove_key_value_pairs(json_data):
    updated_json = {}
    try:
        updated_json["http"] = json_data["_source"]["layers"]["http"]
    except KeyError:
        pass
    try:
        updated_json["frame.time"] = json_data["_source"]["layers"]["frame"]["frame.time"]
        updated_json["tcp"] = json_data["_source"]["layers"]["tcp"]
    except KeyError:
        return ''

    # 将更新后的 Python 对象转换回 JSON 格式
    res = json.dumps(updated_json)
    
    return res

def is_json_need(line_cnt, json_object):
    try:
        json_object["_source"]["layers"]["http"]
        return True
    except KeyError:
        return False

path = '/Users/metropolis/Downloads/split_data/'
ip = '12'
oriFile = os.path.join(os.getcwd(), ip + '.json')
storeFile = ip + '_lite.json'
storePath = os.path.join(os.getcwd(), storeFile)
def run():
    with open(storePath, 'w+') as fw:
        with open(oriFile, 'r') as fr:
            for line_cnt, line in enumerate(fr, start=1):
                try:
                    # if not "10.0.0.6" in line:
                    #     continue
                    json_object = json.loads(line)
                    # if not is_json_need(line_cnt, json_object):
                    #     continue
                    updated_json = remove_key_value_pairs(json_object)
                    if updated_json == '':
                        continue
                    fw.write(updated_json)
                    fw.write('\n')
                except json.JSONDecodeError:
                    print(f"JSONDecodeError on line {line_cnt}: unable to parse line as json")
                finally:
                    if line_cnt % 1000 == 0:
                        print(f"current line number is", line_cnt)

run()