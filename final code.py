def encodeString(word, index, rand_num):
    if index == len(word):
        return word
    c = chr(ord('a') + (ord(word[index])-ord('a') + rand_num)%26)
    print(c)
    word = word[:index] + c + word[index+1:]
    return encodeString(word, index+1, rand_num)

word = "atef"
#ID = int(input())
rand_num = 5
print(encodeString(word, 0, rand_num))

