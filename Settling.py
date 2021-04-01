import Cient as Cl
import Hroom as rm

class Settling():
    
    # Установка типов
    __dateIn = str
    __client = Cl.Client
    __room = rm.HRoom
    __dateOut = str
    __note = str
    def __init__(self,client,room,dateIn,dateOut,note):
        self.setClient(client)    
        self.setRoom(room)
        self.setDateIn(dateIn)
        self.setDateOut(dateOut)
        self.setNote(note)

    # Методы set-get
    def setClient(self, value): self.__client = value
    def setRoom(self, value): self.__room = value
    def setDateIn(self, value): self.__dateIn = value
    def setDateOut(self, value): self.__dateOut = value
    def setNote(self, value): self.__note = value
    


    def getClien(self): return self.__client
    def getRoom(self): return self.__room
    def getDateIn(self): return self.__dateIn
    def getSateOut(self): return self.__dateOut
    def getSetNote(self): return self.__note

        
    def __str__(self):
        return ( "Клиент: {}\nКомната: {}\nДатаВъезда: {}\nДатаОтъезда: {}\nПримечание: {} ".format(
            self.__client, self.__room, self.__dateIn, self.__dateOut,self.__note) )
