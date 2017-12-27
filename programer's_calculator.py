
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
                
    except :
        #Error message for the users
        print("You did not entered a valid value Please try again")
    #List(reversed(list_name) is use for reverse the list)
    strdata=""
    binno = list(reversed(binno))  
    for no in range(len(binno)):
        string=str(binno[no])
        strdata=strdata+string
    print("Binary no for ",ip,"is",strdata)
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
        
        #All the magics begin here
        for nos in range(len(data)-1,-1,-1):
            if data[nos]not in {0,1}:
                print("Enter a valid binary no")
                deci=0
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
        data=list(reversed(data))
        strdata=""
        for no in range(len(data)):
            string=str(data[no])
            strdata=strdata+string
        print("Octal conversion of decimal no ",ip,"is",strdata)
    except :
        print("Enter a valid decimal value carefully");
   


def octal_to_decimal(ip):
    data=[]
    octal=0
    try :
        ip=str(ip)
        length=len(ip)
        for nos in range(length):
            data1=int(ip[nos])
            data.append(data1)
        for no in range(length-1,-1,-1):
            if data[no] not in {0,1,2,3,4,5,6,7}:
                print("Entered no. is not an octal no Please try again")
                octal=0
                break
            else :
                i=(length-1)-no
                octal=octal+(data[no]*(8**i))
        if octal>0 :
            print("Decimal equivelent no of ",ip,"is : ",octal)
        else :
            print("Operation can not be purform for no ",ip)
            
    except :
        print("You have not entered a valid value Please enter a valid octal no")
        
#%%
stri=""+"yadav"
stri=stri+"name"
print(stri)