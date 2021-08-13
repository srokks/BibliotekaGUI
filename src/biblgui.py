import wx
from biblioteka import Biblioteka as bibl, Biblioteka
#-*-utf-8-*-
##########################################################################################################
'''
ID Buttonow
    zamknij=99
    zaloguj=21
    ok(panel_login)=22
    back(panel_login)=23
    wypozycza=25
    oddaje=26
    ok_wypozycza=28
    od_oddaje=29
    powrot(z choicces)=30
    wyswietl wypozyczone=31
    dodaj ksiazke=32
    dodaj uzytkownika=33
    zatwierdzenie dodawania ksiazki=34
    zatwierdzenie dodania uzytkownika=35

'''
##########################################################################################################
class MainWindow(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, wx.ID_ANY, title='Biblioteka::glowne okno')
        self.userID=''
        self.bookID=''
        self.data=['Random','Randon']
        self.bbooks={}
        self.uuser={}

        self.mainbox=wx.BoxSizer(wx.VERTICAL)
        self.panelMain=self.d_panelMain()
        self.panelLogIn=self.d_panelLogIn()
        self.panelChoices=self.d_panelChoices()
        self.panelBooksBorrow=self.d_panelBooksBorrow()
        self.panelBooksBack=self.d_panelBooksBack()
        self.panelBorowed=self.d_panelBorowed()
        self.panelAddBook=self.d_panelAddBook()
        self.panelAddUser=self.d_panelAddUser()
        self.mainbox.Add(self.panelMain,1,wx.CENTER|wx.EXPAND)
        self.mainbox.Add(self.panelLogIn,1,wx.CENTER|wx.EXPAND)
        self.mainbox.Add(self.panelChoices,1,wx.CENTER|wx.EXPAND)
        self.mainbox.Add(self.panelBorowed,1,wx.CENTER|wx.EXPAND)
        self.mainbox.Add(self.panelAddBook,1,wx.CENTER|wx.EXPAND)
        self.mainbox.Add(self.panelAddUser,1,wx.CENTER|wx.EXPAND)
#         self.mainbox.Add(self.panelBooksBorrow,1,wx.CENTER)
#         self.mainbox.Add(self.panelBooksBack,1,wx.CENTER)
        self.SetSize((330, 250))
        self.SetSizer(self.mainbox)
        #self.mainbox.Fit(self)
        self.onHideAll()
        self.panelMain.Show()
        self.Center()
#---------------------------------------------------------------------------------------------------------
    def d_panelMain(self):
        panel=wx.Panel(self,-1)
        box=wx.BoxSizer(wx.VERTICAL)
        box.Add(wx.Button(panel,21,'Zaloguj uzytkownika'),0,wx.EXPAND|wx.ALL,5)
        box.Add(wx.Button(panel,31,'Pokaz wypozyczone ksiazki'),0,wx.EXPAND|wx.ALL,5)
        #TODO: Dodawanie ksiazek
        box.Add(wx.Button(panel,32,'Dodaj nowa ksiazke'),0,wx.EXPAND|wx.ALL,5)
        #TODO: Dodawanie uzytkownikow
        box.Add(wx.Button(panel,33,'Dodaj uzytkownika '),0,wx.EXPAND|wx.ALL,5)
        box.Add(wx.Button(panel,99,'Zamknij'),0,wx.EXPAND|wx.ALL,5)
        box.Add(wx.StaticText(panel,label=''),0,wx.ALIGN_CENTER)
        box.Add(wx.StaticText(panel,label="*- funkcje niedzialajace"),0,wx.ALIGN_CENTER)
        self.Bind(wx.EVT_BUTTON,self.onShowLogIn,id=21)
        self.Bind(wx.EVT_BUTTON,self.onShowBorrowed,id=31)
        self.Bind(wx.EVT_BUTTON,self.onShowAddBook,id=32)
        self.Bind(wx.EVT_BUTTON,self.onShowAddUser,id=33)
        self.Bind(wx.EVT_BUTTON,self.onClose,id=99)

        panel.SetSizer(box)
        #box.Fit(self)
        return panel
#---------------------------------------------------------------------------------------------------------
    def d_panelLogIn(self):
        temp=[]
        panel=wx.Panel(self,-1)
        box=wx.BoxSizer(wx.VERTICAL)
        i=1
        for row in bibl().getUser():
            temp.append(row[1])
            self.uuser[row[1]]=i
            i+=1
        combo=wx.ComboBox(panel,pos=(50,30),choices=temp,style=wx.CB_READONLY)
        combo.Bind(wx.EVT_COMBOBOX, self.setUID)
        box.Add(combo)
        boxa=wx.BoxSizer(wx.HORIZONTAL)
        boxa.Add(wx.Button(panel,22,'OK'),0,wx.EXPAND,5)
        boxa.Add(wx.Button(panel,23,'Powrot'),0,wx.EXPAND,5)
        self.Bind(wx.EVT_BUTTON,self.onShowChoices,id=22)
        self.Bind(wx.EVT_BUTTON,self.onShowMain,id=23)
        box.Add(boxa)
        panel.SetSizer(box)
        #box.Fit(self)
        return panel

#---------------------------------------------------------------------------------------------------------
    def d_panelChoices(self):
        panel=wx.Panel(self,-1)
        box=wx.BoxSizer(wx.HORIZONTAL)
        box.Add(wx.Button(panel,25,'Wypozycza'),0)
        box.Add(wx.Button(panel,26,'Oddaje'),0)
        self.Bind(wx.EVT_BUTTON,self.onShowBooksToBorrow,id=25)
        self.Bind(wx.EVT_BUTTON,self.onShowBooksBack,id=26)
        panel.SetSizer(box)

        return panel
#---------------------------------------------------------------------------------------------------------
    def d_panelBooksBorrow(self):
        i=0
        temp=[]
        panel=wx.Panel(self,-1)
        boxa=wx.BoxSizer(wx.VERTICAL)
        for row in bibl().getBooks():
            if (Biblioteka().getBooksState()[i][1]==1):
                temp.append(row[2]+'-'+row[1]+'')
            i+=1
        if not temp:
            boxa.Add(wx.StaticText(panel,label=u"\nNie ma wiecej ksiazek",style=wx.CENTER))
        else:
            cb=wx.ComboBox(panel,pos=(25, 30),choices=temp,style=wx.CB_READONLY)
            cb.Bind(wx.EVT_COMBOBOX, self.setBookID)
            boxa.Add(cb)
        boxx=wx.BoxSizer(wx.HORIZONTAL)
        boxx.Add(wx.Button(panel,28,'OK'),0,wx.EXPAND,5)
        boxx.Add(wx.Button(panel,30,'Powrot'),0,wx.EXPAND,5)
        self.Bind(wx.EVT_BUTTON,self.onSetBorrowBook,id=28)
        boxa.Add(boxx)
        panel.SetSizer(boxa)
        #boxa.Fit(self)
        return panel
#---------------------------------------------------------------------------------------------------------
    def d_panelBooksBack(self):
        i=0
        temp=[]
        uID=self.userID

        panel=wx.Panel(self,-1)
        box=wx.BoxSizer(wx.VERTICAL)
        boxx=wx.BoxSizer(wx.HORIZONTAL)
        for row in bibl().getBooks():
            if(bibl().getBooksState()[i][2]==uID):
                t=row[2]+'-'+row[1]
                temp.append(t)
            i+=1
        if not temp:
            box.Add(wx.StaticText(panel,label=u"\nUzytkownik nic nie wypozyczyl",style=wx.CENTER))
        else:
            cba=wx.ComboBox(panel,pos=(25, 30),choices=temp,style=wx.CB_READONLY)
            cba.Bind(wx.EVT_COMBOBOX, self.setBookID)
            box.Add(cba)
            boxx.Add(wx.Button(panel,29,'OK'),0,wx.EXPAND,5)
            self.Bind(wx.EVT_BUTTON,self.onSetBackBook,id=29)
        boxx.Add(wx.Button(panel,30,'Powrot'),0,wx.EXPAND,5)
        self.Bind(wx.EVT_BUTTON,self.onresetIDs,id=30)
        box.Add(boxx)
        panel.SetSizer(box)
        return panel
#---------------------------------------------------------------------------------------------------------
    def d_panelBorowed(self):
        i=0
        ilosc=0
        users=bibl().getUser()
        panel=wx.Panel(self,-1)
        box=wx.BoxSizer(wx.VERTICAL)
        for row in bibl().getBooksState():
            if(bibl().getBooksState()[i][1]==0):
                ilosc+=1
                i+=1
        ilosc+=1
        gbox=wx.GridSizer(ilosc,3,3,3)

        #gbox.Add(wx.StaticText(panel,label=bibl().getBooks()[0][1]),0,wx.EXPAND,5)


        i=0
        if (ilosc-1>=1):
            box.Add(wx.StaticText(panel,label='Spis wypozyczonch ksiazek'),0,wx.ALIGN_CENTER)
            gbox.Add(wx.StaticText(panel,label='| AUTOR'),0)
            gbox.Add(wx.StaticText(panel,label='| TYTUL'),0)
            gbox.Add(wx.StaticText(panel,label='| KTO?'),0)
            for row in bibl().getBooks():
                if(bibl().getBooksState()[i][1]==0):
                    '''FIXME: przy ponownym uruchomieniu wyrzuca poniższy blad
                    File "C:/Users/Jarek Sroka/OneDrive/Projekty/python/Biblioteka/src/biblgui.py", line 189, in d_panelBorowed
                    gbox.Add(wx.StaticText(panel,label='| '+row[2]),0,wx.EXPAND,5)
                    wx._core.wxAssertionError: C++ assertion "Assert failure" failed at ..\..\src\common\sizer.cpp(1401) in wxGridSizer::DoInsert():
                    too many items (10 > 3*3) in grid sizer (maybe you should omit the number of either rows or columns?)'''
                    gbox.Add(wx.StaticText(panel,label='| '+row[2]),0,wx.EXPAND,5)
                    gbox.Add(wx.StaticText(panel,label='| '+'"'+row[1]+'"'),0)
                    gbox.Add(wx.StaticText(panel,label='| '+users[(bibl().getBooksState()[i][2])-1][1]),0)
                    i+=1
                else:
                    i+=1
        else:
            box.Add(wx.StaticText(panel,label='Nie ma wypozyczonych ksiazek'),0,wx.ALIGN_CENTER)
        box.Add(gbox,0,wx.TOP)
        panel.SetSizer(box)
        box.Add(wx.Button(panel,23,'Powrot'),0,wx.EXPAND,5)

        return panel
#---------------------------------------------------------------------------------------------------------
    def d_panelAddBook(self):
        panel=wx.Panel(self,-1)
        box=wx.BoxSizer(wx.VERTICAL)
        self.tc1=wx.TextCtrl(panel,-1)
        self.tc2=wx.TextCtrl(panel,-1)
        box.Add(wx.StaticText(panel,label="Podaj autora: "),0,wx.ALIGN_CENTER)
        box.Add(self.tc1,0,wx.EXPAND|wx.ALIGN_CENTER,29)
        box.Add(wx.StaticText(panel,label="Podaj nazwe ksiazki: "),0,wx.ALIGN_CENTER)
        box.Add(self.tc2,0,wx.EXPAND|wx.ALIGN_CENTER,29)
        box.Add(wx.Button(panel,34,'Ok'),0,wx.ALIGN_CENTER,5)
        box.Add(wx.Button(panel,23,'Powrot'),0,wx.ALIGN_CENTER,5)
        self.Bind(wx.EVT_BUTTON,self.onAddBook,id=34)
        panel.SetSizer(box)
        return panel
#---------------------------------------------------------------------------------------------------------
    def d_panelAddUser(self):
        panel=wx.Panel(self,-1)
        box=wx.BoxSizer(wx.VERTICAL)
        self.tc3=wx.TextCtrl(panel,-1)
        box.Add(wx.StaticText(panel,label="Podaj imie i nazwisko uzytkownika: "),0,wx.ALIGN_CENTER)
        box.Add(self.tc1,0,wx.EXPAND|wx.ALIGN_CENTER,29)
        box.Add(wx.Button(panel,36,'Ok'),0,wx.ALIGN_CENTER,5)
        box.Add(wx.Button(panel,23,'Powrot'),0,wx.ALIGN_CENTER,5)
        self.Bind(wx.EVT_BUTTON,self.onAddUser,id=36)
        panel.SetSizer(box)
        return panel
#---------------------------------------------------------------------------------------------------------
    def onAddUser(self,event):
        if not self.tc3.GetValue():
            self.onShowAddBad()
            return
        else:
            bibl().addUser(self.tc1.GetValue())
            self.tc3.Clear()
            self.onShowAddGood()
#---------------------------------------------------------------------------------------------------------
    def onAddBook(self,event):
        if not self.tc1.GetValue() or not self.tc2.GetValue():
            self.onShowAddBad()
            return
        else:
            bibl().addBook(self.tc2.GetValue(), self.tc1.GetValue())
            self.tc1.Clear()
            self.tc2.Clear()
            self.onShowAddGood()
#---------------------------------------------------------------------------------------------------------
    def onShowBorrowed(self,event):
        self.SetTitle('Biblioteka::spis wypozyczonych')
        self.panelBorowed.Destroy()
        self.panelBorowed=self.d_panelBorowed()
        self.mainbox.Add(self.panelBorowed,1,wx.CENTER|wx.EXPAND)
        self.onHideAll()
        self.panelBorowed.Show()
        self.Layout()
#---------------------------------------------------------------------------------------------------------
    def onSetBackBook(self,event):
        bibl().resetBooksState(self.bookID)
        self.ShowMessage()
#---------------------------------------------------------------------------------------------------------
    def onSetBorrowBook(self,event):
        bibl().setBooksState(self.userID, self.bookID)
        self.ShowMessageBorrow()
#---------------------------------------------------------------------------------------------------------
    def ShowMessage(self):
        wx.MessageBox('Ksiazka oddana', 'Info',wx.OK | wx.ICON_INFORMATION)
        #self.resetIDs()
        self.panelBooksBack.Destroy()
        self.panelBooksBorrow.Destroy()
        self.panelBooksBorrow=self.d_panelBooksBorrow()
        self.panelBooksBack=self.d_panelBooksBack()
        self.mainbox.Add(self.panelBooksBorrow,1,wx.CENTER|wx.EXPAND)
        self.mainbox.Add(self.panelBooksBack,1,wx.CENTER|wx.EXPAND)
        self.panelBooksBorrow.Hide()
        self.panelBooksBack.Hide()
        self.Layout()

#     def resetIDs(self):
#         self.userID=''
#         self.bookID=''
#         self.data=['Random','Randon']
#---------------------------------------------------------------------------------------------------------
    def ShowMessageBorrow(self):
        wx.MessageBox('Ksiazka zostala wypozyczona', 'Info',wx.OK | wx.ICON_INFORMATION)
#         self.panelBooksBorrow=self.d_panelBooksBorrow()
#         self.panelBooksBack=self.d_panelBooksBack()
#         self.panelBooksBorrow.Hide()
#         self.panelBooksBack.Hide()
        self.Layout()
#---------------------------------------------------------------------------------------------------------
    def onShowAddBad(self):
        wx.MessageBox('Wprowadzone dane sa niepoprawne', 'Info',wx.OK | wx.ICON_INFORMATION)
        self.Layout()
#---------------------------------------------------------------------------------------------------------
    def onShowAddGood(self):
        wx.MessageBox('Dane zostaly wpisane', 'Info',wx.OK | wx.ICON_INFORMATION)
        self.Layout()
#---------------------------------------------------------------------------------------------------------
    def onresetIDs(self,event):
        self.onHideAll()
        self.data=['None','None']
        self.bbooks={}
        self.uuser={}
        self.panelLogIn.Show()
#---------------------------------------------------------------------------------------------------------
    def setBookID(self,e):
        i = e.GetString()
        self.data[1]=i
        self.bookID=bibl().getBookID(i)[0]
#---------------------------------------------------------------------------------------------------------
    def setUID(self,e):
        i = e.GetString()
        self.data[0]=i
        self.userID=bibl().getUserID(i)[0]
#---------------------------------------------------------------------------------------------------------
    def onShowChoices(self,event):
        self.SetTitle("Panel: "+self.data[0])
        self.onHideAll()
        self.panelBooksBack.Destroy()
        self.panelBooksBorrow.Destroy()
        self.panelBooksBorrow=self.d_panelBooksBorrow()
        self.panelBooksBack=self.d_panelBooksBack()
        self.mainbox.Add(self.panelBooksBorrow,1,wx.CENTER|wx.EXPAND)
        self.mainbox.Add(self.panelBooksBack,1,wx.CENTER|wx.EXPAND)
        self.panelBooksBorrow.Hide()
        self.panelBooksBack.Hide()
        self.panelChoices.Show()
        self.SetSizer(self.mainbox)


        self.Layout()
#---------------------------------------------------------------------------------------------------------
    def onShowMain(self,event):
        self.SetTitle('Biblioteka::glowne okno')
        self.onHideAll()
        self.panelMain.Show()
        self.Layout()
#---------------------------------------------------------------------------------------------------------
    def onShowBooksToBorrow(self,event):
        self.panelBooksBack.Hide()
        self.panelBooksBorrow.Show()
        self.Layout()
#---------------------------------------------------------------------------------------------------------
    def onShowBooksBack(self,event):
        self.panelBooksBorrow.Hide()
        self.panelBooksBack.Show()
        self.Layout()
#---------------------------------------------------------------------------------------------------------
    def onShowLogIn(self,event):
        self.SetTitle('Biblioteka::zaloguj')
        self.panelLogIn.Destroy()
        self.panelLogIn=self.d_panelLogIn()
        self.mainbox.Add(self.panelLogIn,1,wx.CENTER|wx.EXPAND)
        self.onHideAll()
        self.panelLogIn.Show()
        self.Layout()
#---------------------------------------------------------------------------------------------------------
    def onShowAddBook(self,event):
        self.onHideAll()
        self.panelAddBook.Show()
        self.Layout()
#---------------------------------------------------------------------------------------------------------
    def onShowAddUser(self,event):
        self.onHideAll()
        self.panelAddUser.Show()
        self.Layout()
#---------------------------------------------------------------------------------------------------------
    def onHideAll(self):
        self.panelMain.Hide()
        self.panelLogIn.Hide()
        self.panelChoices.Hide()
        self.panelBooksBorrow.Hide()
        self.panelBooksBack.Hide()
        self.panelBorowed.Hide()
        self.panelAddBook.Hide()
        self.panelAddUser.Hide()
#---------------------------------------------------------------------------------------------------------
    def onClose(self,event):
        self.Close()
##########################################################################################################
if __name__ == '__main__':
    app = wx.App(False)
    frame = MainWindow().Show()
    app.MainLoop()
