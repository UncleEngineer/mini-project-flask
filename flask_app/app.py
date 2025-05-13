from flask import Flask, render_template

app = Flask(__name__)

# localhost:8000
# 210.155.77.100
# www.loongshop.com

@app.route('/')
def home():
    name = 'Uncle Engineer'
    context = {'nm':name}
    friend = ['somchai','somsak','somsri']

    return render_template('index.html',context=context, friend=friend)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)