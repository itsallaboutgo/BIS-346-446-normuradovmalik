def display_tablet(lst):
    print("\t",end="")
    for i in range(len(lst[0])):
        print(i+1,end="\t")
        print()
        
        for i in range(len(lst)):
            print(i+1,end="\t")
            for col in lst[i]:
                print(col,end="\t")
            print()
            