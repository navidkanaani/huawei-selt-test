from telnetlib import Telnet
import getpass


HOST = "192.168.40.83"
user = "Fanavasd"
password = "SD@82185"

tn = Telnet(HOST)
print(tn.read_until(b"Username:").decode("ascii"))
tn.write(user.encode("ascii") + b"\r\n")
if password:
    print(tn.read_until(b"Password:").decode("ascii"))
    tn.write(password.encode("ascii") + b"\r\n\r\n")

print(tn.read_until(b"esf-esf-estghl1>").decode("ascii"))
tn.write("enable".encode("ascii") + b"\r\n")

print(tn.read_until(b"esf-esf-estghl1>").decode("ascii"))
tn.write("configure terminal".encode("ascii") + b"\r\n")

print(tn.read_until(b"esf-esf-estghl1(config)#").decode("ascii"))
tn.write("adsl deactivate adsl 2/0/47".encode("ascii") + b"\r\n\r\n")

print(tn.read_until(b"esf-esf-estghl1(config)#").decode("ascii"))
tn.write("interface adsl 2/0/47".encode("ascii") + b"\r\n\r\n")

print(tn.read_until(b"esf-esf-estghl1(config-if-Adsl2/0/47)#").decode("ascii"))
tn.write("adsl test selt".encode("ascii") + b"\r\n\r\n")

print(tn.read_until(b"esf-esf-estghl1(config-if-Adsl2/0/47)#").decode("ascii"))
tn.write("exit".encode("ascii") + b"\r\n\r\n")

print(tn.read_until(b"esf-esf-estghl1(config)#").decode("ascii"))
tn.write("show adsl test selt adsl 2/0/47".encode("ascii") + b"\r\n\r\n")

# print(tn.read_until(b"esf-esf-estghl1(config)#", timeout=20).decode("ascii"))



# tn.write(b"\n")
# tn.write(b"enable")
# print(tn.read_all().decode("ascii"))

cmd = b"""

Enable

Config terminal

Adsl deactivate adsl 2/0/47

 

 

Interface ads 2/0/47

Adsl test selt

Exit

 

show adsl test selt adsl 2/0/47 
"""

# tn.write(cmd)

print(tn.read_all().decode("ascii"))