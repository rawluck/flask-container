import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Containerized Hello, World! with CI/CD using Travis CI by Lakshya Rawat, <a href=https://github.com/rawluck/flask-container>Github Repo</a> '

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))