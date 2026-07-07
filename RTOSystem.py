import random,string,sqlite3

conn=sqlite3.connect("Registration list.db")
cur=conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS Registration (
    NumPlate TEXT PRIMARY KEY,
    Name TEXT,
    Mobile INTEGER,
    Company TEXT,
    Type TEXT,
    Aadhar INTEGER,
    Address TEXT,
    Total INTEGER
)""")

def NumPlateChecker(Number):
    cur.execute("""
    SELECT * FROM Registration
    WHERE NumPLate = ?
    """,(Number,))
    if cur.fetchone(): # return cur.fetchone() is None
        return False
    else:
        return True

def Record(NumPlate,Name,Mobile,Company,Type,Aadhar,Address,Total):
    cur.execute("""
    INSERT INTO Registration
    (NumPlate,Name,Mobile,Company,Type,Aadhar,Address,Total)
    VALUES (?,?,?,?,?,?,?,?)
    """,(NumPlate,Name,Mobile,Company,Type,Aadhar,Address,Total))
    conn.commit()
def NumGen(Sp):
    while True:
        Number=""
        for i in range(2):
            Number+=random.choice(string.ascii_uppercase)
        if Number == "GV":
            continue
        else:
            if Sp==1:
                lis=["0000","0001","1111","0007","7777","9999"]
                W=input("If you want to choose special number from list type y or press Enter to get the special number randomly ")
                if W=="y":
                    print(lis)
                    C=input("select from given option ")
                    if C in lis:
                        Number+=C
                        if NumPlateChecker(Number):
                            return Number
                        else:
                            continue
                    else:
                        print("Please select from given option only")
                        continue
                else:
                    r=random.randrange(len(lis))
                    Number+=lis[r]
                    if NumPlateChecker(Number):
                        return Number
                    else:
                        continue
            else:
                Plate=""
                for i in range(4):
                    Plate+=str(random.randrange(0,10))
                Number+=Plate
                if NumPlateChecker(Number):
                    return Number
                else:
                    continue

def Details(Roadtax,Reg,NumPlatecharge,Permit,Other,SpecNum):
    Name=input("Write the name of Owner ")
    Mobile=int(input("Write the mobile number "))
    Company=input("Write the company name of the vehicle ")
    Type=input("Write the name of vehicle\nexample:Bus ")
    Aadhar=int(input("Write your Aadhar number "))
    Address=input("Write your Address ")
    Price=int(input("Write the price of the vehicle "))
    Total=0
    Total=int(Roadtax*Price*0.01 + Reg + NumPlatecharge + Permit + Other + SpecNum)
    if SpecNum==0:            # NumPlate = NumGen(Sp=1 if SpecNum else 0)
        NumPlate=NumGen(Sp=0)
    else:
        NumPlate=NumGen(Sp=1)
    Record(NumPlate,Name,Mobile,Company,Type,Aadhar,Address,Total)
    return Total,NumPlate
def Money(Sn):
    while True:
        Category=input("select\nCategory a:Truck,Bus\nCateogy b:Car,pickup\nCategory c:e-rickshaw,Bike,Rickshaw ")
        if Category=="a":
            A=input("you are applying in category a y/n ")
            if A=="n":
                continue
            else:
                if Sn==1:
                    D1,NumPlate=Details(12,5000,1500,2000,1000,2000000)
                else:
                    D1,NumPlate=Details(12,5000,1500,2000,1000,0)
            return D1,NumPlate
        elif Category=="b":
            B=input("you are applying in category b y/n ")
            if B=="n":
                continue
            else:
                if Sn==1:
                    D2,NumPlate=Details(10,3000,1000,1500,1000,2500000)
                else:
                    D2,NumPlate=Details(10,3000,1000,1500,1000,0)
            return D2,NumPlate
        elif Category=="c":
            C=input("you are applying in category c y/n ")
            if C=="n":
                continue
            else:
                if Sn==1:
                    D3,NumPlate=Details(6,1000,800,500,400,1000000)
                else:
                    D3,NumPlate=Details(6,1000,800,500,400,0)
            return D3,NumPlate
        else:
            print("Please select from given option")
            continue
print("Welcome to RTO Management System")
a=input("Do you want to apply for New Numbers,Special Numbers,search for Owner Details y/n ")
if a=="n":
    print("exit")
    exit()
else:
    while True:
        c=int(input("select\n1:New Number\n2:Special Number\n3:Owner Details\n4:Update\n5:Delete\n6:Exit "))
        if c==1:
            N=input("Do you want to apply for New Number y/n ")
            if N=="n":
                continue
            else:
                D,NumPlate=Money(Sn=0)
                print(f"Total Cost {D}\nYour Number is {NumPlate}")
        elif c==2:
            S=input("Do you want to apply for Special Number y/n ")
            if S=="n":
                continue
            else:
                D,NumPlate=Money(Sn=1)
                print(f"Total Cost {D}\nYour Number is {NumPlate}")
        elif c==3:
            F=input("Write the numberplate to find the Details ")
            cur.execute("""
            SELECT * FROM Registration
            WHERE NumPlate=?
            """,(F,))
            data=cur.fetchall()
            if data:
                for row in data:
                    print(row)
            else:
                print("No Data found")
conn.commit()   
conn.close()       
