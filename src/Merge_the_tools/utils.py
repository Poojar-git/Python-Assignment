def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        sub_string=string[i:i+k]
        result=set(sub_string)
    return result
    