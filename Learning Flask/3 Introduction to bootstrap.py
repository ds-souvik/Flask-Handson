'''Copied the same code as it was there in 2 static, templates folder and first HTML.py to edit further
'''

from flask import Flask, render_template
app = Flask(__name__)    #Whenever we make a website using Flask, it's an app. Making an instance of Flask class present in flask.

@app.route('/')
def hello():
    return render_template('index.html') #Until here Hello World will be printed on local host/

#To go beyond localhost and slash(/)

@app.route('/bootstrap')
def bootstrap():
    return render_template('bootstrap.html')

@app.route('/Souvik')
def Souvik():
    return 'Hello Souvik. How are you doing today?'    #Doesn't contain render template.

@app.route('/about')
def me():
    return  render_template('about.html')              #Has a heading in html.

@app.route('/about1')
def me1():
    name='Souvik Ganguly'
    return render_template('about1.html', var_for_html=name)  #declared a variable here to be used in html file

#If you the above program run now, the program will execute but there will be no link to browse.
#For that we need to write app.run()

#app.run()
app.run(debug=True)      #Using debug=True automatically changes in the client if the code is changed here. Only the page needs to
                         #be refreshed.