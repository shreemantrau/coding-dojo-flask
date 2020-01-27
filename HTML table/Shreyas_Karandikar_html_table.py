from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def root():
    print("inside route")
    users=[
        {'first_name':'Michael', 'last_name':'Choi'},
        {'first_name': 'John','last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name':'Tonel'}
        ]
    return render_template('html_table.html',users=users)
app.run(debug=True)