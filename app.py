from flask import Flask
from markupsafe import escape


app = Flask(__name__)

@app.route("/huawei-dslam-5300/<address>")
def huawei_5300_selt_test(address: str) -> str:
    return f"{escape(address)}"

@app.route("/huawei-dslam-5600/<address>")
def huawei_5600_selt_test(address: str) -> str:
    return f"{escape(address)}"