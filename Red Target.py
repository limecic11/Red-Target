import socket
try:
    url=input("Enter The Domain => ")
    host=socket.gethostname()
    ip_add=socket.gethostbyname(host)
    url_ip= socket.gethostbyname(url)
    print("="*20)
    print(f"HOST: {host}")
    print(f"Your IP : {ip_add}")
    print("="*20)
    print (f"Server : {url}")
    print(f"Server IP : {url_ip}")
except:
    print("Check Your Internet Connection")