if __name__ == '__main__':
    arr = map(int, input().split())
    score=list(arr)
    final=set(score)
    final_list=list(final)
    final_list.sort(reverse=True)
    print(final_list[(1)])
