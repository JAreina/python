import threading
import time

class Proceso(threading.Thread):
    def run(self):
        print("{} Inicia SELF :: {}".format(self.getName(),self))
        time.sleep(1)
        print("{} fin , SELF __ {}".format(self.getName(),self))



if __name__=="__main__": #programa main
    for a in range(0,10):

        p1 = Proceso(name = "proceso__{}".format(a+1))
        p1.start()
        time.sleep(.5)

