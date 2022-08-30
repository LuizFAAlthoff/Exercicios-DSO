class Ordenacao():

    def __init__(self, array_para_ordenar:[]):
        self.__array = array_para_ordenar

    def ordena(self):
        for g in range(len(self.__array)-1):
            for i in range(len(self.__array)-1):
                if self.__array[i] > self.__array[i+1]:
                    self.__array[i], self.__array[i+1] = self.__array[i+1], self.__array[i]
        return self.__array

    def toString(self):
        string = ""
        for h in range(len(self.__array)):
            string += str(self.__array[h]) + ","
        string = string[:-1]
        return string
