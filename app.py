from flask import Flask, render_template, request,redirect,url_for
from database import *
app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("homepage.html")




@app.route('/see_jobs')
def see_jobs():
    workplaces = get_all_workplaces()
    return render_template("see_jobs.html", workplaces=workplaces)





@app.route('/add_a_job', methods=['GET', 'POST'])
def add_a_job():
    #return render_template("add_a_job.html")
    if request.method == 'GET':
        return render_template('add_a_job.html')
    else:
        name = request.form['name']
        age = request.form['agelimit']
        location = request.form['location']
        phone = request.form['phonenumber']
        description = request.form['description']


        save_to_database(name,age,location,phone,description)        
        print("go to see jobs")
        return redirect(url_for('see_jobs'))
           







if __name__ == '__main__':
    app.run(debug=True)

