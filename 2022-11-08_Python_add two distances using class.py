#Python Program
# Python  add two distances using class
#Computer Programming Tutor, 08 Nov 2022

class Distance:
    def GetDistance(self):
        self.__cm=int(input("Enter CM:"))
        self.__m=int(input("Enter M:"))
        self.__km=int(input("Enter KM:"))


    def PutDistance(self):
        print(self.__km,self.__m,self.__cm)

    def __add__(self,T):
        dist = Distance()
        dist.__cm=self.__cm+T.__cm
        dist.__m=self.__m+T.__m
        dist.__km = self.__km+T.__km
        dist.__m =dist.__m +(dist.__cm//100)
        dist.__cm =dist.__cm%100
        dist.__km=dist.__km+(dist.__m//1000)
        dist.__m=dist.__m%1000
        return dist

dist1 = Distance()
dist2 = Distance()
print("Enter First Distance:")
dist1.GetDistance()
print("Enter Second Distance:")
dist2.GetDistance()

dist3 = dist1 + dist2

print("The Sum of Both Distances is:")
dist3.PutDistance()





        
