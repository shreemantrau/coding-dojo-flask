from flask import Flask, render_template,redirect, request, flash, session
from mysqlconnection import connectToMySQL

app=Flask(__name__)
app.secret_key="something"
@app.route('/')
def index():
    mysql=connectToMySQL('mydb')
    query=("SELECT * FROM coding_dojo;")
    output=mysql.query_db(query)
    print(output)
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    flag=True
    data={ 
    'name':request.form['name'],
    'language': request.form['language'],
    'location':request.form['location'],
    'comment':request.form['comment']
    }
    
    if len(request.form['name']) <1:
        
        flag=False
        flash("Please enter name!")
        
    
    if flag:
        
        query=("INSERT INTO coding_dojo (name,dojo_location,favorite_laguage,comment) VALUES(%(name)s,%(location)s,%(language)s,%(comment)s);")
        mysql=connectToMySQL('mydb')
        mysql.query_db(query,data)
        return render_template('result.html',data=data)
    return redirect('/')

app.run(debug=True)
