import os

ipList = ['11','12','17','25','26','28']

for ip in ipList:
    curPath = os.getcwd()
    storeFile = ip + '_lite.json'
    storePath = os.path.join(curPath, storeFile)
    with open(storeFile, 'r') as fr:
        with open(ip+'_lite2.json', 'w') as fw:
            for line_cnt, line in enumerate(fr, start=1):
                if "HTTP/1.1 404 Not Found" in line:
                    continue
                fw.write(line)
