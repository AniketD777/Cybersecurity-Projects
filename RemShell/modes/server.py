import socket
import os

def get(connection,cmd):
    connection.sendall(cmd)
    bits=connection.recv(1024)
    if b'Unable to find out the file' not in bits:
        filpath=(cmd.split(b' ')[1]).decode('utf-8')
        with open(f'{filpath}','wb') as file:
            while True:                
                if bits.endswith(b'DONE'):
                    print('[*] Successfully Downloaded.')
                    break
                file.write(bits)
                bits=connection.recv(1024)                
    else:
        print('[-] Unable to find out the file.')

def put(connection,cmd):
    if os.path.exists((cmd.split(b' ')[1].decode('utf-8'))):
        with open(cmd.split(b' ')[1].decode('utf-8'),'rb') as file:
            connection.sendall(cmd)
            packet=file.read(1024)
            while packet!=b'':
                connection.sendall(packet)
                packet=file.read(1024)
            connection.sendall(b"DONE")
            print("[*] Successfully Uploaded.")
            file.close()
    else:
        print("[-] No such file exists.")

def start(host,port):
    try:
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sock:     
            sock.bind((host,port))
            sock.listen(1)
            print(f'[*] Waiting for Connection...')
            connection,addr=sock.accept()
            print(f'[*] Connection Received from {addr}.')
            with connection:
                while True:
                    cmd=input("[+] Command: ").encode('utf-8')
                    filpath='test'
                    if b'exit' in cmd:
                        print("[*] Exiting...")
                        connection.sendall(b'exit')
                        break
                    elif b'get' in cmd:
                        get(connection,cmd)
                    elif b'put' in cmd:
                        put(connection,cmd)
                    else:
                        connection.sendall(cmd)
                        print(connection.recv(10240).decode('utf-8'))
    except (OSError,OverflowError) as e:
        print(f"[-] Error: {e}")

