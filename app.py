from flask import Flask 
from flask import render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'app'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
        if request.method == "POST":
           email = request.form['email']
           message = request.form['message']
           cur = mysql.connection.cursor()
           cur.execute("INSERT INTO app(email, message) VALUES (%s, %s)", (email, message))
           mysql.connection.commit()
           cur.close()
        #    return 'success'
        return render_template ('index.html')

if __name__ == '__main__':
    app.run(debug=True)
