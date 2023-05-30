# This is a Python file for return filtered pcap data.

# coding=utf-8


from datetime import datetime
import json

ip_list = ["99.999.9.11", "99.999.9.12", "99.999.9.17", "99.999.9.25", "99.999.9.26", "99.999.9.28"]
ip_get = ["10.0.0.3"]
exip_list = ["99.999.9.3", "99.999.9.5", "99.999.9.7", "99.999.9.10", "99.999.9.13", "99.999.9.14",
             "99.999.9.16", "99.999.9.18", "99.999.9.19", "99.999.9.20", "99.999.9.21", "99.999.9.22",
             "99.999.9.23", "99.999.9.27", "99.999.9.29", "99.999.9.30", "99.999.9.31", "99.999.9.32",
             "99.999.9.33", "99.999.9.34", "99.999.9.35", "99.999.9.36", "99.999.9.37"]
def is_json(logstr):
    try:
        json.loads(logstr)
    except Exception as e:
        return False
    else:
        return True

'''
功能：排除无关ip（非本组分析）
'''
def exclude_pcap(pcapjson):
    pcapjsonstr = json.dumps(pcapjson, ensure_ascii=False)
    flag = 0
    for exipstr in exip_list:
        if exipstr not in pcapjsonstr:
            flag = flag + 1

    if flag == 23:
        return True
    return False


'''
功能：提取相关ip（本组分析）
'''
def include_pcap(pcapjson):
    pcapjsonstr = json.dumps(pcapjson, ensure_ascii=False)
    for ipstr in ip_list:
        if ipstr in pcapjsonstr:
            return True

    return False

def get_pcap(pcapjson):
    pcapjsonstr = json.dumps(pcapjson, ensure_ascii=False)
    for ipstr in ip_get:
        if ipstr in pcapjsonstr:
            return True

    return False

def datasplit(filename):
    f = open(filename, "r")

    wf1 = open("./11.json", "w")
    wf2 = open("./12.json", "w")
    wf3 = open("./17.json", "w")
    wf4 = open("./25.json", "w")
    wf5 = open("./26.json", "w")
    wf6 = open("./28.json", "w")

    fileindexpr = [wf1, wf2, wf3, wf4, wf5, wf6]

    #print(type(fileindexpr))
    for str in f:
        for ipstr in ip_list:
            if ipstr in str:
                fileindexpr[ip_list.index(ipstr)].write(str)


    f.close()
    wf1.close()
    wf2.close()
    wf3.close()
    wf4.close()
    wf5.close()
    wf6.close()

'''
提取数据，将数据集划分为exclude和include两个集合
'''
def dataextract(filename):
    f = open(filename, "r")

    wf1 = open("./exclude.json", "w")
    wf2 = open("./include.json", "w")
    #wf3 = open("./temp.json", "w")
    jsonstr = ''

    for str in f:
        #wf3.write(str)
        if str == '  {\n':
            jsonstr = jsonstr + str[0: len(str)-1]
            for str in f:
                #wf3.write(str)
                if str != '  },\n':
                    jsonstr = jsonstr + str[0: len(str)-1]
                else:
                    break

            jsonstr = jsonstr + str[0: len(str)-2]
            # print(jsonstr)
            # jsonstr.replace('\t', '')
            # jsonstr.replace(' ', '')
            # print(jsonstr)
            try:
                json_object = json.loads(jsonstr)
            except:
                print(jsonstr)
                jsonstr = ''
                continue
            json_object = json.loads(jsonstr)

            if include_pcap(json_object):
                wf2.write(json.dumps(json_object, ensure_ascii=False)+'\n')
            if exclude_pcap(json_object):
                wf1.write(json.dumps(json_object, ensure_ascii=False) + '\n')
            jsonstr = ''

    f.close()
    wf1.close()
    wf2.close()
    #wf3.close()
    
#获取指定ip的日志和指定字段
def get_ip(filename):
    wf1 = open("./ip28_3.json", "w")
    with open(filename, 'r') as f:
        for line in f:
            json_data = json.loads(line)
            frame_time, http, data_text_lines = get_specific_fields(json_data)
            output_data = {
                "frame_time": frame_time,
                "http": http,
                "data_text_lines": data_text_lines
            }
            if get_pcap(output_data):
                wf1.write(json.dumps(output_data, ensure_ascii=False) + '\n')
            

    f.close()
    wf1.close()
    # wf2.close()
## 输出   {    "_index": "packets-2023-04-26",    "_type": "doc",    "_score": null,    "_source": {      "layers": {        "frame": {          "frame.encap_type": "1",          "frame.time": "Apr 26, 2023 16:52:46.729900000 中国标准时间",          "frame.offset_shift": "0.000000000",          "frame.time_epoch": "1682499166.729900000",          "frame.time_delta": "1.020011000",          "frame.time_delta_displayed": "1.020011000",          "frame.time_relative": "441941.102703000",          "frame.number": "5884607",          "frame.len": "42",          "frame.cap_len": "42",          "frame.marked": "0",          "frame.ignored": "0",          "frame.protocols": "eth:ethertype:arp"        },        "eth": {          "eth.dst": "ff:ff:ff:ff:ff:ff",          "eth.dst_tree": {            "eth.dst_resolved": "Broadcast",            "eth.dst.oui": "16777215",            "eth.addr": "ff:ff:ff:ff:ff:ff",            "eth.addr_resolved": "Broadcast",            "eth.addr.oui": "16777215",            "eth.dst.lg": "1",            "eth.lg": "1",            "eth.dst.ig": "1",            "eth.ig": "1"          },          "eth.src": "e2:33:ee:ef:45:42",          "eth.src_tree": {            "eth.src_resolved": "e2:33:ee:ef:45:42",            "eth.src.oui": "14824430",            "eth.addr": "e2:33:ee:ef:45:42",            "eth.addr_resolved": "e2:33:ee:ef:45:42",            "eth.addr.oui": "14824430",            "eth.src.lg": "1",            "eth.lg": "1",            "eth.src.ig": "0",            "eth.ig": "0"          },          "eth.type": "0x0806"        },        "arp": {          "arp.hw.type": "1",          "arp.proto.type": "0x0800",          "arp.hw.size": "6",          "arp.proto.size": "4",          "arp.opcode": "1",          "arp.src.hw_mac": "e2:33:ee:ef:45:42",          "arp.src.proto_ipv4": "10.255.0.1",          "arp.dst.hw_mac": "00:00:00:00:00:00",          "arp.dst.proto_ipv4": "10.255.112.32"        }      }    }  }]

# def save_to_json_file(data, file_path):
#     with open(file_path, "w") as file:
#         json.dump(data, file, indent=4)
        
def get_specific_fields(data):
    try:
        # data = json.loads(json_data)
        frame_time = data["_source"]["layers"]["frame"]["frame.time"]
        http = data["_source"]["layers"]["http"]
        data_text_lines = data["_source"]["layers"].get("data-text-lines")
        
        return frame_time, http, data_text_lines
    except KeyError:
        # 如果字段不存在或无法访问到特定字段，返回None
        return None, None, None





if __name__ == '__main__':
    # dataextract("./dataset_0415.json")
    # datasplit("./include.json")
    get_ip("./28.json")
    

