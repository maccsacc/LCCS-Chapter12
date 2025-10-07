#Question_16_A_HL
#Enter your name here: Daniel

s = 0
sentList = []
digitList = [48,49,50,51,52,53,54,55,56,57] #(iii) oh my god please forgive me huw. finding all the unicode code for every digit and letter 
consList = [97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122]
wordList = ["",]
sentence = input("Please enter a sentence: ")
sentence2 = sentence.lower() #(ii) creating a lowercase version of the sentence
count1 = 0
count2 = 0
print("The number of s's was:", sentence.count("s")) #(i) Using the string.count() function to count the s's in the sentence
print("Your lowercase sentence is:", sentence2) #(ii) printing the lowercase sentence
print("The number of vowels was:", sentence.count("a")+sentence.count("e")+sentence.count("i")+sentence.count("o")+sentence.count("u")) #(ii) counting the vowels in the sentence
sentList.extend(sentence2)#(iii) creating a list of every character in the string
for i in sentList: #(iii) evaluating every character to be either a digit or character
    if digitList.count(ord(i)) == 1:
        count1 += 1
    elif consList.count(ord(i)) == 1:
        count2 += 1

print("The number of letters was", count2) #(iii) printing the output
print("The number of digits was", count1)
wordList.extend(sentence2)
numWord = wordList.count(" ") #(iv) Counting the number of spaces and then adding 1 to get the number of words
print("The number of words was:", numWord+1)

