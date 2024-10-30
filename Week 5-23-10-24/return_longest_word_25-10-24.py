list=[]
size=int(input("enter number of words :"))
for i in range(size):
    words=input(f"Enter word {i+1}:")
    list.append(words)
longest_word=max(list,key=len)
print("word list :",list)
print("longest word :",longest_word)
print("Length of longest word:",len(longest_word))

