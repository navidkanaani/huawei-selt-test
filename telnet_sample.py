from telnetlib import Telnet
import time
import re
import getpass


HOST = "192.168.40.83"
user = "Fanavasd"
password = "SD@82185"


with Telnet(HOST) as tn:
    tn.write(user.encode("ascii") + b"\r\n")
    tn.write(password.encode("ascii") + b"\r\n")
    tn.write("enable".encode("ascii") + b"\r\n")
    tn.write("configure terminal".encode("ascii") + b"\r\n")
    tn.write("adsl deactivate adsl 2/0/47".encode("ascii") + b"\r\n\r\n")
    tn.write("interface adsl 2/0/47".encode("ascii") + b"\r\n\r\n")
    tn.write("adsl test selt".encode("ascii") + b"\r\n\r\n")
    tn.write("exit".encode("ascii") + b"\r\n\r\n")
    time.sleep(60)
    tn.write("show adsl test selt adsl 2/0/47".encode("ascii") + b"\r\n\r\n")
    time.sleep(10)
    result = tn.read_very_eager().decode("ascii")
    # print(result)
    time.sleep(20)
    tn.write("adsl activate adsl 2/0/47".encode("ascii") + b"\r\n")


def retrieve_line_length(selt_result):
    line_length_pattern = r"line length.*feet"
    line_length_meters_value_pattern = r"\d.+ m"
    line_length = re.findall(line_length_pattern, selt_result)
    line_length_meters = re.findall(line_length_meters_value_pattern, line_length[0])
    return line_length_meters[0]

print(retrieve_line_length(result))


# tn = Telnet(HOST)
# print(tn.read_until(b"Username:").decode("ascii"))
# tn.write(user.encode("ascii") + b"\r\n")
# if password:
#     print(tn.read_until(b"Password:").decode("ascii"))
#     tn.write(password.encode("ascii") + b"\r\n\r\n")

# print(tn.read_until(b"esf-esf-estghl1>").decode("ascii"))
# tn.write("enable".encode("ascii") + b"\r\n")

# print(tn.read_until(b"esf-esf-estghl1>").decode("ascii"))
# tn.write("configure terminal".encode("ascii") + b"\r\n")

# print(tn.read_until(b"esf-esf-estghl1(config)#").decode("ascii"))
# tn.write("adsl deactivate adsl 2/0/47".encode("ascii") + b"\r\n\r\n")

# print(tn.read_until(b"esf-esf-estghl1(config)#").decode("ascii"))
# tn.write("interface adsl 2/0/47".encode("ascii") + b"\r\n\r\n")

# print(tn.read_until(b"esf-esf-estghl1(config-if-Adsl2/0/47)#").decode("ascii"))
# tn.write("adsl test selt".encode("ascii") + b"\r\n\r\n")

# print(tn.read_until(b"esf-esf-estghl1(config-if-Adsl2/0/47)#").decode("ascii"))
# tn.write("exit".encode("ascii") + b"\r\n\r\n")

# print(tn.read_until(b"esf-esf-estghl1(config)#").decode("ascii"))
# print("sleep thread!")
# time.sleep(60)
# print("wake up thread!")
# tn.write("show adsl test selt adsl 2/0/47".encode("ascii") + b"\r\n\r\n")
# print(tn.read_until(b"esf-esf-estghl1(config)#").decode("ascii"))

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

# print(tn.read_all().decode("ascii"))