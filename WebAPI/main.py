import string
import random
from fastapi import FastAPI
from datetime import datetime
import sqlite3

app = FastAPI(
    title="REST API (CRUD)"
)

local_parameter = "sasat+lezhat"


@app.put('/')
def Create_NewUser(name: str, password: str):
    con = sqlite3.connect("DB.db", check_same_thread=False)
    cur = con.cursor()
    salt = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    h = 0

    for i in password + salt + local_parameter:
        h += ord(i)

    cur.execute(f"""INSERT INTO Users(username, password, salt, created_at, updated_at) 
                VALUES ("{name}", "{h}", "{salt}", "{datetime.now().strftime('%d.%m.%Y %H:%M:%S')}", "{datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")""")

    id = list(cur.execute(f"""select id from Users where username = "{name}" and password = {h} """))[0]

    con.commit()
    con.close()

    return {
        "status": "ok",
        "data": None,
        "details": f"Пользователь создан, ваш id {id}"
    }


def auntifications(password, id):
    con = sqlite3.connect("DB.db", check_same_thread=False)
    cur = con.cursor()

    user = list(cur.execute(f"""select * from Users where id = "{id}" """))[0][0]

    h = 0
    for i in password + user[3] + local_parameter:
        h += ord(i)

    if h == user[2]:
        con.close()
        return {
            "status": "ok",
            "data": user,
            "details": None
        }
    con.close()
    return {
        "status": "error",
        "data": None,
        "details": "Неверный пароль"
    }


@app.get("/{id}")
def Read_user(password: str, id: int = 0):
    return auntifications(password, id)


@app.patch("/{id}")
def update_user(what_to_update: str, what_to_change: str, password: str, id: int = 0):
    con = sqlite3.connect("DB.db", check_same_thread=False)
    cur = con.cursor()

    result = auntifications(password, id)

    if result['status'] == 'ok':
        if what_to_update != 'password':
            cur.execute(f"""UPDATE Users SET username = "{what_to_change}" WHERE id = {result['data'][0]}""")
            cur.execute(f'''UPDATE Users SET update_at = "{datetime.now().strftime('%d.%m.%Y %H:%M:%S')}" ''')
            con.commit()
            con.close()

            return {
                "status": "ok",
                "data": None,
                "details": f'{what_to_update} был изменён на {what_to_change}'
            }
        else:
            h = 0
            for i in what_to_change + result['data'][3] + local_parameter:
                h += ord(i)

            cur.execute(f"""UPDATE Users SET password = {h} WHERE id = {result['data'][0]}""")
            con.commit()
            con.close()

            return {
                "status": "ok",
                "data": None,
                "details": f'{what_to_update} был изменён'
            }
    else:
        con.close()
        return result


@app.delete('/{id}')
def Del_user(password, id):
    con = sqlite3.connect("DB.db", check_same_thread=False)
    cur = con.cursor()

    result = auntifications(password, id)

    if result['status'] == 'ok':
        cur.execute(f"""DELETE FROM Users WHERE id= {id}""")
        cur.execute(f"""DELETE FROM Booking WHERE user_id= {id}""")
        con.commit()
        con.close()

        return {
            "status": "ok",
            "data": None,
            "details": f'Акаунт был удалён'
        }
    else:
        return result


@app.put('/{id}/booking')
def create_booking(password: str, id: int, start_time: datetime, end_time: datetime, comment: str = ''):
    con = sqlite3.connect("DB.db", check_same_thread=False)
    cur = con.cursor()

    result = auntifications(password, id)

    def comparison(x):
        if x[0].date() == start_time.date() or x[1].date() == start_time.date():
            return True
        return False

    if result['status'] == 'ok':
        booking = list(cur.execute(f"""select start_time, end_time from Booking """))
        booking = list(map(lambda x: list(map(lambda b: datetime.strptime(b, '%d.%m.%Y %H:%M:%S'), x)), booking))
        booking = list(filter(comparison, booking))

        if booking:
            flag = True
            for i in booking:
                if i[0] <= start_time and i[1] > start_time:
                    flag = False
                    break
                if i[0] < end_time and i[0] >= start_time:
                    flag = False
                    break
            if flag:
                cur.execute(f"""INSERT INTO Booking(user_id, start_time, end_time, comment)
                                        VALUES ({result['data'][0]}, "{start_time}", "{end_time}", "{comment}")""")
                con.commit()
                con.close()

                return {
                    "status": "ok",
                    "data": None,
                    "details": f'бронирование создано'
                }
            return {
                "status": "error",
                "data": None,
                "details": f'мест нет'
            }

        cur.execute(f"""INSERT INTO Booking(user_id, start_time, end_time, comment)
                        VALUES ({result['data'][0]}, "{start_time.strftime('%d.%m.%Y %H:%M:%S')}", "{end_time.strftime('%d.%m.%Y %H:%M:%S')}", "{comment}")""")
        con.commit()
        con.close()
        return{
            "status": "ok",
            "data": None,
            "details": f'бронирование создано'
        }
    else:
        return result


@app.get('/{id}/booking')
def get_booking(password: str, id: int):
    con = sqlite3.connect("DB.db", check_same_thread=False)
    cur = con.cursor()

    result = auntifications(password, id)

    if result['status'] == 'ok':
        booking = list(cur.execute(f"""select * from Booking where user_id = {id}"""))
        con.close()
        return{
            "status": "ok",
            "data": booking,
            "details": None
        }
    con.close()
    return result


@app.delete('/{id}/booking')
def del_booking(password: str, id: int, b_id: int):
    con = sqlite3.connect("DB.db", check_same_thread=False)
    cur = con.cursor()

    result = auntifications(password, id)

    if result['status'] == 'ok':
        booking =  list(cur.execute(f"""select * from Booking where id = {b_id}"""))[0]
        if booking[1] == id:
            cur.execute(f"""DELETE FROM Booking WHERE id= {b_id}""")
            con.commit()
            con.close()

            return {
                "status": "ok",
                "data": None,
                "details": 'Бронирование  удаленно'
            }

        return {
            "status": "error",
            "data": None,
            "details": "Это не ваше бронирование"
        }

    return result