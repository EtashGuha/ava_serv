from flask import Flask
app = Flask(__name__)

meetings = {}

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/create_meeting_id', methods=['POST'])
def create_meeting_id():
	print(request.form)

if __name__ == '__main__':
    app.run()