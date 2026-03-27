from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/hello')
def hello():
    return {"message": "Hello, DevOps!"}

@app.route('/time')
def time():
    return {"time": str(datetime.now())}

@app.route('/health')
def health():
    return {"status": "healthy"}

@app.route('/version')
def version():   
    return {"version": "1.0.0"}  

@app.route('/metrics')
def metrics():
    return {"metrics": {"requests": 100, "errors": 5}}

@app.route('/date')
def date():
    return {"date": str(datetime.now().date())}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)