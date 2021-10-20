class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height= height
    def setWidth(self, width):
        self.width = width
    def setHeight(self, height):
        self.height = height
    def getWidth(self):
        return self.width
    def getHeight(self):
        return self.height
    def area(self):
        return self.width*self.height
    def __str__(self):
        my_str = "Width: " + str(self.width)+"\n"+ "Height: " + str(self.height)+"\n"+ "Area: "+str(self.area())+"\n"
        # area 함수를 내부에선 어떻게 쓰느냐 => self.area() 이케 쓴다 !!!!!
        return my_str
r1 = Rectangle(4)
r2 = Rectangle(3,5)
print(r1)
print(r2)
    
    