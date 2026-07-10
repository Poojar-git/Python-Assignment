def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        sub_string=string[i:i+k]
        result=""
        for ch in sub_string:
            if ch not in result:
                result+=ch
        print(result)