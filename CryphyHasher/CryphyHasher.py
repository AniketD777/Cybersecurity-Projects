#!/bin/python3

import pyfiglet
from termcolor import colored
import hashlib

def main():
    banner=pyfiglet.figlet_format("Cryphy-Hasher")
    print(colored(banner,"cyan"))
    print(colored("Hash-Scheme: MD5->1    SHA1->2    SHA224->3    SHA256->4    SHA3_224->5    SHA3_256->6    SHA512->7",'red'))
    try:
        hashmode=int(input("[+] Select Hash-Scheme: "))
        if hashmode not in range(1,8):
            raise ValueError()
        string=input("[+] Enter String to Hash: ")
        while(string==""):
            string=input("[-] No String provided. Please Enter String: ")
        schemes=[hashlib.md5,hashlib.sha1,hashlib.sha224,hashlib.sha256,hashlib.sha3_224,hashlib.sha3_256,hashlib.sha512]
        hash_obj=schemes[hashmode-1]()
        hash_obj.update(string.encode('utf-8'))
        print("[+] Hash: "+hash_obj.hexdigest())
    except ValueError:
        print("[-] Invalid scheme: Please select available schemes between 1 to 7.")

if __name__=="__main__":
    main()
