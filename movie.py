from flask import Flask,render_template,request,redirect
import os

import pymysql
conn= pymysql.connect(host='localhost',user='root',passwd='1234',port=3306,database='mycinema')


app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    if request.method =='POST':
        userDetails = request.form
        CustomerName = userDetails['CustomerName']
        Tickets = userDetails['Tickets']
        Price = userDetails['Price']
        Showtime = userDetails['Showtime']
        Cinema = userDetails['Cinema']

        cur = conn.cursor()
        cur.execute("INSERT INTO users(CustomerName,Tickets,Price,Showtime,Cinema) VALUES(%s,%s,%s,%s,%s)",
                    (CustomerName,Tickets,Price,Showtime,Cinema))
        conn.commit()
        cur.close()
        return redirect('/users')
    return render_template('login.html')

'''venom_folder = os.path.join('static','venom_photo')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = venom_folder

@app.route('/')
@app.route('/users')
def show_index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'venom.png')
    return render_template("login.html", user_image = full_filename)'''


@app.route('/users')
def users():
    cur = conn.cursor()
    resultValue = cur.execute("SELECT * FROM users")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html', userDetails=userDetails)


if __name__ == "__main__":
    app.run(debug=True)

