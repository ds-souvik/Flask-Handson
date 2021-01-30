'''Copied the same code as it was there in 2 static, templates folder and first HTML.py to edit further
'''

from flask import Flask, render_template
app = Flask(__name__)    #Whenever we make a website using Flask, it's an app. Making an instance of Flask class present in flask.

@app.route('/')
def home():
    return render_template('index.html') #Until here Hello World will be printed on local host/

@app.route('/index')
def home2():
    return render_template('index.html') #Until here Hello World will be printed on local host/

#To go beyond localhost and slash(/)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post')
def samplepost():
    return render_template('post.html')

@app.route('/contact')
def contact():
    return  render_template('contact.html')

#If you the above program run now, the program will execute but there will be no link to browse.
#For that we need to write app.run()

#app.run()
app.run(debug=True)      #Using debug=True automatically changes in the client if the code is changed here. Only the page needs to
                         #be refreshed.