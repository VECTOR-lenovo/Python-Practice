set1= {10,20,30,40,50}
set2= {30,40,50,60,70}
set3= { 10,20,30}


def ques_a(a):
    print(f"The legth of set1 is {len(a)}")
ques_a(set1)

def ques_b(b):
    print(f"The sum of set2 is {sum(b)}")
ques_b(set2)    

def ques_c(set1,set2,set3):
    print(f"The union of all the sets are: {set1 | set2| set3}")
ques_c(set1,set2,set3)    

def ques_d(set1,set2,set3):
    print(f"The intersection of all the sets are: {set1 & set2& set3}")
ques_d(set1,set2,set3)

def ques_e(set1,set2):
    print(f"Set1 - Set2:{set1 - set2}")
ques_e(set1,set2)    

def ques_f(set2,set3):
    print(f"Set2 - Set3:{set2 - set3}")
ques_f(set2,set3)

def ques_g(set1,set2,set3):
    print(f"set3 is the subset of set1 and set2:{set3.issubset(set1), set3.issubset(set2)}")
ques_g(set1,set2,set3)

def ques_h(set1):
    set_universal=set()
    for i in range(1,51):
        set_universal.add(i)
    print(f"The complement of set1 :{set_universal-set1}") 
ques_h(set1)   


def ques_i(set1):
    for i in set1:
        if i==15:
            print(True)
        else:
            print(False)
            break
ques_i(set1)      

def ques_j(set1):
    new_set = set1
    new_set.add(60)
    return new_set
print(f" First set with 60 added: {ques_j(set1)}")

def ques_k(set2):
    set2.discard(60)
    return set2
print(f"Second set with 60 removed: {ques_k(set2)}")


def ques_l(set3):
    set3.clear()
    return set3
print(f"Set3 after removing all elements: {ques_l(set3)}")


def ques_m(set2):
    print(f"The maximum value in set2 is: {max(set2)}")
    print(f"The minimum value in set2 is: {min(set2)}")
ques_m(set2)