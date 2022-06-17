# from flask import Flask, redirect, render_template, request, url_for, session
from flask import *
from flask_mysqldb import MySQL
from flask_session import Session
import os
from flask import *
from fileinput import filename
from werkzeug.utils import secure_filename
from matplotlib.style import use


app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'riyaesmsys'
app.config['MYSQL_DB'] = 'login_sample'
app.config['UPLOAD_FOLDER'] = 'D:/python_esmsys/flask/flask_login_project/static/'

mysql = MySQL(app)

uploaded_files = os.listdir('D:/python_esmsys/flask/flask_login_project/static/')
cd = uploaded_files[2]           

@app.route("/", methods = ['POST', 'GET'])
def login():
    # return render_template('login.html')
    if request.method == 'POST':
        lusername = request.form['username']
        lpassword = request.form['password']
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM user WHERE username = % s',(lusername,))
        account = cur.fetchall()
        # user_id = account[0][5]
        print('*********************************************************************************************************************************************************************************///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print(account)
        # print(account[0][0], account[0][2])
        # name and password index
        print('*********************************************************************************************************************************************************************************///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')

        if account == ():
            # len(account) == 0
            print('user already exist')
            redirect_url = 'http://127.0.0.1:5000/signup' 
            return f"<html><body><p>Username not found,   Please SignUp first,  You will be redirected to Signup page in 5 seconds</p><script>var timer = setTimeout(function() {{window.location='{ redirect_url }'}}, 5000);</script></body></html>"     
        else:
            if account[0][0] == lusername and account[0][2] == lpassword :
                user_id = account[0][5]
                ("hreloo0 shelllii vckocvk d")
                buddy = uploaded_files
                print(buddy)
                # for i in uploaded_files:
                # l_second = []
                # if f'{lusername}.pdf' in uploaded_files:
                #     l_second.append(f'{lusername}.pdf')
                # print(l_second)
                # print(cd)
                return redirect(url_for('success', user_id = user_id, cd = f'{lusername}.pdf'))
            else :
                redirect_url = 'http://127.0.0.1:5000/' 
            return f"<html><body><p>Username or Password is incorrect, Please Enter correct Login and Password,  You will be redirected to Login page in 5 seconds</p><script>var timer = setTimeout(function() {{window.location='{ redirect_url }'}}, 5000);</script></body></html>"     
                
    else:
        return render_template('login.html')



@app.route("/signup", methods = ['GET', 'POST'])
def signup():
    # return render_template('login.html')
    if request.method == 'POST':
        details = request.form
        usernm = details['username']
        f = request.files['file']
        print(request.files)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f'{usernm}.pdf')))
        # uploaded_files = os.listdir('D:/python_esmsys/flask/flask_login_project/static/')
        # cd = uploaded_files[0]
        print(uploaded_files)
        print('kuch bhi')
        # details = request.form
        # usernm = details['username']
        pwd = details['password']
        eml = details['email']
        # *************************************************************************************
        # f = request.files['file']
        # print(request.files)
        # f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        # uploaded_files = os.listdir('flask_login_project/static')
        # cd = uploaded_files
        # print('kuch bhi')
        # *******************************************************************************
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO login_sample.user(username, password, email) VALUES (%s, %s, %s)",(usernm, pwd, eml))
        mysql.connection.commit()
        cur.execute('SELECT * FROM user WHERE username = % s',(usernm,))
        account_detail = cur.fetchall()
        user_id = account_detail[0][5]
        cur.close()
        # path = "D:/python_esmsys/flask/flask_login_project/static/MANHATTAN_5LBS_GRE.pdf"
        # send_file(path, as_attachment=True)
        return redirect(url_for('success', user_id = user_id, cd = f'{usernm}.pdf'))
        # return render_template('tmp.html',cd=cd)

    else:
        return render_template('signup.html')



@app.route('/success/<user_id>/<cd>', methods = ['POST', 'GET'])
def success(user_id,cd):
    
    # cur = mysql.connection.cursor()
    # cur.execute('SELECT * FROM user WHERE username = % s',(name,))
    # account = cur.fetchall()
    # print(account)

    # return 'welcome' + '  ' + name
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM user WHERE id = % s',(user_id,))
        account = cur.fetchall()
        user_id = account[0][5]
        print('jxhabcahbcsdhcsdhcbhcb')
        print(user_id)
        print('*********')
        details = request.form
        usernms = details['username']
        pwd = details['password']
        eml = details['email']
        city_u =details['city'] 
        cur.execute("UPDATE user SET username = %s, email = %s, password = %s, city = %s WHERE id = %s", (usernms, eml, pwd, city_u, user_id))
        mysql.connection.commit()
        cur.execute('SELECT * FROM user WHERE id = % s',(user_id,))
        baccount = cur.fetchall()
        
        # user_id = baccount[0][5]
        # print('*********************************************************************************************************************************************************************************///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        # print(baccount)
        # print('jxhabcahbcsdhcsdhcbhcb')
        # print(user_id)
        # print('*********************************************************************************************************************************************************************************///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        return render_template('display.html', account = baccount, cd = cd)

    else:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM user WHERE id = % s',(user_id,))
        account = cur.fetchall()
        print(account)
        # if account:
        #     path = "D:/python_esmsys/flask/flask_login_project/static/MANHATTAN_5LBS_GRE.pdf"
        #     return send_file(path, as_attachment=True)
        # print('*********************************************************************************************************************************************************************************///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        return render_template('display.html', account = account, cd = cd)

    # return render_template('display.html', account = account)


@app.route('/delete/<user_id>', methods = ['POST', 'GET'])
def delete(user_id):
    # print(user_id)
    print('zcdsdsdsvsdvvdvsvdvvdsvvdvdf))))))))))))))))))))))))))))))))))))))))))))))))')
    print(user_id)
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM user WHERE id = % s',(user_id,))
    mysql.connection.commit()

    return 'close' 




app.run(debug = True)


# @app.route('/success/<name>', methods = ['POST', 'GET'])
# def success(name):
#     # cur = mysql.connection.cursor()
#     # cur.execute('SELECT * FROM user WHERE username = % s',(name,))
#     # account = cur.fetchall()
#     # print(account)

#     # return 'welcome' + '  ' + name
#     if request.method == 'POST':
#         details = request.form
#         usernms = details['username']
#         pwd = details['password']
#         eml = details['email']
#         cur = mysql.connection.cursor()
#         print(usernms)
#         print('*********************************************************************************************************************************************************************************///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
#         # cur.execute("UPDATE user SET username = %s WHERE password ='goli123'", (usernms, ))
#         cur.execute("UPDATE user SET username = %s, email = %s WHERE password = %s", (usernms, eml, pwd))
#         # baccount = cur.fetchall()
#         mysql.connection.commit()
#         # cur.close()
#         cur.execute('SELECT * FROM user WHERE username = % s',(usernms,))
#         baccount = cur.fetchall()
#         print('*********************************************************************************************************************************************************************************///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
#         print(baccount)
#         print('*********************************************************************************************************************************************************************************///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')
#         return render_template('display.html', account = baccount)

#     else:
#         cur = mysql.connection.cursor()
#         cur.execute('SELECT * FROM user WHERE username = % s',(name,))
#         account = cur.fetchall()
#         print(account)
#         return render_template('display.html', account = account)







# @app.route("/signup", methods = ['POST', 'GET'])
# def signup():
#     # return render_template('login.html')
#     if request.method == 'POST':
#         details = request.form
#         usernm = details['username']
#         pwd = details['password']
#         eml = details['email']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO login_sample.user(username, password, email) VALUES (%s, %s, %s)",(usernm, pwd, eml))
#         mysql.connection.commit()
#         cur.close()
#         return redirect(url_for('success', name = usernm))

#     else:
#         return render_template('signup.html')



# -- ALTER TABLE user
# -- ADD id INT NOT NULL AUTO_INCREMENT PRIMARY KEY;