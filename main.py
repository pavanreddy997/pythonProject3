word = input("enter your word:")
print("original string ", word)
size=len(word)
print("printing only even index characters")
for i in range(0,size-1,3):
 print("index[",i,"]",word[i])