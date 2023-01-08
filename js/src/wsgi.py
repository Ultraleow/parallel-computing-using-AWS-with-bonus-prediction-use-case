from flask import Flask
import sys
from api_function import app_func
sys.getswitchinterval()

print(sys.version)
app = Flask(__name__)
app.register_blueprint(app_func)


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@app.route('/health_check_1')
def hello_world():  # put application's code here
    return 'Hello World!'
   
if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
