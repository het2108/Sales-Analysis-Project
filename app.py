# tracking_server.py
from flask import Flask, send_file, request, redirect
from datetime import datetime
import csv, os

app = Flask(__name__)

OPEN_LOG_FILE = "/tmp/open_log.csv"

@app.route("/openlog/<lead_id>")
def open_log(lead_id):
    with open(OPEN_LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([lead_id, datetime.now(), request.remote_addr])
    return send_file("static/1x1.png", mimetype="image/png")

# @app.route("/clicklog/<lead_id>")
# def click_log(lead_id):
#     redirect_url = request.args.get("redirect", "")
#     with open(CLICK_LOG_FILE, "a", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow([lead_id, datetime.now(), request.remote_addr, redirect_url])
#     return redirect(redirect_url)

if __name__ == "__main__":
    os.makedirs("static", exist_ok=True)
    with open("static/1x1.png", "wb") as f:
        f.write(b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\nIDATx\xdac``\x00\x00\x00\x02\x00\x01\xe2!\xbc\x33\x00\x00\x00\x00IEND\xaeB`\x82')
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
