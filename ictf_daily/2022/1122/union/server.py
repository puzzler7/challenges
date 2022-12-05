#!/usr/bin/env python3

from sqlite3 import *
from flask import Flask, request, Response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
app = Flask(__name__)
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["50000 per hour"],
    storage_uri="memory://",
)

@app.route('/', methods=["GET"])
@limiter.limit("2/second")
def index():
    if 'lastname' not in request.args:
        return open("index.html").read()
    else:
        con = connect("users.db")
        cur = con.cursor()
        res = cur.execute(f"SELECT * from authors where last LIKE '%{request.args['lastname']}%'")
        ret = '<table>'
        ret += '<tr><th>First Name</th> <th>Middle Name</th> <th>Last Name</th></tr>'
        for row in res:
            ret += '<tr>'
            for entry in row:
                ret += f"<td>{entry}</td>"
            ret += '</tr>'
        ret += '</table>'
        return ret

if __name__ == "__main__":
    # con = connect("users.db")
    # cur = con.cursor()
    # cur.execute('''
    #     CREATE TABLE authors(first, middle, last)
    # ''')
    # cur.execute('''
    #     INSERT INTO authors VALUES
    #         ("Tobias", '', "Smollett"),
    #         ("William", '', "Shakespeare"),
    #         ("Edward", "Morgan", "Forster"),
    #         ("George", "", "Eliot"),
    #         ("Louisa", "May", "Alcott"),
    #         ("Lucy", "Maud", "Montgomery"),
    #         ("Frank", "T.", "Merill"),
    #         ("Herman", "", "Melville"),
    #         ("Alexandre", "", "Dumas"),
    #         ("Elizabeth", "", "Von Arnim")
    # ''')
    # cur.execute('''
    #     CREATE TABLE hmmwhatshouldicallmyusers(username, passwords)
    # ''')
    # cur.execute('''
    #     INSERT INTO hmmwhatshouldicallmyusers VALUES
    #         ("admin", "ictf{reading_is_good_but_please_stop_reading_my_databases}")
    # ''')
    # con.commit()
    # cur.close()
    # con.close()

    app.run('0.0.0.0', 7005)