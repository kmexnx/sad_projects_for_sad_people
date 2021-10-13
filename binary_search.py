import random;

def binaryStupidSearch(length, magicNumber):

    list = [];

    for i in range(0,length):
        list.append(random.randint(10,length));

    list.sort();

    print(list);
    middle = int(len(list) / 2);
    for i in list:
        
        if(list[middle] <= magicNumber):
            middle = middle + 1;
            break
        else:
            middle = middle - 1;

    if(list[middle - 1] != magicNumber):
        print('Not found, 404');
    else:
        print('Found number:', list[middle - 1] , 'at index:' , middle - 1 );


binaryStupidSearch(100000, 333)
