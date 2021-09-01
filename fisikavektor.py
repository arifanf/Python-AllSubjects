def main():
    print("\n1. Vp = (15i+14j-16k)")
    print("   Va = (18i-25j+24k)")

    i1=15
    j1=14
    k1=-16

    i2=18
    j2=-25
    k2=24

    ai=i1+i2
    bj=j1+j2
    ck=k1+k2

    di=i1-i2
    ej=j1-j2
    fk=k1-k2

    print("\n   a. Vp + Va = (15i+14j-16k)+(18i-25j+24k)")
    print("              = {}i{}j+{}k".format(ai,bj,ck))
    print("   b. Vp - Va = (15i+14j-16k)-(18i-25j+24k)")
    print("	      = {}i+{}j{}k".format(di,ej,fk))

    print("\n2. m = 100kg")
    print("   v = (15i+60j-2k)m/s")

    i3=15
    j3=60
    k3=-2
    m=100

    ii=i3*m
    jj=j3*m
    kk=k3*m

    print("\n   m . v = {}i+{}j{}k".format(ii,jj,kk))



if __name__ =='__main__':
    main()
