'''import wx
from biblioteka import Biblioteka as bibl, Biblioteka
#-*-utf-8-*-
##########################################################################################################
''''''
Buttons id:
    back=22
    login=21
    books=3+
    wyporzycza=25
    oddaje=26
''''''
##########################################################################################################
#TODO: sadasd
class MainWindow(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, title='Biblioteka::glowne okno')
        box1=wx.BoxSizer(wx.VERTICAL)
        self.panelMain=self.panelMain()
        self.panelLogIn=self.panelLogIn()
        self.panelBooksBorrow=self.panelBooksBorrow()
        self.panelBooksBack=self.panelBooksBack()
        box1.Add(self.panelMain,1,wx.CENTER)
        box1.Add(self.panelLogIn,1,wx.CENTER)
        box1.Add(self.panelBooksBorrow,1,wx.CENTER)
        box1.Add(self.panelBooksBack,1,wx.CENTER)
        self.uID=1
        self.SetSizer(box1)
        self.panelMain.Show()
        self.panelLogIn.Hide()
        self.panelBooksBorrow.Hide()
        self.panelBooksBack.Hide()
        self.Center()
#---------------------------------------------------------------------------------------------------------
    def panelMain(self):
        panel1=wx.Panel(self,-1)
        box=wx.BoxSizer(wx.VERTICAL)
        box.Add(wx.Button(panel1,21,'Zaloguj uzytkownika'),0,wx.EXPAND|wx.ALL,5)
        box.Add(wx.Button(panel1,99,'Zamknij'),0,wx.EXPAND|wx.ALL,5)
        self.Bind(wx.EVT_BUTTON,self.onShowBooks,id=21)
        self.Bind(wx.EVT_BUTTON,self.onClose,id=99)
        panel1.SetSizer(box)
        box.Fit(self)
        return panel1
#---------------------------------------------------------------------------------------------------------
    def panelChoices(self):
        panel=wx.Panel(self,-1)
        box=wx.BoxSizer(wx.HORIZONTAL)
        box.Add(wx.Button(panel,25,'Wyporzycza'),0,wx.EXPAND|wx.ALL,5)
        box.Add(wx.Button(panel,26,'Oddaje'),0,wx.EXPAND|wx.ALL,5)
        panel.SetSizer(box)
        box.Fit(self)
        return panel
#---------------------------------------------------------------------------------------------------------
    def panelBooksBorrow(self):
        i=0
        panel=wx.Panel(self,-1)
        boxa=wx.BoxSizer(wx.VERTICAL)
        for row in bibl().getBooks():
            if (Biblioteka().getBooksState()[i][1]==1):
                boxa.Add(wx.Button(panel,30+row[0],row[2]+'-"'+row[1]+'"'),0)
                i+=1
        boxa.Add(wx.Button(panel,22,'Powrot'),0)
        self.Bind(wx.EVT_BUTTON,self.onBookreturn,id=31)
        panel.SetSizer(boxa)
        boxa.Fit(self)
        return panel
#---------------------------------------------------------------------------------------------------------
    def panelBooksBack(self):
        i=0
        temp=[]
        uID=1
        panel=wx.Panel(self,-1)
        box=wx.BoxSizer(wx.HORIZONTAL)
        for row in bibl().getBooks():
            if(bibl().getBooksState()[i][2]==uID):
                temp.append(row[0],row[2]+'-"'+row[1]+'"')
            i+=1
        if not temp:
            box.Add(wx.StaticText(panel,label=u"\nUzytkownik nic nie wypozyczyl",style=wx.CENTER))
        else:
            box.Add(wx.ComboBox(panel,pos=(50, 30),choices=temp,style=wx.CB_READONLY))
        panel.SetSizer(box)
        panel.Position
        return panel


#    cb = wx.ComboBox(pnl, pos=(50, 30), choices=distros,
#           style=wx.CB_READONLY)
#             self.i=0
#         self.j=0
#         self.temp={}
#         for self.elem in self.books:
#             if(self.bookstate[self.i][2]==self.uID):
#                 print str(self.j+1)+'. '+self.elem[2]+'\t"'+self.elem[1]+'"'
#                 self.j+=1
#                 self.temp[self.j]=self.i+1
#             self.i+=1
#---------------------------------------------------------------------------------------------------------
    def panelLogIn(self):
        panel=wx.Panel(self,-1)
        boxa=wx.BoxSizer(wx.VERTICAL)
        for row in bibl().getUser():
            boxa.Add(wx.Button(panel,3+row[0],row[1]),0)
        boxa.Add(wx.Button(panel,21,'Powrot'),0)
        panel.SetSizer(boxa)
        self.Bind(wx.EVT_BUTTON,self.onLoginDisp,id=22)
        boxa.Fit(self)
        return panel
#---------------------------------------------------------------------------------------------------------
    def onClose(self,event):
        self.Close()
#---------------------------------------------------------------------------------------------------------
    def onLoginDisp(self,event):
        """"""
        if self.panelMain.IsShown():
            self.SetTitle("Biblioteka::zaloguj uzytkownika")
            self.panelBooks.Hide()
            self.panelMain.Hide()
            self.panelLogIn.Show()
        else:
            self.SetTitle("Biblioteka::glowne okno")
            self.panelMain.Show()
            self.panelLogIn.Hide()
            self.panelBooks.Hide()
        self.Layout()

#---------------------------------------------------------------------------------------------------------
    def panelsHide(self):
        self.panelMain.Hide()
        self.panelLogIn.Hide()
        self.panelBooks.Hide()
#---------------------------------------------------------------------------------------------------------
    def onShowBooks(self,event):
        self.panelsHide()
        self.panelBooksBack.Show()

        self.Layout()

    def onBookreturn(self,event):
        if id==31:
            self.onLoginDisp()
        else:
            self.panelLogIn.Hide()
            self.panelBooks.Hide()
            self.panelMain.Show()

##########################################################################################################
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MainWindow().Show()
    app.MainLoop()
    
'''


# '''
# Created on 3 lut 2014
# 
# @author: Srokks
# '''
# # -*- coding: utf-8 -*-
# import linecache
# import sqlite3 as lite
# import os
# class Biblioteka:
#     def __init__(self):
#         self.key=''
#         while (self.key!='k' and self.key!='K'):
#             self.CLS()
#             print '='*35
#             print "Witaj w systemie bibliotecznym"
#             print '='*35
#             print '1.Wyporzycz ksiazke'
#             print '2.Oddaj ksiazke'
#             print '3.Zakoncz'
#             print '='*35
#             self.key=raw_input("Co chcesz zrobic?\t")
#             if self.key=='1':
#                 self.Borrow()
#             elif self.key==2:
#                 print '='*35
#                 #self.GetBack()
#             elif self.key==3:
#                 self.key='k'
#     def CLS(self):
#         print '\n'*25
#     def GetUser(self):
#         self.database = "ksiazki.db"
#         self.con = lite.connect('%s' % self.database)
#         with self.con:    
#             cur = self.con.cursor()    
#             cur.execute("SELECT * FROM uzytkownicy")
#             self.rows = cur.fetchall()
#             print "Ktory uzytkownik przyszedl wypozyczyc?"
#             for self.row in self.rows:
#                 print str(self.row[0])+' || '+self.row[1]
#         self.id=input("Podaj jego nurmer identyfikacyjny:\t")
#         return self.rows[self.id]
#     def GetBooks(self):
#         self.CLS()
#         self.database = "ksiazki.db"
#         self.con = lite.connect('%s' % self.database)
#         print "Ksiazki dostepne:"
#         print "ID  || Tytul    || Autor"
#         with self.con:    
#             cur = self.con.cursor()    
#             cur.execute("SELECT * FROM ksiazki")
#             self.ksiazki = cur.fetchall()
#             cur.execute("SELECT id,jest FROM na_stanie WHERE jest=1")
#             self.na_stanie = cur.fetchall()
#             for self.row in self.ksiazki:
#                 for self.rows in self.na_stanie:
#                     if ((self.row[0]==self.rows[0])and self.rows[1]==1):
#                         print str(self.row[0])+' || '+ self.row[1] +' || ' + self.row[2]
#                         
#     def Borrow(self):
#         self.CLS()
#         self.User=self.GetUser()
#         print self.User
#         
#         
#         
#         def resetBookState(self,bookID):
#         self.bID=bookID
#         self.database = "ksiazki.db"
#         self.con = lite.connect('%s' % self.database)
#         with self.con:    
#             self.cur = self.con.cursor()    
#             #self.cur.execute("UPDATE na_stanie SET jest=1,kto=01 WHERE id=%i" % self.bID)
#             self.cur.execute("UPDATE na_stanie SET jest=1,kto=9 WHERE id=0")
#         self.con.close()
#         raw_input("Operacja oddania zakonczona pomyslnie")
#                 