will=input("are you willing for corona test: ")
if will=="yes":
    print("ok, lets start")
    tem=float(input("your body temperature: "))
    if tem<100:
        print ("your body temperature is normal")
        
    if tem>=100 and tem<105:
        print("you have fever")
        
    if tem >=105:
        print("you have high chance of corona")
        
    print("answer the following questions with yes or no")
    sym1=input("you have dry cough: ")
    sym2=input("you have tiredness: ")
    sym3=input("you have difficulty breathing or shortness of breath: ")
    
    if sym1=="yes" and sym2=="yes" and sym3=="yes" and tem <100:
        print("positive")
        
    if sym1=="yes" and sym2=="yes" and sym3=="no" and tem <100:
        print("negative")
        
    if sym1=="yes" and sym2=="no" and sym3=="yes" and tem <100:
        print("negative")
        
    if sym1=="no" and sym2=="yes" and sym3=="yes" and tem <100:
        print("negative")
        
    if sym1=="yes" and sym2=="no" and sym3=="no" and tem <100:
        print("negative")
        
    if sym1=="no" and sym2=="yes" and sym3=="no" and tem <100:
        print("negative")
        
    if sym1=="no" and sym2=="no" and sym3=="yes" and tem <100:
        print("negative")
        
    if sym1=="no" and sym2=="no" and sym3=="no" and tem <100:
        print("negative")
        
        
        
    if sym1=="yes" and sym2=="yes" and sym3=="yes" and tem >=105:
        print("positive")
        
    if sym1=="yes" and sym2=="yes" and sym3=="no" and tem >=105:
        print("positive")
        
    if sym1=="yes" and sym2=="no" and sym3=="yes" and tem >=105:
        print("positive")
        
    if sym1=="no" and sym2=="yes" and sym3=="yes" and tem >=105:
        print("positive")
        
    if sym1=="yes" and sym2=="no" and sym3=="no" and tem >=105:
        print("negative")
        
    if sym1=="no" and sym2=="yes" and sym3=="no" and tem >=105:
        print("negative")
        
    if sym1=="no" and sym2=="no" and sym3=="yes" and tem >=105:
        print("positive")
        
    if sym1=="no" and sym2=="no" and sym3=="no" and tem >=105:
        print("negative")
        
        
        
        
    if sym1=="yes" and sym2=="yes" and sym3=="yes" and tem>=100 and tem<105:
        print("positive")
        
    if sym1=="yes" and sym2=="yes" and sym3=="no" and tem>=100 and tem<105:
        print("positive")
        
    if sym1=="yes" and sym2=="no" and sym3=="yes" and tem>=100 and tem<105:
        print("positive")
        
    if sym1=="no" and sym2=="yes" and sym3=="yes" and tem>=100 and tem<105:
        print("positive")
        
    if sym1=="yes" and sym2=="no" and sym3=="no" and tem>=100 and tem<105:
        print("negative")
        
    if sym1=="no" and sym2=="yes" and sym3=="no" and tem>=100 and tem<105:
        print("negative")
        
    if sym1=="no" and sym2=="no" and sym3=="yes" and tem>=100 and tem<105:
        print("positive")
        
    if sym1=="no" and sym2=="no" and sym3=="no" and tem>=100 and tem<105:
        print("negative")
        
if will=="no":
    print("ok, have a nice day")
