#pip install selenium
#pip install chromedriver-binary
#pip install flask
#pip install -U flask-cors

from flask import Flask, render_template, redirect, url_for,request
from flask import make_response,jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.Chrome()
# driver.get("http://www.python.org")

class TwitterBot:
    def __init__(self,username, password):
        self.username=username
        self.password=password
        self.bot=webdriver.Chrome("../chromedriver_win32/chromedriver.exe")

    def login(self):
        bot=self.bot
        bot.get('https://twitter.com/login')
        time.sleep(3)
        email=bot.find_element_by_name('session[username_or_email]')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)

@app.route('/api/getsample', methods=['POST'])
@cross_origin()
def getsample():
    data = {'name': 'nabin khadka'}
    dataIn= request.json
    
    print((dataIn))
    
    # message = None
    if request.method == 'POST':
        ed=TwitterBot(dataIn['username'],dataIn['password'])
        res=ed.login()
    return dataIn['username']
    # return jsonify(data)

@app.route('/api/login', methods=['POST'])
def testfunction():
    
    dataIn= request.get_json()
    print(dataIn)
    
    message = None
    if request.method == 'POST':
        ed=TwitterBot(dataIn['username'],dataIn['password'])
        res=ed.login()
    return 'Ok'

if __name__ == "__main__":
    app.run(debug = True)
