def check_equals(lst1, lst2):
    return lst1 == lst2
l1 = list(map(int,input("-> ").split()))
l2 = list(map(int,input("-> ").split()))
print(check_equals(l1,l2))