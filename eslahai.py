                                            ##  In The Name Of "Yegane Codnevise AAlame Hasti"  ##


# input Cipher Text
# Output Key




# Create Dictionaries to Store the Mappings
alphabet_dict = {
'a' : 0,'b' : 1,'c' : 2,'d' : 3,'e' : 4,'f' : 5,'g' : 6,'h' : 7,'i' : 8,'j' : 9,
'k' : 10,'l' : 11,'m' : 12,'n' : 13,'o' : 14,'p' : 15,'q' : 16,'r' : 17,'s' : 18,
't' : 19,'u' : 20,'v' : 21,'w' : 22,'x' : 23,'y' : 24,'z': 25
                 }


numb_dic = {
0 : 'a',1 : 'b',2 : 'c',3 : 'd',4 : 'e',5 : 'f',6 : 'g',7 : 'h',8 : 'i',9 : 'j',
10 : 'k',11 : 'l',12 : 'm',13 : 'n',14 : 'o',15 : 'p',16 : 'q',17 : 'r',18 : 's',
19 : 't',20 : 'u',21 : 'v',22 : 'w',23 : 'x',24 : 'y',25 : 'z'
    }


# Remove Spaces from Text
def removeSpaces(text): 
    text = text.lower()                       
    text = text.replace(" ","")
    return text


def enc(plainText, key): 
    key = list(key)                             #horoofe key ro besoorate list darmiare
    if len(plainText) == len(key): 
        return(key) 
    else: 
        for i in range(len(plainText) -len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key))                      #inja tabee join horof ro  bedune fasele("") beham michasbune


#This Function Encrypts a Message 
def encrypt(plainText, key):
    plainText=removeSpaces(plainText) 
    key=enc(plainText, key)
    cipherText = [] 
    for i in range(len(plainText)): 
        x = (alphabet_dict[plainText[i]] + alphabet_dict[key[i]]) % 26
        cipherText.append(numb_dic[x]) 
    return("" . join(cipherText))


#This Function Decrypts the Message
def decrypt(cipherText, key):
    cipherText = removeSpaces(cipherText) #inja be in niazi nadarim ama tabeesh ro neveshtim jaie dige niaz bud daghigh bashe
    key = enc(cipherText, key)
    plain_Text =''
    for i in range(len(cipherText)):
        x = (alphabet_dict[cipherText[i]] - alphabet_dict[key[i]] + 26) % 26
        plain_Text += numb_dic[x]
    return plain_Text


#Calculate the Index of Coincidence
def index_of_coincidence(cipherText):
    freq = [0] * 26
    n = 0
    for letter in cipherText:
        if letter.isalpha():
            freq[ord(letter.lower()) - ord('a')] += 1
            n += 1
    ic = 0.0
    for letter_freq in freq:
        ic += letter_freq * (letter_freq - 1)
    if n > 1:
        ic /= n * (n - 1)
    else:
        ic = 0.0
    return ic

def calLenthOfKey(cipherText):
    # Calculating the lengh of the key
    pass


def calKey(cipherText, keyLenght):
    # Calculating the key
    pass













name = input ("Please Enter Your Name :")
print('Hello ',name ,'   :))')
plainText = input("Please Insert The plainText :")
key = input("Please Insert The Key :")
cipherText = encrypt(plainText, key) 
print("Encrypted message:", cipherText)
print("Decrypted message:", decrypt(cipherText, key)) 
ic = index_of_coincidence(cipherText)
print("Index of Coincidence is : ",ic)


print("ساپس داتسا میتسه نوتتامحز نادردق ")