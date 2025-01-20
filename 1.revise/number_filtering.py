def list_filtering(lst):
    new_list = []
    for l in lst:
        if l%2 == 0:    
            new_list.append(l)
    return new_list

n = int(input ("how many numbers do you want in your list? "))

lst = []

for i in range(n):
    lst.append(int(input("enter a number:")))

primary_number = list_filtering(lst)
print(primary_number)