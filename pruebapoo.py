class carro():
    
    def __init__(self,name):
        self.nombre = name
    
    def acelerar(self):
        print("estoy acelerando")
    
    def transportar(self,per):
        print("estoy transpotando",per,"personas",self.nombre)
        
bmw01 = carro("bmw01") #crea el objeto
bmw01.acelerar()
bmw01.transportar(5)

mazda01 = carro("mazda01")
mazda01.transportar(3)
mazda01.transportar(6)
mazda01.transportar(36)
mazda01.transportar(63)