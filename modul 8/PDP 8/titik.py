import math
P={}
def MakePoint(x,y,T):
    global P
    P[T+"absis"]=x
    P[T+"ordinat"]=y
    return P
def GetAbsis(T):
    return P[T+"absis"]
def GetOrdinat(T):
    return P[T+"ordinat"]
def SetOrdinat(newy,T):
    global P
    P[T+"ordinat"]=newy
    return P[T+"ordinat"]
def SetAbsis(newx,T):
    global P
    P[T+"absis"]=newx
    return P[T+"absis"]
def BacaTulis():
    p1=MakePoint(2.0,2.0,"1")
    p2=MakePoint(-2.0,2.0,"2")
    p3=MakePoint(2.0,-2.0,"3")
    p4=MakePoint(-2.0,-2.0,"4")
    print("P1: ({},{})".format(p1["1absis"],p1["1ordinat"]))
    print("P2: ({},{})".format(p2["2absis"],p2["2ordinat"]))
    print("P3: ({},{})".format(p3["3absis"],p3["3ordinat"]))
    print("P4: ({},{})".format(p4["4absis"],p4["4ordinat"]))
def AddP(x1,y1,x2,y2):
    return x1+x1,y1+y2
def MinP(x1,y1,x2,y2):
    return x1-x2,y1-y2
def MulDot(x1,y1,x2,y2):
    return x1*x2,y1*y2
def IsEqual(x1,y1,x2,y2):
    return x1==x2 and y1==y2
def IsNotEqual(x1,y1,x2,y2):
    return x1!=x2 and y1!=y2
def IsLess(x1,y1,x2,y2):
    return x1+y1<x2+y2
def IsGreater(x1,y1,x2,y2):
    return x1+y1>x2+y2
def IsOrigin(x,y):
    return x==0 and y==0
def IsOnSbX(x):
    return x==0
def IsOnSbY(y):
    return y==0
def Kuadran(x,y):
    if x>0 and y>0:
        return "1"
    elif x<0 and y>0:
        return "2"
    elif x>0 and y<0:
        return "4"
    elif x<0 and y<0:
        return "3"
    else:
        return "Titik berada pada sumbu x,y atau 0,0"
def NextX(x,T):
    global P
    P[T+"absis"]=x+1
    return P[T+"absis"]
def NextY(y,T):
    global P
    P[T+"ordinat"]=y+1
    return P[T+"ordinat"]
def PlusDelta(x,y,deltax,deltay,T):
    global P
    P[T+"absis"]=x+deltax
    P[T+"ordinat"]=y+deltay
    return P[T+"absis"],P[T+"ordinat"]
def MirrorOf(x,y,sb,T):
    global P
    if sb=="SbX":
        P[T+"ordinat"]=(-1)*y
        return x,P[T+"ordinat"]
    elif sb=="SbY":
        P[T+"absis"]=(-1)*x
        return P[T+"absis"],y
def JarakPst(x,y):
    return "{:.2f}".format(math.sqrt((x**2)+(y**2)))
def Jarak2T(x1,y1,x2,y2):
    return "{:.2f}".format(math.sqrt((x2-x1)**2)+((y2-y1)**2))
def Geser(x,y,deltax,deltay,T):
    global P
    P[T+"absis"]=x+deltax
    P[T+"ordinat"]=y+deltay
    return P[T+"absis"],P[T+"ordinat"]
def GeserSbX(x,deltax,T):
    global P
    P[T+"absis"]=x+deltax
    return P[T+"absis"]
def GeserSby(y,deltay,T):
    global P
    P[T+"ordinat"]=y+deltay
    return P[T+"ordinat"]
def MirrorP(x,y,sb,T):
    global P
    if sb=="SbX":
        P[T+"ordinat"]=(-1)*y
        return x,P[T+"ordinat"]
    elif sb=="SbY":
        P[T+"absis"]=(-1)*x
        return P[T+"absis"],y
def Putar(x,y,sudut):
    return (math.cos(sudut)*x)+(math.sin(sudut)*y),((-1)*math.sin(sudut)*x)+(math.cos(sudut)*y)
