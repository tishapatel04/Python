#Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match. Your task is simple. Given a string, you need to tell if it is a lapindrome.
# TISHA PATEL 20CE106 
#https://github.com/tishapatel04/Python.git



import collections;
testCases = int(input())
while testCases:        
    testCases -= 1
    string = input()        
    halve = len(string) // 2    
    if len(string) % 2 == 0:      
        if sorted(string[:halve]) == sorted(string[halve:]):  
            print('YES')
        else:                                
            print('NO')
    else:                            
        if sorted(string[:halve]) == sorted(string[halve + 1:]):   
            print('YES')
        else:
            print('NO')