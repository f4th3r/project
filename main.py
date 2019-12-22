import pymysql
from app import app
from db_config import mysqldb
from flask import jsonify
from flask import flash, request
import requests
#import os
#import json
from datetime import datetime
#import sys

@app.route('/users')
def users():
	try:
		conn = mysqldb.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM user")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()


@app.route('/update/<string:user_name>',methods=['PUT'])
def user_name(user_name):
    data = request.get_json()
    dateti = datetime.today()
    if not user_name.isalpha():
        return jsonify('dont  use a numbers in username, please')
    if not datetime.strptime(data['dateOfBirth'], '%Y-%M-%d') < datetime.today():
        return jsonify('Are you from the future?')
    else:
        try:
                birthfromjson = data.get('dateOfBirth')
                conn = mysqldb.connect()
                cursor = conn.cursor()
                cursor.execute("UPDATE user SET name=%s,birth=%s where id=1", (user_name,birthfromjson,))
                conn.commit()
                respone = jsonify('hello,', user_name ,' You just changed the name and birth of ID=1')
                respone.status_code = 204
                return respone
                abort()        
        except Exception as e:
                print(e)
        finally:
                cursor.close()
                conn.close()
                
@app.route('/hello/<user_name2>',methods=['GET'])
def user_name2(user_name2):
        try:
                thisday = datetime.today()
                conn = mysqldb.connect()
                cursor = conn.cursor()
                cursor.execute("SELECT birth FROM user where name=%s",(user_name2))
                data = cursor.fetchall()
                user_time = data[0]
                user_time2 = user_time[0]
                user_bd = (user_time2.month),(user_time2.day)
                current_date = (thisday.month), (thisday.day)
                if (user_bd) == (current_date):
                   respone = jsonify("hello" , user_name2, "happy bday!")
                   respone.status_code = 200
                   cursor.close()
                else:
                    nextbday = datetime(thisday.year,user_time2.month,user_time2.day)
                    if not  (thisday > nextbday):
                        hmdays = (nextbday - thisday).days
                    else:
                        nextbday = datetime(thisday.year + 1,user_time2.month,user_time2.day)
                        hmdays = (nextbday - thisday).days
                    respone = jsonify("hello",user_name2,'your bday in', hmdays, 'days!')
                    respone.status_code = 200
                    return respone
                return respone
        except  Exception as e:
                 print(e)
        finally:
                cursor.close() 
                conn.close()                
                
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
