#This is the list for the alphabet,the encrypted alphabet, and the counter that tells the encrypted list which letter to use.
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
encrypted_alphabet=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
counter=0
is_letter=0
encrypted_word = []

#Asks the user for the letter
base_word = input("Enter your first word: ")

#Figures out the letter and what to make it
word = [letter for letter in base_word]
print(word)


for x in range(len(word)):
    encrypted_word.append(encrypted_alphabet[alphabet.index(word[x])])

print(encrypted_word)