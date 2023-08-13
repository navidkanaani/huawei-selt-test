import logging
from flask import Flask, request
from markupsafe import escape

from selt_test import SeltTest

app = Flask(__name__)

@app.route("/huawei-dslam-5300/selt-test/<string:host_address>")
def huawei_5300_selt_test(host_address: str) -> str:
    interface_address = request.args.get("interface")
    app.logger.critical(f"Starting test selt on host: {host_address}, interface: {interface_address}")
    selt_test_result = SeltTest.huawei_5300_selt_test(host=escape(host_address), 
                                                     interface_address=escape(interface_address))

    return f"{selt_test_result}"

@app.route("/huawei-dslam-5600/selt-test/<string:host_address>")
def huawei_5600_selt_test(host_address: str) -> str:
    interface_address = request.args.get("interface")
    port = request.args.get("port")
    app.logger.critical(f"Starting test selt on host: {host_address}, interface: {interface_address}, port: {port}")
    selt_test_result = SeltTest.huawei_5600_selt_test(host=escape(host_address),
                                                      interface_address=escape(interface_address),
                                                      port=escape(port))
    return f"{selt_test_result}"

if __name__ == "__main__":
    app.run(debug=True)