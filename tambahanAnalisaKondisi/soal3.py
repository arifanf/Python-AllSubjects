def main():
    n=list(map(int, input("Masukkan 3 nilai integer : ").split(",")))
    c=abs(n[0]-n[1])
    b=abs(n[0]-n[2])
    if c>=2 or b>=2:
        if abs(n[1]-n[2])>=2:
            print("True")
        else:
            print("False")
    else:
        print("False")
if _name_ == '_main_':
    main()