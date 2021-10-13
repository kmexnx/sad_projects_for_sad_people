import random;

list = [];

for i in range(0,100):
    list.append(random.randint(10,101));

list.sort();

print(list);
middle = int(len(list) / 2);
a = list[middle]
for i in list:
    
    if(list[middle] <= 33):
        middle = middle + 1;
        break
    else:
        middle = middle - 1;

if(list[middle - 1] != 33):
    print('Not found, 404');
else:
    print('Found number:', list[middle - 1] , 'at index:' , middle - 1 );