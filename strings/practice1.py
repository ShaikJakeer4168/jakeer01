#program1:Vowels and Consonants
def program1():
    name = input("Enter your name: ")
    v = 0
    c = 0
    for i in name:
        if i in "aeiou":
            v += 1
        else:
                c += 1
    print("Number of vowels:", v)
    print("Number of consonants:")


#program2:no.of charecters
def program2():
    str1 = "Jakeer"
    print(len(str1))  


    
#program3:reverse a string 
def program3():
    s = input("Enter a string:")
    print(s[::-1])    

#program4:polindram
def program4():
    a = input("Enter a string:")
    temp = a 
    b = a[::-1]
    if temp == b:
        print("Given string is a polindram")
    else:
        print("Given string is not a polindram")



                    


   
