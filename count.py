def count_substring(string, sub_string):
    start=count=0
    while True:#loop continues indefinitely until explicitly broken off
        start=string.find(sub_string,start)+1# .find() starts searching for the substring from the 'start'-index
        if(start>0):
            count+=1
        else:#when no more substirng is availble in the string the .find() returns -1 hence start is -1+1=0
            return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()#.strip() removes leading and trailing spaces
    
    count = count_substring(string, sub_string)
    print(count)