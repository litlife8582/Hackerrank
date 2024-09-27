def swap_case(s):
    word=""
    for i in range(0,len(s)+1,1):
        if (s(i).isupper() == True):
            word+=s(i).upper()
    return word

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)