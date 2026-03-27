from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/hello')
def hello():
    return {"message": "Hello, DevOps!"}

@app.route('/time')
def time():
    return {"time": str(datetime.now())}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)