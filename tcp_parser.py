import json
import os

def hex_to_ascii(hex_str):
    hex_str = hex_str.replace(':', '')  # 移除冒号
    bytes_obj = bytes.fromhex(hex_str)  # 将十六进制字符串转换为字节对象
    ascii_str = bytes_obj.decode('ascii')  # 将字节对象解码为ASCII字符串
    return ascii_str

ip = '12'
fileName = ip + '_lite.json'
filePath = os.path.join(os.getcwd(), fileName)
with open(filePath + '.bak', 'w+') as fout:
    with open(filePath, 'r+') as f:
        for line_number, line in enumerate(f, start=1):
            json_object = json.loads(line)
            try:
                payload = json_object["tcp"]['tcp.payload']
                res = hex_to_ascii(payload)
                fout.write(str(line_number) + ' ' + res)
                fout.write('\n')
            except KeyError:
                continue
            except UnicodeDecodeError:
                continue
