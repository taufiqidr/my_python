if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    if n<2 or n>10:
        quit()
    list_arr=[]
    
    for a in arr:
        if a>100 or a<-100:
            quit()
        else:
            list_arr.append(a)    
    
    idx = list_arr.index(max(list_arr))
    popped_item=list_arr.pop(idx)
    for i in range(len(list_arr)):
        if popped_item == max(list_arr):
            idx = list_arr.index(max(list_arr))
            popped_item=list_arr.pop(idx)
        else:
            break
    
    print (max(list_arr))
    # while popped_item == max(list_arr):
    #     popped_item=list_arr.pop(idx)
    #     if popped_item != max(list_arr):
    #         print (max(list_arr))
    #         break
            
    