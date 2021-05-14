import socket
import argparse
from encryption import encrypt_msg

def run_server(port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(('', port))
        sock.listen(2)
        s, addr = sock.accept()
        with s:
            rec = s.recv(1024)
            aes_key = bytes.fromhex("0f1571c947d9e8590cb7add6af7f6798")
            print("Received a message")
            
              
def run_client(ip, port, msg):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        aes_key = bytes.fromhex("0f1571c947d9e8590cb7add6af7f6798")
        sock.send(encrypt_msg(msg, aes_key))#b'hardcoded_key123'))
        print(str(encrypt_msg(msg, aes_key)))##b'hardcoded_key123')))
        print('Message Sent')
    
        
        
if __name__ =='__main__':
    msg = bytes.fromhex("9090909090909090909090909090")
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', help='listen for connections', action='store_true', dest='listen')
    args = parser.parse_args()
    
    if args.listen:
        run_server(8000)
    else:
        run_client('127.0.0.1', 8000, msg)

