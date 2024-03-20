def compression(s):
    compressed_string = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed_string += s[i - 1] + str(count)
            count = 1
    compressed_string += s[-1] + str(count)
    return compressed_string

def decompression(s):
    decompressed_string = ""
    i = 0
    while i < len(s):
        char = s[i]
        count = int(s[i + 1])
        decompressed_string += char * count
        i += 2
    return decompressed_string

str_input = input("Enter string : ")

compressed_string = compression(str_input)
decompressed_string = decompression(compressed_string)
print(f"String : {str_input}, Compressed String : {compressed_string}, Decompressed String: {decompressed_string}")