from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    print('Welcome to the api.')


@app.route('/webhook-testing', methods = ['POST'])
def testing():
    print("Wehbook successfull")




if __name__ == '__main__':
    app.run(debug=True)