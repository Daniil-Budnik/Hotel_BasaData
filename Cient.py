class Client():
    #установка типов
    __UnicID = int
    __surname = str
    __name = str
    __secondname = str
    __passdate = str
    __comment = str
    def __init__(self, UnicID, surname, name, secondname, passdate,comment):
        self.setUID(UnicID)    
        self.setSurname(surname)
        self.setName(name)
        self.setSname(secondname)
        self.setPassdate(passdate)
        self.setComment(comment)
    #методы set-get
    def setUID(self, value): self.__UnicID = value
    def setSurname(self, value): self.__surname = value
    def setName(self, value): self.__name = value
    def setSname(self, value): self.__secondname = value
    def setPassdate(self, value): self.__passdate = value
    def setComment(self, value): self.__comment = value

    def getUID(self): return self.__UnicID
    def getSurname(self): return self.__surname
    def getName(self): return self.__name
    def getSname(self): return self.__secondname
    def getPassDate(self): return self.__passdate
    def getComment(self): return self.__comment

    def __str__(self):
        return ( "Id: {}\nФамиля: {}\nИмя: {}\nОтчество: {}\nПаспортные данные: {}\nПримечание: {} ".format(
            self.__UnicID, self.__surname, self.__name, self.__secondname, self.__passdate,self.__comment))