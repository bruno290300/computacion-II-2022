import signal,os,argparse, asyncio
import socketserver,subprocess,socket,threading


def handle(self):
    while True:
        self.data = self.request.recv(1024).strip()
        print(self.data)
        pp = subprocess.Popen([self.data], stdout = subprocess.PIPE,stderr = subprocess.PIPE, shell = True)
        out,err = pp.communicate()
        if err:
            self.request.sendall(b"ERROR \n"+err)
            print(err)
        else:
            self.request.sendall(b"OK\n"+out)
            print(out)
            
        print("PID: %d" % os.getpid())

async def main(PORT):
    server = await asyncio.start_server(
        handle, 'localhost', PORT)
    
    async with server:
        await server.serve_forever()

        

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p","--port", type=int,required=True,help="Nª de puerto del servidor")
    args = parser.parse_args()
    HOST, PORT = "localhost", args.port
    print("Server iniciado en: ",HOST,PORT)
    asyncio.run(main(PORT))