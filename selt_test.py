from telnetlib import Telnet
import time
import logging

from utils import Utils
from runtime_config import RuntimeConfig

logger = logging.getLogger("app")

class SeltTest:
    @staticmethod
    def huawei_5300_selt_test(host: str, interface_address: str):
        logger.info("Huawei 5300 selt test is starting...")
        with Telnet(host) as tn_socket:
            logger.info("Connect to interface...")
            tn_socket.write(RuntimeConfig.USERNAME.encode("ascii") + b"\r\n")
            tn_socket.write(RuntimeConfig.PASSWORD.encode("ascii") + b"\r\n")
            logger.info("Login user.")
            tn_socket.write("enable".encode("ascii") + b"\r\n")
            tn_socket.write("configure terminal".encode("ascii") + b"\r\n")
            logger.critical("Deactivating interface.")
            tn_socket.write(f"adsl deactivate adsl {interface_address}".encode("ascii") + b"\r\n\r\n")
            tn_socket.write(f"interface adsl {interface_address}".encode("ascii") + b"\r\n\r\n")
            logger.info("Testing interface.")
            tn_socket.write("adsl test selt".encode("ascii") + b"\r\n\r\n")
            tn_socket.write("exit".encode("ascii") + b"\r\n\r\n")
            time.sleep(60)
            logger.info("Fetching test result...")
            tn_socket.write(f"show adsl test selt adsl {interface_address}".encode("ascii") + b"\r\n\r\n")
            time.sleep(10)
            try:
                result = tn_socket.read_very_eager().decode("ascii")
                logger.critical(result)
            except BrokenPipeError as error:
                logger.error("Test failed, trying again :(")
                tn_socket.close()
                SeltTest.huawei_5300_selt_test(host=host, interface_address=interface_address)
            time.sleep(20)
            logger.critical("Activating interface.")
            tn_socket.write(f"adsl activate adsl {interface_address}".encode("ascii") + b"\r\n")
        return Utils.retrieve_line_length(result)
    
    @staticmethod
    def huawei_5600_selt_test(host: str, interface_address: str, port: str) -> str:
        line_length = ""
        logger.critical("Huawei 5600 selt test is starting...") 
        with Telnet(host) as tn_socket:
            time.sleep(0.5)
            tn_socket.write(RuntimeConfig.USERNAME.encode("ascii") + b"\r\n")
            time.sleep(0.5)
            tn_socket.write(RuntimeConfig.PASSWORD.encode("ascii") + b"\r\n")
            logger.info("Login user.")
            time.sleep(1)
            tn_socket.write("enable".encode("ascii") + b"\r\n")
            time.sleep(1)
            tn_socket.write("config".encode("ascii") + b"\r\n")
            time.sleep(1)
            tn_socket.write(f"interface adsl {interface_address}".encode("ascii") + b"\r\n")
            time.sleep(1)
            tn_socket.write(f"deactivate {port}".encode("ascii") + b"\r\n")
            time.sleep(1)
            deactivate_result = tn_socket.read_very_eager().decode("ascii")
            deactivated = Utils.huawei_5600_deactivate_confirmation(deactivate_result)
            if deactivated:
                try:
                    tn_socket.write(f"adsl selt {port}".encode("ascii") + b"\r\n\r\n")
                    tn_socket.read_until("SELT finish successfully".encode("ascii"))
                    time.sleep(1)
                    result = tn_socket.read_very_eager().decode("ascii")
                    logger.critical(result)
                    line_length = Utils.huawei_5600_retrieve_line_length(result)
                except Exception as error:
                    logger.critical(f"Test failed, try again :(, {error}")
                    tn_socket.close()
                    SeltTest.huawei_5600_selt_test(host=host, interface_address=interface_address, port=port)
            else:
                logger.error("There is some problem to deactivating the port, please check port status.")
        return line_length
