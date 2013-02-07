# -*- coding: utf-8 -*-
# Fake Sqlite
# This file simulate a Sqlite insert
fake_memory =open("sqlite.db.txt", "a")
def insert(login, password):
    fake_memory.write("login :%s :password : %s \n\r" %(
                        login , password))
                      
                      
def get(login):
    with open(fake_memory) as fs:
        lines = fs.readlines()
        for line in lines:
            if line.startwith('loing :%s'%login):
                return line
