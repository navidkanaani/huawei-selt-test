from telnetlib import Telnet
import time
import logging

from utils import Utils
from runtime_config import RuntimeConfig

logger = logging.getLogger("app")

class SeltTest:
    @staticmethod
    def huawei_5300_selt_test(host, interface_address):
        line_length = ""
        logger.critical("Huawei 5300 selt test is starting...")
        with Telnet(host) as tn_socket:
            logger.critical("Connecting to port...")
            time.sleep(0.5)
            tn_socket.write(RuntimeConfig.USERNAME.encode("ascii") + b"\r\n")
            time.sleep(0.5)
            tn_socket.write(RuntimeConfig.PASSWORD.encode("ascii") + b"\r\n")
            time.sleep(1)
            login_result = tn_socket.read_very_eager().decode("ascii")
            Utils.huawei_5300_login_check(tn_socket, login_result)
            logger.critical("Login user.")
            tn_socket.write("enable".encode("ascii") + b"\r\n")
            tn_socket.write("configure terminal".encode("ascii") + b"\r\n")
            logger.critical("Deactivating port.")
            tn_socket.write("adsl deactivate adsl ".encode("ascii") + interface_address.encode("ascii") + b"\r\n\r\n")
            tn_socket.write("interface adsl ".encode("ascii") + interface_address.encode("ascii") + b"\r\n\r\n")
            logger.info("Testing port.")
            tn_socket.write("adsl test selt".encode("ascii") + b"\r\n\r\n")
            tn_socket.write("exit".encode("ascii") + b"\r\n\r\n")
            time.sleep(60)
            tn_socket.write("show adsl test selt adsl ".encode("ascii") + interface_address.encode("ascii") + b"\r\n\r\n")
            time.sleep(15)
            try:
                logger.info("Fetching test result...")
                result = tn_socket.read_very_eager().decode("ascii")
                logger.info(result)
                line_length = Utils.huawei_5300_retrieve_line_length(result)
            except Exception as error:
                logger.error(error)
                tn_socket.close()
                SeltTest.huawei_5300_selt_test(host=host, interface_address=interface_address)
            time.sleep(20)
            logger.critical("Activating port.")
            tn_socket.write("adsl activate adsl ".encode("ascii") + interface_address.encode("ascii") + b"\r\n")
            tn_socket.close()
        return line_length
    
    @staticmethod
    def huawei_5600_selt_test(host: str, interface_address: str, port: str) -> str:
        line_length = ""
        logger.critical("Huawei 5600 selt test is starting...") 
        with Telnet(host) as tn_socket:
            logger.critical("Connecting to port...")
            time.sleep(0.5)
            tn_socket.write(RuntimeConfig.USERNAME.encode("ascii") + b"\r\n")
            time.sleep(0.5)
            tn_socket.write(RuntimeConfig.PASSWORD.encode("ascii") + b"\r\n")
            logger.info("Login user.")
            time.sleep(1)
            login_result = tn_socket.read_very_eager().decode("ascii")
            Utils.huawei_5600_login_check(tn_socket, login_result)
            tn_socket.write("enable".encode("ascii") + b"\r\n")
            time.sleep(1)
            tn_socket.write("config".encode("ascii") + b"\r\n")
            time.sleep(1)
            tn_socket.write(f"interface adsl {interface_address}".encode("ascii") + b"\r\n")
            time.sleep(1)
            logger.critical("Deactivating port...")
            tn_socket.write(f"deactivate {port}".encode("ascii") + b"\r\n")
            time.sleep(1)
            try:
                logger.critical("Starting SELT test...")
                tn_socket.write(f"adsl selt {port}".encode("ascii") + b"\r\n\r\n")
                tn_socket.read_until("SELT finish successfully".encode("ascii"))
                time.sleep(1)
                result = tn_socket.read_very_eager().decode("ascii")
                logger.info(result)
                logger.info("Fetching result...")
                line_length = Utils.huawei_5600_retrieve_line_length(result)
                logger.critical("Activating port...")
                tn_socket.write(f"activate {port}".encode("ascii") + b"\r\n")
                tn_socket.close()
            except Exception as error:
                logger.critical(f"Test failed, try again :(" + error)
                tn_socket.close()
                SeltTest.huawei_5600_selt_test(host=host, interface_address=interface_address, port=port)
        return line_length
