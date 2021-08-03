'''
Created on 14 lut 2014

@author: Srokks
'''
# -*- coding: utf-8 -*-

import sqlite3 as lite

class Biblioteka:
    def __init__(self):
        self.database = "ksiazki.db"
        self.con = lite.connect('%s' % self.database)
    def getUser(self):
        with self.con:
            self.cur = self.con.cursor()
            self.cur.execute("SELECT * FROM uzytkownicy")
            self.rows = self.cur.fetchall()
        self.con.close()
        return (self.rows)

    def getBooks(self):

        with self.con:
            self.cur=self.con.cursor()
            self.cur.execute("SELECT * FROM ksiazki")
            self.rows=self.cur.fetchall()
        self.con.close()
        return (self.rows)

    def getBooksState(self):

        with self.con:
            self.cur=self.con.cursor()
            self.cur.execute("SELECT * FROM na_stanie")
            self.rows=self.cur.fetchall()
        self.con.close()
        return (self.rows)

    def setBooksState(self,userID,bookID):
        self.uID=userID
        self.bID=bookID
        with self.con:
            self.cur = self.con.cursor()
            self.cur.execute("UPDATE na_stanie SET jest=0,kto=%i WHERE id=%i" % (self.uID,self.bID))
            #self.cur.execute("UPDATE na_stanie SET jest=0,kto=%i WHERE id=%i" % (self.userID,self.bookID))
        self.con.close()

    def resetBooksState(self,bookID):
        self.bID=bookID
        self.empty=u''

        with self.con:
            self.cur = self.con.cursor()
            self.cur.execute("UPDATE na_stanie SET jest=1,kto=0 WHERE id=%i" % self.bID)
        self.con.close()
    def getUserID(self,userName):
        self.userNames=userName

        with self.con:
            self.cur=self.con.cursor()
            self.cur.execute("SELECT id FROM uzytkownicy WHERE name='%s'" % self.userNames)
            self.row=self.cur.fetchone()
        self.con.close()
        return self.row
    def getBookID(self,bookName):
        self.a=bookName.find('-')
        self.booksName=bookName[self.a+1:]

        with self.con:
            self.cur=self.con.cursor()
            self.cur.execute("SELECT id FROM ksiazki WHERE nazwa='%s'" % self.booksName)
            self.row=self.cur.fetchone()
        self.con.close()
        return self.row
    def addBook(self,name,author):
        self.b_name=name
        self.b_author=author
        with self.con:
            self.cur=self.con.cursor()
            self.cur.execute("INSERT INTO ksiazki (nazwa,autor) VALUES ('%s','%s')" %(self.b_name,self.b_author))
            self.cur.execute("INSERT INTO na_stanie (jest,kto) VALUES (1,0)")
        self.con.close()

    def addUser(self,name):
        self.b_name=name
        with self.con:
            self.cur=self.con.cursor()
            self.cur.execute("INSERT INTO uzytkownicy (name) VALUES ('%s')" %self.b_name)

        self.con.close()