
#this program is about conversion of dcimal no into a binary no
def dec_to_binary(ip):
    try :
        dec = int(ip)
        binno = []
        #All the magic begins here
        while dec!=0:
            rem=dec%2
            binno.append(rem)
            dec=int(dec/2)
            #List(reversed(list_name) is use for reverse the list)
        print("Binary no for ",ip,"is",list(reversed(binno)))
    except :
        #Error message for the users
        print("You did not entered a valid value Please try again")

#this program is for performing binary to decimal conversion
def binary_to_dec(ip):
    deci=0
    data=[]
    ip = str(ip)
    length= len(ip)
    try :
        #Logic for converting n_bit no into a single no or single bit no
        for nos in range(length):
            integers=int(ip[nos])
            #Storing all the single bit into a single variable or list
            data.append(integers)
        i=0
        deci=0
        #All the magics begin here
        for nos in range(len(data)-1,-1,-1):
            if data[nos]not in {0,1}:
                print("Enter a valid binary no")
                break
            else :
                i=(len(data)-1)-nos
                deci=deci+((data[nos]*2)**i) #Logic for binary to decimal conversion
        if deci>0:
            print("Dcimal equivelent no of ",data,"is",deci)
        else :
            print("For given no ",data,"operation can't perform PLEASE TRY AGAIN")
            
    except :
        print("You did not entered a valid value PLEASE ENTER BINBARY NO CAREFULLY")
        
        
# THis function is for converting decimal no into octal no
def dec_to_octal(ip):
    data=[]
    try :
        dec=int(ip)
        while dec!=0:
            rem=dec%8
            data.append(rem)
            dec=int(dec/8)
    except :
        print("Enter a valid decimal value carefully");
    print("Octal conversion of decimal no ",ip,"is",list(reversed(data)))
#%%
