"""crating a  point of 3 dimensional """
class point:
    def __init__(self,x,y,z):
        """" this is the doc string for initializer method """
        self.x=x
        self.y=y
        self.z=z

    def printpoint(self):
        'this is the doc string for printing values for 3-D coordinate sytem point'
        print(self.x,self.y,self.z)

p1=point(1,2,3)
p1.printpoint()
print(__doc__)