import socket, sys, argparse, time
    
def cliente(h,p):
    if h == 'localhost':
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print("Socket creation failed")
            sys.exit()
    if h == '::1':
        try:
            s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        except socket.error:
            print("Socket creation failed")
            sys.exit()
        

    host = h
    port = p
    print("Connecting.....")
    time.sleep(2)
    s.connect((host,port))
    print("Handshake terminado")
    time.sleep(1)
    print("Esperando datos del server")
    while True:    
        msg = input("Ingresar comando a realizar:")
        s.send(msg.encode())
        print("Esperando datos del server")
        msg = s.recv(1024)
        print(msg.decode())
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-ht","--host",required=True,help="Dirección IP o nombre del servidor")
    parser.add_argument("-p","--port", type=int,required=True,help="Nª de puerto del servidor")
    args = parser.parse_args()
    print(args.host,args.port)
    cliente(args.host,args.port)