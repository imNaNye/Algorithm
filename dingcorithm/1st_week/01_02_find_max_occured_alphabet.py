def result(string):
    char_dic = {}

    for char in string:
        if char.isalpha():
            if char in char_dic:
                char_dic[char] += 1
            else:
                char_dic[char] = 1

    max_char = max(char_dic, key=char_dic.get)
    return max_char


print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))