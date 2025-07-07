from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "LINE Bot is running on Render!"

@app.route('/callback', methods=['POST'])
def callback():
    print("✅ LINEからリクエストを受信しました")
    return "OK",200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
