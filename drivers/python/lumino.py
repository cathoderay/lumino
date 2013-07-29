import serial


class Lumino:
    def __init__(self, interface):
        self.interface = interface
        self.source = serial.Serial(interface, 9600)

    def get(self):
        while True:
            try:
               values = self.source.readline().strip().split(' ')
               if len(values) == 2:
                   return values
            except Exception, e:
                print e

    def geta(self):
        return int(self.get()[0])

    def getb(self):
        return int(self.get()[1])


if __name__ == '__main__':
    interface = "/dev/ttyUSB0" 
    l = Lumino(interface)
    while True:
        try:
            print l.get(), l.geta(), l.getb()
        except KeyboardInterrupt:
            "Thanks for trying Lumino, ;)"
