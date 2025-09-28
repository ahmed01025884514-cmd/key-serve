from flask import Flask, request, jsonify

app = Flask(__name__)

# قائمة الأكواد المسموح بيها
valid_keys = {
    "ahmed123": {"uses": 0, "max_uses": 3},
    "test999": {"uses": 0, "max_uses": 1}
}

@app.route("/check", methods=["POST"])
def check_key():
    data = request.get_json()
    key = data.get("key")

    if key not in valid_keys:
        return jsonify({"valid": False, "reason": "not_found"})

    info = valid_keys[key]
    if info["uses"] >= info["max_uses"]:
        return jsonify({"valid": False, "reason": "exhausted"})

    # لو لسه ينفع
    info["uses"] += 1
    return jsonify({"valid": True, "remaining": info["max_uses"] - info["uses"]})

@app.route("/")
def home():
    return "Server is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
