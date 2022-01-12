alphabets_ = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i', 10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q', 18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y', 26:'z'}
alphabets = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
test_msg = "The quick brown fox jumps over the lazy dog"
def encrypt(msg, shift=0):
    msg_ = ""
    for i in range(len(msg)):
        temp = alphabets[msg[i]] + shift
        if temp > 26:
            temp = temp - 26
        if temp <= 0:
            temp = temp + 26
        temp = alphabets_[temp]
        msg_ = msg_ + temp
    return msg_


msg = input("Enter the message to be encrypted (without spaces): ").lower()
try:
    shift = int(input("Enter the number of positions to shift: "))
except ValueError:
    shift = 0

encrypted_msg = encrypt(msg, shift)
print("This is the encrypted msg:",encrypted_msg)