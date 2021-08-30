import sqlite3
import os
from sys import path

ROOT = os.path.dirname(os.path.realpath(__file__))

def create_course(nome_curso, nome_facilitaor, link, info, valor, validacao):
    con = sqlite3.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('insert into facilitador (nome_curso, nome_facilitaor, link, info, valor, validacao) values(?,?,?,?,?,?', (nome_curso, nome_facilitaor, link, info, valor, validacao))
    con.commit()
    con.close()
    
def get_course():
    con = sqlite3.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute("SELECT * FROM facilitador")