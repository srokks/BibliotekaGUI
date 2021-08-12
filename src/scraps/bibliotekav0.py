'''
Created on 23 sty 2014
Completed ver. 0.1 on 14 lut 2014
@author: Srokks
'''
# -*- coding: utf-8 -*-
import sqlite3 as lite


class Biblioteka:
    
    def __init__(self):
        self.dispMain()
    
    def getUser(self):
        self.database = "ksiazki.db"
        self.con = lite.connect('%s' % self.database)
        with self.con:    
            self.cur = self.con.cursor()    
            self.cur.execute("SELECT * FROM uzytkownicy")
            self.rows = self.cur.fetchall()
        self.con.close()
        return (self.rows)
    
    def getBooks(self):
        self.database= "ksiazki.db"
        self.con = lite.connect('%s' % self.database)
        with self.con:
            self.cur=self.con.cursor()
            self.cur.execute("SELECT * FROM ksiazki")
            self.rows=self.cur.fetchall()
        self.con.close()
        return (self.rows)
    
    def getBooksState(self):
        self.database = "ksiazki.db"
        self.con=lite.connect("%s" % self.database)
        with self.con:
            self.cur=self.con.cursor()
            self.cur.execute("SELECT * FROM na_stanie")
            self.rows=self.cur.fetchall()
        self.con.close()
        return (self.rows)
    
    def CLS(self):
        print '\n'*25
    
    def dispMain(self):
        self.key=''
        while (self.key!='k' and self.key!='K'):
            self.CLS()
            print '='*35
            print "Witaj w systemie bibliotecznym"
            print '='*35
            print '1.Zaloguj uzytkownika'
            print '2.Dodaj nowa ksiazke'
            print '3.Dodaj uzytkownika'
            print '3.Zakoncz'
            print '='*35
            self.key=raw_input("Co chcesz zrobic?\t")
            if self.key=='1':
                self.dispUser()
            elif self.key=='2':
                self.dispInsertBook()
            elif self.key=='3':
                self.dispInsertUser()
            elif self.key=='4':
                self.key='k'
    
    def dispUser(self):
        self.users=self.getUser()
        self.key=''
        self.i=0
        self.CLS()
        print '='*35
        print "Lista uzytkownikow biblioteki"
        print '='*35
        for self.elem in self.users:
            print str(self.elem[0])+'. '+self.elem[1]
            self.i+=1
        print str(self.i+1)+'. koniec'
        self.key=input("Wybierz uzytkownika:\t") 
        if(self.key==self.i+1):
            self.dispMain()
        elif(self.key<self.i+1):
            self.dispChoose(self.key)
        else:
            print "BLAD"
    def dispChoose(self,key):
        self.userID=key
        self.key=''
        while (self.key!='k' and self.key!='K'):
            self.CLS()
            print '='*35
            print "Co chce "+self.getUser()[int(self.userID)-1][1] +" zrobic"
            print '='*35
            print '1.Wyporzycza'
            print '2.Oddaje'
            print '3.Zakoncz'
            print '='*35
            self.key=raw_input("Co chcesz zrobic?\t")
            if self.key=='1':
                self.dispBorrow(self.userID)
            elif self.key=='2':
                self.dispGetBack(self.userID)
            elif self.key=='3':
                self.dispMain()
            
   
    def dispBorrow(self,userID):
        self.uID=userID
        self.books=self.getBooks()
        self.bookstate=self.getBooksState()
        self.key=''
        self.i=0
        self.j=1
        #self.CLS()
        print '='*35
        print "Lista ksiazek do wyporzyczenia "
        print '='*35 
        self.i=0
        self.j=0
        self.temp={}            
        for self.elem in self.books:
            if(self.bookstate[self.i][1]==1):
                print str(self.j+1)+'. '+self.elem[2]+'\t"'+self.elem[1]+'"'
                self.j+=1
                self.temp[self.j]=self.i+1
            self.i+=1       
        print str(self.j+1)+'. Koniec'
        self.key=input("Wybierz ksiazke do wyporzyczenia:\t")
        if(self.key==self.j+1):
            self.dispMain()
        elif(self.key in self.temp):
            self.setBooksState(self.uID, self.temp[self.key])
        else:
            print "BLAD"
            
    def dispGetBack(self,userID):
        self.uID=userID
        self.bookstate=self.getBooksState()
        self.books=self.getBooks()
        print '='*35
        print "Lista ksiazek do oddania przez uzytkownika "
        print '='*35      
        self.i=0
        self.j=0
        self.temp={}
        for self.elem in self.books:
            if(self.bookstate[self.i][2]==self.uID):
                print str(self.j+1)+'. '+self.elem[2]+'\t"'+self.elem[1]+'"'
                self.j+=1
                self.temp[self.j]=self.i+1
            self.i+=1   
        print str(self.j+1)+'. Koniec'
        self.key=input("Wybierz ksiazke do wyporzyczenia:\t")
        if(self.key==self.j+1):
            self.dispMain()
        elif(self.key in self.temp):
            self.resetBooksState(self.temp[self.key])
        else:
            print "BLAD"
               
    def setBooksState(self,userID,bookID):
        self.uID=userID
        self.bID=bookID
        self.database = "ksiazki.db"
        self.con = lite.connect('%s' % self.database)
        with self.con:    
            self.cur = self.con.cursor()    
            self.cur.execute("UPDATE na_stanie SET jest=0,kto=%i WHERE id=%i" % (self.uID,self.bID))
            #self.cur.execute("UPDATE na_stanie SET jest=0,kto=%i WHERE id=%i" % (self.userID,self.bookID))
        self.con.close()
        raw_input("Operacja wyporzyczenia zakonczona pomyslnie")
        
    def resetBooksState(self,bookID):
        self.bID=bookID
        self.empty=u''
        self.database = "ksiazki.db"
        self.con = lite.connect('%s' % self.database)
        with self.con:    
            self.cur = self.con.cursor()    
            self.cur.execute("UPDATE na_stanie SET jest=1,kto=0 WHERE id=%i" % self.bID)
        self.con.close()
        raw_input("Operacja odddania zakonczona pomyslnie")
        
    def dispInsertBook(self):
        self.CLS()
        print '='*35
        print "Dodawanie ksiazek "
        print '='*35
        temp=[]
        temp.append(raw_input("Podaj nazwe ksiazki:\t"))
        temp.append(raw_input("Podaj autora ksiazki\t"))
        self.setInsertBook(temp)
    
    def setInsertBook(self,temp):
        self.ksiazka=temp
        self.database = 'ksiazki.db'
        self.con = lite.connect('%s' % self.database)
        with self.con:
            self.cur = self.con.cursor()
            self.cur.execute("INSERT INTO ksiazki (nazwa,autor) VALUES ('%s','%s') " % (self.ksiazka[0],self.ksiazka[1]))
            self.cur.execute("INSERT INTO na_stanie(jest,kto) VALUES (1,0) ")
        self.con.close()
        raw_input("Operacja odddania zakonczona pomyslnie")
        
    def dispInsertUser(self):
        self.CLS()
        print '='*35
        print "Dodawanie uzytkownika "
        print '='*35
        temp=raw_input("Podaj imie i nazwisko nowego uzytkownika:\t")
        self.setInsertUser(temp)
        
    def setInsertUser(self,temp):
        self.user=temp
        self.database = 'ksiazki.db'
        self.con = lite.connect('%s' % self.database)
        with self.con:
            self.cur = self.con.cursor()
            self.cur.execute("INSERT INTO uzytkownicy (name) VALUES ('%s') " % self.user)
        self.con.close()
        raw_input("Operacja odddania zakonczona pomyslnie")