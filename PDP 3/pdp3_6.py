from sys import argv

def f1(p,q):
    a1=p and q
    return a1
def f2(p,q):
    a2=not (p and q)
    return a2
def f3(p):
    a3=not p
    return a3
def f4(q):
    a4=not q
    return a4
def f5(p,q):
    a5=p or (not q)
    return a5
def f6(p,q):
    a6=not(p and q)
    return a6
def f7(p,q):
    a7=not(p or q)
    return a7
def f8(p,q):
    if p==q:
        a8=False
    else:
        a8=True
    return a8
def f9(p,q):
    if p==q:
        a9=True
    else:
        a9=False
    return a9

def output(h):
    print("T | T = {}".format(h[0]))
    print("T | F = {}".format(h[1]))
    print("F | T = {}".format(h[2]))
    print("F | F = {}".format(h[3]))

def main():
    t = True
    f = False
    andv=[0,0,0,0]

    print("output 1 :")
    andv[0] = f1(t,t)
    andv[1] = f1(t,f)
    andv[2] = f1(f,t)
    andv[3] = f1(f,f)

    print("output 1 :")
    andv[0] = f2(t,t)
    andv[1] = f2(t,f)
    andv[2] = f2(f,t)
    andv[3] = f2(f,f)

    print("output 1 :")
    andv[0] = f3(t,t)
    andv[1] = f3(t,f)
    andv[2] = f3(f,t)
    andv[3] = f3(f,f)

    print("output 2 :")
    andv[0] = f4(t,t)
    andv[1] = f4(t,f)
    andv[2] = f4(f,t)
    andv[3] = f4(f,f)

    print("output 3 :")
    andv[0] = f5(t,t)
    andv[1] = f5(t,f)
    andv[2] = f5(f,t)
    andv[3] = f5(f,f)

    print("output 4 :")
    andv[0] = f1(t,t)
    andv[1] = f1(t,f)
    andv[2] = f1(f,t)
    andv[3] = f1(f,f)

    print("output 5 :")
    andv[0] = f1(t,t)
    andv[1] = f1(t,f)
    andv[2] = f1(f,t)
    andv[3] = f1(f,f)

    print("output 6 :")
    andv[0] = f1(t,t)
    andv[1] = f1(t,f)
    andv[2] = f1(f,t)
    andv[3] = f1(f,f)

    print("output 7 :")
    andv[0] = f1(t,t)
    andv[1] = f1(t,f)
    andv[2] = f1(f,t)
    andv[3] = f1(f,f)

    print("output 8 :")
    andv[0] = f1(t,t)
    andv[1] = f1(t,f)
    andv[2] = f1(f,t)
    andv[3] = f1(f,f)

    print("output 9 :")
    andv[0] = f1(t,t)
    andv[1] = f1(t,f)
    andv[2] = f1(f,t)
    andv[3] = f1(f,f)

if __name__ == '__main__':
	main()