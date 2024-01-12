import pyfiglet
from termcolor import colored
from modes import client,server 

def main():
    try:
        banner=pyfiglet.figlet_format("RemShell")
        print(colored(banner,'cyan'))
        print(colored("[*] Modes:   Take-Access => 0    Grant-Access => 1",'red'))
        Mode=int(input("[+] Enter Mode: "))
        if Mode not in (0,1):
            raise ValueError
        if Mode==0:
            host=input("[+] Enter Address to listen to: ")
            port=int(input("[+] Enter port to listen to: "))
            server.start(host,port)
        else:
            host=input("[+] Enter host address to connect to: ")
            port=int(input("[+] Enter port to connect to: "))
            client.start(host,port)     
    except ValueError:
        print("[-] Invalid Mode! Select Mode 0 or 1.")

if __name__=='__main__':
    main()
