alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ']
encrypted_alphabet = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m', ' ']

encrypted_word = []
finalword = ''

base_word = input("Enter what you want to encrypt: ")
base_word = base_word.lower()

word = [letter for letter in base_word]

for x in range(len(word)):
    encrypted_word.append(encrypted_alphabet[alphabet.index(word[x])])

print(finalword.join(encrypted_word))
