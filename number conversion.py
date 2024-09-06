print("\n\n\t\tMENU\n1.Decimal to Binary number\n2.Binary to Decimal\n3.decimal to octal\n4.Decimal to hexa decimal")
ch=int (input("enter your choice:"))
if(ch==1):
        dec=int(input("enter a decimal number"))
        c=bin(dec)
        print(dec,"in decimal=",c," in binary")
elif(ch==2):
        n=input("Enter the binary number")
        dec=0
        for i in n:
            dec=dec*2+int(i)
        print(n,"in binary=",dec,"in bnary")
elif(ch==3):
         dec=int(input("enter a decimal number"))
         c=oct(dec)
         print(dec,"in decimal=",c," in octail")
elif(ch==4):
          dec=int(input("enter a decimal number"))
          c=hex(dec)
          print(dec,"in decimal=",c," in hexadecimal")
else:
    print("invalid choice")
          
