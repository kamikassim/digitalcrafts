class Balloon(object):
    def __init__(self, color, size, shape):
        self.color = color
        self.size = size
        self.shape = shape
        self.inflated = False 
        self.working = True
    
    def inflate(self):
        self.inflated = True

    def explode(self):
        self.inflated = False
        print "BANG!"

bigBalloon = Balloon()
smallBalloon = Balloon('blue', 'small', 'square')

class BigBalloon(Balloon):
    def __init__(self, color, shape)
        super(Balloon, self).__init__(color, 'Big', shape)

        