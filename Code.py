from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def Mainpage():
    return render_template('Mainpage.html')

def Catalogue():
    return render_template('catalogue.html')


if __name__ == '__main__':
    app.run()
    
