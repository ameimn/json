from flask import Flask, request, jsonify
import json
from flask_cors import CORS  # CORS 추가

app = Flask(__name__)
CORS(app)  # 모든 origin 허용

# JSON 파일 불러오기
with open("csvjson.json", "r", encoding="utf-8") as f:
    od_data = json.load(f)

@app.route("/query")
def query():
    origin = request.args.get("origin", "").strip()
    dest = request.args.get("dest", "").strip()

    for record in od_data:
        if record.get("행정동O", "").strip() == origin and record.get("행정동D", "").strip() == dest:
            return jsonify({
                "time_pt": record.get("time_pt", "N/A"),
                "price_pt": record.get("price_pt", "N/A"),
                "time_car": record.get("time_car", "N/A"),
                "price_car": record.get("price_car", "N/A"),
                "walk_time": record.get("walk_time", "정보 없음"),
                "naver_p": record.get("naver_p", ""),
                "naver_c": record.get("naver_c", "")
            })

    return jsonify({"error": "No match found"}), 404

@app.route("/")
def home():
    return "🚦 Seoul OD API is working!"
