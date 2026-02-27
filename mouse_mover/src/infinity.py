import time
import win32api, win32con
import math

weight = 50

choochoo=.01
push = 500
pie=math.pi
sqish=100

pie_multiplied=int(pie*sqish)
half_pie_multiplied=int(pie_multiplied*.5)
threehalves_pie_multiplied=half_pie_multiplied*3
two_pie_multiplied=2*pie_multiplied

def generate_magic():
    magic=[]
    
    # horizontal
    holdoff = []
    holdon = []
    for i in range(two_pie_multiplied):
       pepperoni= ( (i+push ),
                  (math.sin(i/sqish)*weight).__round__()+push)
                    
       if pepperoni not in holdoff:
        holdoff.append(pepperoni)
    
        pepperoni= ( (i+push ),
                    -(math.sin(i/sqish)*weight).__round__()+push)
        if pepperoni not in holdon:
            holdon.append(pepperoni)
    holdon.reverse()
    
    holdup = []
    holdown = []
    for i in range(pie_multiplied):
        pepperoni= int(math.sin(i/sqish)+holdon[0][0])          
        holdup.append(pepperoni)
        
        pepperoni= int(-math.sin(i/sqish)+holdon[len(holdon)-1][0])
        holdown.append(pepperoni)
    
    for i in range(half_pie_multiplied):        
        holdoff[i]=(int(
            holdoff[i][0]*(i/half_pie_multiplied)
            +holdown[half_pie_multiplied+i]*(1-2*i/pie_multiplied)),
                  holdoff[i][1])
        holdon[i]=(int(
            holdon[i][0]*(i/half_pie_multiplied)
            +holdup[half_pie_multiplied+i]*(1-2*i/pie_multiplied)),
                  holdon[i][1])
    
    for i in range(threehalves_pie_multiplied,two_pie_multiplied):      
        holdoff[i]=(int(
            holdoff[i][0]*(1-(i-threehalves_pie_multiplied)/half_pie_multiplied)
           +holdup [i-threehalves_pie_multiplied]*((i-threehalves_pie_multiplied)/half_pie_multiplied)),
                holdoff[i][1])
        
        holdon[i]=(int(
            holdon[i][0]*(1-(i-threehalves_pie_multiplied)/half_pie_multiplied)
           +holdown [i-threehalves_pie_multiplied]*((i-threehalves_pie_multiplied)/half_pie_multiplied)),
                holdon[i][1])
        
    magic.extend(holdon)
    magic.extend(holdoff)
    
   
    i=1
    while i<len(magic):
        if math.dist(magic[i],magic[i-1])>1.42:
            magic.insert(i,((magic[i][0]+magic[i-1][0])//2,(magic[i][1]+magic[i-1][1])//2))
            i+=1
        else: i+=1
        
    pancake = magic[-1]
    try:
        for i in range(0,len(magic)):
            if magic[i] == pancake:
                magic.pop(i)
                i-=1
            else: pancake = magic[i]
    except IndexError: pass
    
    return magic

magic=generate_magic()
        
class Wabbula():
    def __init__(self):
        self.prev_pos = win32api.GetCursorPos()
        self.pos = win32api.GetCursorPos()
        self.index = 0
       
    def next_pos(self):
        if self.index == len(magic)-1:
            self.index = 0
        else:
            self.index += 1
        win32api.mouse_event(win32con.MOUSE_MOVED,0,1,0,0)
        return magic[self.index]
    
    def get_pos(self):
        self.pos = win32api.GetCursorPos()
        return self.pos
    
    def set_pos(self):
        if  math.dist(self.prev_pos,self.get_pos())<10:
            win32api.SetCursorPos(self.next_pos())
            self.prev_pos = self.get_pos()
        else: return False
        time.sleep(choochoo)
        return True
    
    def dubdub(self):
        while self.set_pos():
            pass

bu=Wabbula()
bu.dubdub()