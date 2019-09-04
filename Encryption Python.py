#This is the list for the alphabet,the encrypted alphabet, and the counter that tells the encrypted list which letter to use.
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
encrypted_alphabet=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
counter=0
is_letter=0


#Asks the user for the letter
letter=input("enter your first letter")

#Figures out the letter and what to make it
if is_letter==0:
    for i in range(26):
        if letter==alphabet[i]:
            is_letter==1
            counter=i
            
#This prints out the encrypted letter
print(encrypted_alphabet[counter])




