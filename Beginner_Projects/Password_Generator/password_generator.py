import random

digits="1234567890"
lower="abcdefghijklmnopqrstuvwxyz"
upper=lower.upper()
special="!@#$%&*()+-/"
everything=digits+lower+upper+special


def generate_password(r=10):        #default length of password is set to 10
    r=r-4
    temp_p="" 

    # one character from all types:
    temp_p=temp_p + random.choice(digits)
    temp_p=temp_p + random.choice(lower)
    temp_p=temp_p + random.choice(upper)
    temp_p=temp_p + random.choice(special)
    # remaining 
    for i in range(0,r):
        temp_p=temp_p+random.choice(everything)
    
    list1=list(temp_p)      # conveting to list because random.shuffle(list) only takes list
    random.shuffle(list1)   # list is shuffled to make no pattern is generated
    password=''.join(list1) # join() method provides a flexible way to create strings from iterable objects. 
    
    return password

#Driver Code--------------------------------------------
# default length is set to 10 but this number can also be taken from user
password = generate_password()
print("Generated Password: ",password)