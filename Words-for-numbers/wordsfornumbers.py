import sys

ONES = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]  
TEENS = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]  
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]  

def convert_to_words(num):  
    if num == 0:  
        return "zero"  
    elif num< 0:  
            return "minus " + convert_to_words(abs(num))  
    elif num< 10:  
            return ONES[num]  
    elif num< 20:  
            return TEENS[num - 10]  
    elif num< 100:  
            return TENS[num // 10] + ("-" + convert_to_words(num % 10) if num % 10 != 0 else "") 
    


for line in sys.stdin:
    a = line.split()
    for i,k in enumerate(a):
        if k.isdigit():
            a[i]=convert_to_words(int(k))
    for i in a:
        print(i, end=" ")
        
    print()