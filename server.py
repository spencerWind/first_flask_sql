from flask import Flask, render_template, request, redirect
from friend import Friend

app = Flask(__name__)

@app.route('/')
def home():
    friends = Friend.get_all()
    print(friends)
    return render_template('home.html', all_friends = friends)

@app.route('/create',)
def create_friend():
    return render_template('create_friend.html')

@app.route('/submit_data', methods = ['POST'])
def submit_data():
    Friend.save(request.form)
    return redirect('/')
    

if __name__ == '__main__':
    app.run(debug=True, port=5001)