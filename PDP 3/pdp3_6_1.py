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

    print("Output No.1 :")
    andv[0] = f1(t,t)
    andv[1] = f1(t,f)
    andv[2] = f1(f,t)
    andv[3] = f1(f,f)
    output(andv)
#\n buat enter
    print("\nOutput No.2 :")
    andv[0] = f2(t,t)
    andv[1] = f2(t,f)
    andv[2] = f2(f,t)
    andv[3] = f2(f,f)
    output(andv)

    print("\nOoutput No.3 :")
    andv[0] = f3(t)
    andv[1] = f3(f)
    andv[2] = f3(t)
    andv[3] = f3(f)
    output(andv)

    print("\nOutput No.4 :")
    andv[0] = f4(t)
    andv[1] = f4(f)
    andv[2] = f4(t)
    andv[3] = f4(f)
    output(andv)

    print("\nOutput No.5 :")
    andv[0] = f5(t,t)
    andv[1] = f5(t,f)
    andv[2] = f5(f,t)
    andv[3] = f5(f,f)
    output(andv)

    print("\nOutput No.6 :")
    andv[0] = f6(t,t)
    andv[1] = f6(t,f)
    andv[2] = f6(f,t)
    andv[3] = f6(f,f)
    output(andv)

    print("\nOutput No.7 :")
    andv[0] = f7(t,t)
    andv[1] = f7(t,f)
    andv[2] = f7(f,t)
    andv[3] = f7(f,f)
    output(andv)

    print("\nOutput No.8 :")
    andv[0] = f8(t,t)
    andv[1] = f8(t,f)
    andv[2] = f8(f,t)
    andv[3] = f8(f,f)
    output(andv)

    print("\nOutput No.9 :")
    andv[0] = f9(t,t)
    andv[1] = f9(t,f)
    andv[2] = f9(f,t)
    andv[3] = f9(f,f)
    output(andv)
if __name__ == '__main__':
	main()