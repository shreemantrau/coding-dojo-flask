from flask import Flask, render_template,request, redirect,session, flash
from mysqlconnection import connectToMySQL
import re

app=Flask(__name__)
app.secret_key="Its a secret!!!!"
EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
@app.route('/', methods=["POST", 'GET'])
def index():
    return render_template('index.html')


@app.route('/create', methods=['POST', 'GET'])
def create():
    email=request.form['email'] 
    query="INSERT INTO email (email_id) VALUES('{}');".format(email)
    
    query2="SELECT email_id FROM email where email_id= '{}';".format(request.form['email'])
    print ("*"*50)

    
    mysql=connectToMySQL('mydb')
    all_emails=mysql.query_db(query2)
    # print("Printing new var ------------------------------------------------------------------------",new_var)
    print("-----*"*50)
    print(all_emails)
    print("-----*"*50)
   ##

   
   
   
    # for email_dict in all_emails:
    #     if(email_dict['email_id']==request.form['email']):
    #         flash('This email has already been registered','emailError')
    #         return redirect('/show')

    ######### better way to search for a duplicate email id is by changing the sql statement to the one it is right now rather than 
    # having it to be select * from email
    for dict in all_emails:
        if(dict['email_id']==request.form['email']):
            flash('This email has already been registered','emailError')
            return redirect('/show')
    if request.form['email'] == '':
        flash('Email cant be left blank','emailError')
        pass
    elif not EMAIL_REGEX.match(request.form['email']):
        flash('Email adress is not valid!','emailError')
        return redirect('/show')
    else:  
        flash('The email ID that you have entered is valid!','success')  
        mysql=connectToMySQL('mydb')
        mysql.query_db(query)
        print("*"*50)
        return redirect('/show')

@app.route('/show', methods=['POST', 'GET'])
def show():
    query="select * from email"
    mysql=connectToMySQL('mydb')
    email_output=mysql.query_db(query)
    print(email_output)
    return render_template('final.html',emails=email_output)

@app.route('/delete', methods=['POST'])
def delete():
    primary_key=int(request.form['pk'])
    query="DELETE FROM email WHERE id= {};".format(primary_key)
    mysql=connectToMySQL('mydb')
    mysql.query_db(query)
    return redirect ('/show')

if __name__=='__main__':
    app.run(debug=True)
