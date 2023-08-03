from flask import Flask, request
from markupsafe import escape

from selt_test import SeltTest


app = Flask(__name__)

@app.route("/huawei-dslam-5300/<host_address>")
def huawei_5300_selt_test(host_address: str) -> str:
    interface_address = request.args.get("interface")
    selt_test_result = SeltTest.huawei_5300_selt_test(host=escape(host_address), 
                                                      interface_address=escape(interface_address))
    
    return f"{selt_test_result}"

@app.route("/huawei-dslam-5600/<address>")
def huawei_5600_selt_test(address: str) -> str:
    return f"{escape(address)}"