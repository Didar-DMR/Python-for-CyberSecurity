import socket
import time
import ipaddress
import sys

ip_add = input("IP Address: ")

def ip_valid():
    try:
        ip = ipaddress.IPv4Address(ip_add)
    except ValueError:
        print("Invalid IPv4 Address !!!")
        sys.exit()

ip_valid()

all_ports = input("Do you want to Scann all Ports? (Y/n): ")

if all_ports == "Y" or all_ports == "y":
    begin_port = 0
    finish_port = 65536

elif all_ports == "N" or all_ports == "n":
    print("Define Port Range...")
    begin_port = int(input("Start Port: "))
    finish_port = int(input("Finish Port: "))
    if finish_port > 65536 :
        print("Invalid Finish Port!!")
        sys.exit()
else:
    print("Please Try Again !")
    sys.exit()

print("\n","*" * 50,"\n")
print("\t","Scanning Ports From {} to {}".format(begin_port,finish_port),"\t")
print("\n","*" * 50,"\n")
time.sleep(3)

def scanning():

    for port in range(begin_port,finish_port + 1):

        try:
            new_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            new_socket.bind((ip_add, port))
            new_socket.settimeout(1)
        except:
            print("{} Port OPEN".format(port))

    new_socket.close()

scanning()