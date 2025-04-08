from flask import Flask, request
from datetime import datetime
import csv, os

app = Flask(__name__)


TMP_DIR = "tmp"
OPEN_LOG_FILE = os.path.join(TMP_DIR, "open_log.csv")

#Ensuring the file exists
os.makedirs(TMP_DIR, exist_ok=True)

#Route for tracking email opens
@app.route("/clicklog/<lead_id>")
def click_log(lead_id):
    try:
        with open(OPEN_LOG_FILE , "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([lead_id, datetime.now(), request.remote_addr])
        print(f" Logged click for {lead_id} from {request.remote_addr}")
    except Exception as e:
        print(f" Error logging click: {e}")

  
    return "<h2>Thanks for clicking! We’ve logged your interest. </h2>"


if __name__ == "__main__":
    print(" Flask tracking server is running on http://127.0.0.1:5000")
    app.run()
