import Hroom as rom
import Cient as cl
import Settling as sl

Clients = [
        cl.Client(1,"Аллаева","Алла","Пугачёва","222333443","поёт ну такое себе"),
        cl.Client(2,"Хабиб","Нуза","розембаун","576839322","вчера забрал у меня  5 рублей:("),
        cl.Client(3,"Мурмагамед","Соня","Филеевна","89678678","Вернула 5 рублей Нузы") 
        ]

rooms = [
    rom.HRoom(3,2,'lux',2033),
    rom.HRoom(1,1,'midle',5),
    rom.HRoom(2,5,'obsh',1)
    ]

setlings = [
    sl.Settling(Clients[1],rooms[2],'22.02.2002','-',"не хочет съезжать собака"),
    sl.Settling(Clients[0],rooms[2],'21.12.2021','-',"новенькая"),
    sl.Settling(Clients[2],rooms[0],'22.09.2019','26.09.2019',"бысто он") ]

print("\nКлиенты:\n")
for ITEM in Clients: print(ITEM,'\n')
    
print("\nКомнаты:\n")
for ITEM in rooms: print(ITEM,'\n')
    
print("\nПоселение:\n")
for ITEM in setlings: print(ITEM,'\n')
