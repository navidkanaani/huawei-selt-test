from telnetlib import Telnet
import time

from utils import Utils
from runtime_config import RuntimeConfig


class SeltTest:
    def __init__(self, username, password):
        self.username = RuntimeConfig.USERNAME
        self.password = RuntimeConfig.PASSWORD 

    def huawei_5300_selt_test(self, host: str, interface_address: str):
        with Telnet(host) as tn_socket:
            tn_socket.write(self.username.encode("ascii") + b"\r\n")
            tn_socket.write(self.password.encode("ascii") + b"\r\n")
            tn_socket.write("enable".encode("ascii") + b"\r\n")
            tn_socket.write("configure terminal".encode("ascii") + b"\r\n")
            tn_socket.write(f"adsl deactivate adsl {interface_address}".encode("ascii") + b"\r\n\r\n")
            tn_socket.write(f"interface adsl {interface_address}".encode("ascii") + b"\r\n\r\n")
            tn_socket.write("adsl test selt".encode("ascii") + b"\r\n\r\n")
            tn_socket.write("exit".encode("ascii") + b"\r\n\r\n")
            time.sleep(60)
            tn_socket.write(f"show adsl test selt adsl {interface_address}".encode("ascii") + b"\r\n\r\n")
            time.sleep(20)
            try:
                result = tn_socket.read_very_eager().decode("ascii")
            except Exception as error:
                raise(error)
            time.sleep(20)
            tn_socket.write(f"adsl activate adsl {interface_address}".encode("ascii") + b"\r\n")

        return Utils.retrieve_line_length(result)