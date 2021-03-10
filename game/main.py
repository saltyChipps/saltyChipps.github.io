import sqlite3
connection = sqlite3.connect('sports/soccer.db')
sql = connection.cursor()

sql.execute('create table if not exists users(ID integer primary key autoincrement, username Text, password Text, data Text)')


def signup(username, password):
    data = sql.execute('''select * from users where username = ?''', [username])
    rows = data.fetchall()
    if rows:
        print("error: User already exists")
    else:
        sql.execute('''insert into users (username, password) values (?, ?) ''', [username, password])
        connection.commit()
        print(sql.lastrowid)


def signin(username, password):
    data = sql.execute('''select * from users where username = ? and password = ?''', [username, password])
    rows = data.fetchone()
    if rows:
        print(rows[0])
    else:
        print("error: Incorrect username/password")

def clearData(user_id):
    sql.execute('delete from data where userId = ?', [user_id])
    connection.commit()

def getInput():
    if (formData):
        data = {}
        for key in formData.keys():
            data[key] = formData[key].value
        return data


###################################################################################
user_input = getInput()

if user_input:
    mode = user_input['mode']
    if mode == 'signup':
        signup(user_input['username'], user_input['password'])
    elif mode == 'login':
        signin(user_input['username'], user_input['password'])
    elif mode == "clear":
        clear(user_input['userId'])