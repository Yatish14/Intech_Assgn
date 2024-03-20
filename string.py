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

def optimized_compression(s):
   optimized_string = ""
   tempChar = ""
   tempNum = 0
   k = 0
   for i in range(0,len(s)):
        if i < k:
            continue
        if s[i].isalpha():
            tempChar = s[i]
        elif s[i].isdigit():
            currentNum = 0
            for j in range(i,len(s)):
                if s[j].isdigit():
                    currentNum = currentNum*10 + int(s[j])
                else:
                    if currentNum == tempNum or tempNum == 0:
                        optimized_string += tempChar
                        tempNum = currentNum
                    else:
                        optimized_string += str(tempNum) + tempChar
                        tempNum = currentNum
                    k = j
                    break
                if j == len(s) - 1:
                    if currentNum == tempNum or tempNum == 0:
                        optimized_string += tempChar + str(currentNum)
                    else:
                        optimized_string += str(tempNum) + tempChar + str(currentNum)
                    k = len(s) + 1

   return optimized_string

def decompression(s):
    decompressed_string = ""
    tempChar = ""
    k = 0
    for i in range(0,len(s)):
        if i < k:
            continue
        if s[i].isalpha():
            tempChar += s[i]
        elif s[i].isdigit():
            currentNum = 0
            for j in range(i,len(s)):
                if s[j].isdigit():
                    currentNum = currentNum*10 + int(s[j])
                else:
                    for c in tempChar:
                        decompressed_string += c * currentNum
                    tempChar = ""
                    k = j
                    break
                if j == len(s) - 1:
                    for c in tempChar:
                        decompressed_string += c * currentNum
                    k = len(s) + 1

    return decompressed_string

str_input = input("Enter string : ")

compressed_string = compression(str_input)
opt_Str = optimized_compression(compressed_string)
decompressed_string = decompression(opt_Str)
print(f"String : {str_input}, Compressed String : {compressed_string}, Optimised String: {opt_Str}, Decompressed String: {decompressed_string}")