class HRoom():
    
    # Установка типов
    __room = int
    __capacity = int
    __lcomfort = str
    __cost = int
    def __init__(self, room, capacity, lcomfort,cost):
        self.setRoom(room)    
        self.setCapacity(capacity)
        self.setLcomfort(lcomfort)
        self.setCost(cost)

    #методы set-get
    def setRoom(self, value): self.__room = value
    def setCapacity(self, value): self.__capacity = value
    def setLcomfort(self, value): self.__lcomfort = value
    def setCost(self, value): self.__cost = value


    def getRoom(self): return self.__room
    def getCapacity(self): return self.__capacity
    def getLcomfort(self): return self.__lcomfort
    def getCost(self): return self.__cost

    def __str__(self):
        return ("Комната: {}\nВместимость: {}\nУровеньКомфорта: {}\nЦена: {} ".format(
            self.__room, self.__capacity, self.__lcomfort, self.__cost))
