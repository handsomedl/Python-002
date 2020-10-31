import sys
import subprocess
from concurrent.futures import ThreadPoolExecutor

### 此扫描工具仅能运行在linux上 ###

usage="""please input correct argument !
example：
netscan.py -n 4 -f ping -ip 192.168.0.1-192.168.0.100
netscan.py -n 10 -f tcp -ip 192.168.0.1 -w result.json
# -n：指定并发数量。
# -f ping：进行 ping 测试
# -f tcp：进行 tcp 端口开放、关闭测试。
# -ip：目标地址。连续 IP 地址支持 192.168.0.1-192.168.0.100 写法。
# -w：扫描结果进行保存
"""

cmd_arg_list=sys.argv[1:]

if "-f" in cmd_arg_list:
    mode=cmd_arg_list[cmd_arg_list.index("-f")+1]
if "-ip" in cmd_arg_list:
    arg_ip_value=cmd_arg_list[cmd_arg_list.index("-ip")+1]
    if arg_ip_value.count("-") == 1:
        start_ip,end_ip = arg_ip_value.split("-")
        net_area=str(start_ip.split(".")[0]+"."+start_ip.split(".")[1]+"."+start_ip.split(".")[2])
        start_host=int(start_ip.split(".")[-1])
        end_host=int(end_ip.split(".")[-1])
if "-ip" in cmd_arg_list and mode == "tcp":
    arg_ip_value=cmd_arg_list[cmd_arg_list.index("-ip")+1]
if "-n" in cmd_arg_list:
    worker_num=int(cmd_arg_list[cmd_arg_list.index("-n")+1])
if "-w" in cmd_arg_list:
    filename=cmd_arg_list[cmd_arg_list.index("-w")+1]


def pingscan(host):
    rc = subprocess.call(
        'ping -c2 -w2 %s &> /dev/null' % host,
        shell=True
    )            
    if rc:
        pass
    else:
        print('%s: up' % host)       


def tcpscan(ip,port):
    rc = subprocess.call(
        'nc -zvw2 %s %s &> /dev/null' %(ip,port),
        shell=True
    )            
    if rc:
        pass
    else:
        result=("%s port %s is on\n" %(ip,port))
        output.write(result)


if __name__ == "__main__":

    if mode == "ping":
        ips = [net_area+"."+"%d" % i for i in range(start_host, end_host+1)] 
        with ThreadPoolExecutor(worker_num) as executor:
            for ip in ips:
                executor.submit(pingscan, ip)            
    elif mode == "tcp":
        output = open(filename,'a',encoding='utf-8')
        with ThreadPoolExecutor(worker_num) as executor2:
            for port in range(1,1025):
                executor2.submit(tcpscan, arg_ip_value,port) 
        output.close()
    else:
        print(usage)
    
