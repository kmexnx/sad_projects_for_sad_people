import random;

def binaryStupidSearch(length, magicNumber):

    list = [];

    for i in range(0,length):
        list.append(random.randint(1,length));

    list.sort();
    print('List of random and sorted Numbers:',list);
    middle = int(len(list) / 2);
    for i in list:
        if(list[middle] == magicNumber):
            a = list[middle];
            break;
        if(list[middle] < magicNumber):
            middle = middle + 1;
            a = list[middle];
        else:
            middle = middle - 1;
            a = list[middle];

    if(a != magicNumber):
        print('Not found, 404');
    else:
        print('Found number:', magicNumber , 'at index:' , middle + 1);
 

listSize = input("Enter the length of the list: ");
criteria = input("Enter a number to find: ");

binaryStupidSearch(int(listSize), int(criteria));
