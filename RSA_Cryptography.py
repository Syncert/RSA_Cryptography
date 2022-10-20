#RSA Cryptography Script

#TO-DO make this input-based instead of static variables :)

#euclidean algorithm to find d
def extendedEuclideanAlgorithm(a, b):
    if a == 0:
        return b, 0, 1
    gcd, u, v = extendedEuclideanAlgorithm( b % a, a)
    x = v - (b // a) * u
    y = u
    return gcd, x, y


#dictionary of alphabetical encodings

characters_dict = {
    'a' : '01',
    'b' : '02',
    'c' : '03',
    'd' : '04',
    'e' : '05',
    'f' : '06',
    'g' : '07',
    'h' : '08',
    'i' : '09',
    'j' : '10',
    'k' : '11',
    'l' : '12',
    'm' : '13', 
    'n' : '14',
    'o' : '15',
    'p' : '16',
    'q' : '17',
    'r' : '18',
    's' : '19',
    't' : '20',
    'u' : '21',
    'v' : '22',
    'w' : '23',
    'x' : '24',
    'y' : '25',
    'z' : '26',
    ' ' : '32',
}


#prime number p
p = 3
#prime number q
q = 11
#public key
e = 3

#print(extendedEuclideanAlgorithm(p, q))
#TO - DO : CODE ALGORITHM TO FIND D
#private key
d = 7
#n in encryption equation
N = p * q

#encryption
# c = m^e mod N 

def encrypt(char):
    c = characters_dict.get(char.lower())
    c = int(c)
    val = pow(c,e) % N 
    #convert to string with leading values
    #i.e 01 instead of 1
    val = str(val).zfill(2)
    return val

#decryption
# m = c^d mod N

def decrypt(char):
    #m = list(characters_dict.keys())[list(characters_dict.values()).index(char.lower())]
    val = pow(int(char),d) % N
    val = str(val).zfill(2)
    val = list(characters_dict.keys())[list(characters_dict.values()).index(val)]
    return val


#decryption!!!
decryption_string = "03 32 18 09 21 05 31 32 03 14 32 03 05 14 31 24 03 28 14 03 05 13 32 14 17 01 14 32 14 17 26 24 26 32 01 24 26 32 27 09 19 04 12 26 30 32 23 01 16 28 32 14 09 32 28 26 27 24 26 14 12 16 32 27 09 19 19 21 05 03 27 01 14 26"
decryption_list = decryption_string.split(' ')
print(decryption_list)

print('Decrypting')
print()
print_list = []
for i in decryption_list:

    print_list.append(decrypt(i))
print(print_list)


#upper and lowercase the same, treat character inputs with lower function

encrypt_phrase = input("Please input the phrase to encode and encrypt")

print("Encoding and Encrypting Phrase")
print(encrypt_phrase)
print()

counter = 1
#create list of encrypted digits

print("ENCODING")
print()
#loop over string, print decryption
for i in encrypt_phrase:
    #print(i)
    print(str(counter) +  ": Char '" + i + "' = " + str(characters_dict.get(i.lower())))
    #increment counter
    counter += 1

#reset counter
counter = 1
#line break
print()

#create list to store encrypted values
#TO DO, make it possible to manually add to encryption list
encrypted_list = []

print("ENCRYPTING")
print()
#loop over string, print encryption
for i in encrypt_phrase:
    print(str(counter) + ": Char'" + i + "' = " + str(encrypt(i)))
    counter += 1
    #ADD ENCRYPTED ITEM TO LIST FOR DECRYPTION
    encrypted_list.append(encrypt(i))

print()
print("Encrypted Message")
print(encrypted_list)

print_list = []
for i in encrypted_list:
    print_list.append(decrypt(i))
print(print_list)