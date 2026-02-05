from pathlib import Path
import json

class NegetiveError(Exception):
    def __init__(self,args = "its cannot be negetive"):
        super().__init__(args)
class Beace :
    def __init__(self):
        self.path = Path("account.json")
        if not self.path.exists():
            self.path.write_text("[]",encoding="utf-8")
        self.transactions_path = Path("transactions.json")
        if not self.transactions_path.exists():
            self.transactions_path.write_text("[]", encoding="utf-8")


        

        self.account = {}

    def menue(self):
        menue_action = {
            "1" : self.new_account,
            "2" : self.deposit,
            "3":self.withdraw,
            "4":self.show_account,
            "5":self.exit}
        print("wellcome to future bank!")
        print("="*50)
        print("our services:")
        print("1.new account")
        print("2.deposit to other account")
        print("3.withdrawn from account")
        print("4.show the account")
        print("5.exit")
        bank = input("what do you want?").strip()
        
        selected= menue_action.get(bank,0)
        if selected:
            selected()
        else:
            print("Invalid choice")
    def new_account(self):
        accounts = json.loads(self.path.read_text(encoding="utf-8"))
        self.make_account = {}
        
        self.name = input("your full name: ").strip().title()
        self.id = input("your id: ").strip()
        self.amount = 0
        import passwords
        
        

        self.password = passwords.last_password
        print(f"your password{self.password}")
        self.make_account ={"name" :self.name,
                       "id": self.id,
                       "amount": self.amount,
                       "password": self.password
                       }
        if self.id in [acc["id"] for acc in accounts]:
            print("this id used befor")
        
        accounts.append(self.make_account)
        self.path.write_text(json.dumps(accounts,indent=4),encoding="utf-8")
        print(f"making account for{self.name} secsusfully")
    def deposit(self):
        self.type = "deposit"
        self.name=input('what is your name?')
        self.id1=input("what is your id?")
        self.id2=input("recipient id?")
        self.recipinet = input("recipinets name?")
        self.amounts = int( input("how many dollor you whant to deposit?"))
        accounts = json.loads(self.path.read_text(encoding="utf-8"))
        
        if self.amounts <= 0:
            raise NegetiveError ()
        
        
        found1,found2 = False,False
        
        for acc in accounts:
            if acc["id"] == self.id1 :
               found1= True
               send = acc
               
            
               
        for acc in accounts:
            if acc["id"] == self.id2:
               found2= True
               recive = acc
               
               
               
        if found1 and found2:
            if send["amount"]< self.amounts:
                raise ValueError("its cannot be more than amount")
            
            else:
                send["amount"] -= self.amounts
                recive["amount"] += self.amounts

            self.path.write_text(json.dumps(accounts,indent=4),encoding="utf-8")
            print("deposited {self.amount} to {self.recipinet} from {self.name}")
            new_transection = {
                "depositor" : self.id1,
                "recipinet" : self.id2,
                "type" : self.type,
                "amount" : self.amounts
            }
            transactions = json.loads(self.transactions_path.read_text(encoding="utf-8"))
            transactions.append(new_transection)
            self.transactions_path.write_text(json.dumps(transactions,indent=4), encoding="utf-8")

        else:
            print("invaid ids")
    def withdraw(self):
        self.type = "withdraw"
        self.name=input('what is your name?')
        self.id1=input("what is your id?")
        self.password = input("what is your password?")
        self.amounts = int( input("how many dollor you whant to withdraw?"))
        accounts = json.loads(self.path.read_text(encoding="utf-8"))
        if self.amounts <= 0:
            raise NegetiveError()
        
             
        found1= False
        found2 = False
        found3 = False
        you = None

        for acc in accounts:
            if acc["id"] ==self.id1 :
                you = acc
                found1 = True
            if not you:
                raise ValueError("wrong id")
                
            if you["password"] == self.password :
                found2 = True
            if you["amount"]>= self.amounts:
                found3 = True
        if found1 and found2 and found3:
            you["amount"] -= self.amounts
            self.path.write_text(json.dumps(accounts,indent=4),encoding="utf-8")
            print(f"withdraw {self.amounts} dollor from {self.name} account")
            new_transaction = {
                "depositor" : self.id1,
                
                "type" : self.type,
                
                "withdraw" : self.amounts,
                "remainder" : you["amount"]
            }
            transactions = json.loads(self.transactions_path.read_text(encoding="utf-8"))
            transactions.append(new_transaction)
            self.transactions_path.write_text(json.dumps(transactions,indent=4), encoding="utf-8")
        elif  not found1 :
            raise ValueError("your id is not true")
        elif not found2:
            raise ValueError("your password is not true")
        elif not found3 :
            raise ValueError("your amount is not inough")
        else:
            print("unknown problem!")
    def show_account(self):
         accounts = json.loads(self.path.read_text(encoding="utf-8"))
         your_id = input("what is your id?")
         found = False
         for acc in accounts:
             
             if acc["id"] == your_id:
                 found = True
                 lala = acc
                 break
         if found:
             
             print(f"name : {lala["name"]}")
             print(f"id : {lala["id"]}") 
             print(f"amount : {lala["amount"]}")
             
             star = "*" * 12
             print(f"password : {star}")
         else:
             print("your id is not true or maybe you dont have an account")
    def exit (self):
        print("finish")
        return



                 
             





        

            
        
        
        


        

