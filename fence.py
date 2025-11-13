def fence_encrypt(text : str):
    text = text.lower()
    text = text.replace(' ', '')
    even = odd = ""
    for i in range(0, len(text)):
        if i % 2 == 0:
            even += text[i]
        else:
            odd += text[i]
    return even + odd



print(fence_encrypt("abcde"))


def fence_decrypt(text : str):
    text = text.lower()
    text = text.replace(' ', '')
    if len(text) % 2 == 0:
        even = text[0:len(text) // 2]
        odd = text[len(text) // 2:]
    else:
        even = text[0:len(text) // 2 + 1]
        odd = text[len(text) // 2 + 1:]
    decrypted = ""
    for i in range(0, len(text)):
        if i % 2 == 0:
            decrypted += even[0]
            even = even[1:]
        else:
            decrypted += odd[0]
            odd = odd[1:]
    return decrypted



#bonjour mami
print(fence_encrypt("bonjour mami"))
print(fence_decrypt(fence_encrypt("bonjour mami")))

