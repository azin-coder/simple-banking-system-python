import string
import secrets

length = 12
    
lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
special = string.punctuation
password = [] 
password.append(secrets.choice(lower))
password.append(secrets.choice(upper))
password.append(secrets.choice(numbers))
password.append(secrets.choice(special))
all_chart = lower + upper + numbers + special
while len(password)<length:
    password.append(secrets.choice(all_chart))
secrets.SystemRandom().shuffle(password)  
last_password = "" .join(password) 
print("your password : ",last_password)

    
           