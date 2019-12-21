from app import app
from flaskext.mysql import MySQL

mysqldb = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'pajke'
app.config['MYSQL_DATABASE_PASSWORD'] = '5613Cd*aa'
app.config['MYSQL_DATABASE_DB'] = 'project'
mysqldb.init_app(app)