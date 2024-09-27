def swap_case(s):
    word=""
    i=0
    while(i<len(s)):
        if s[i].isupper():
            word+=s[i].lower()
        else:
            word+=s[i].upper()
        i+=1
    return word

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)