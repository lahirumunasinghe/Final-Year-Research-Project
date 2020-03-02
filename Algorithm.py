import numpy as np

verp = [0, 0, 0, 0, 2, 3, 5, 34, 23, 45, 56, 34, 12, 5, 0, 0,0, 6, 10, 24, 45, 65, 23, 10, 4, 0, 0, 0, 0, 0, 0]
lfg = [[0 for col in range(2)] for row in range(20)]

skip =0
inline1 = 1
start1 = 0
end =0
j1 = 0
def zerocount( array,indexkey ):
    num0 = 0
    lenth =len(array)
    for i in range ( indexkey ,lenth-1):
        if( array[i] == 0):
            num0= num0+1
        else:
            break
    return num0

i1 =0
while(i1 <len(verp )):
    if (verp[i1] == 0 and zerocount( verp, i1 ) >2 and inline1 == 1): # Enter the text area from the blank area

        start1 = i1 +zerocount( verp, i1 ) # record starting line split point
        inline1 = 0
        print ("awa" ,i1+ zerocount( verp, i1 ))
        i1 = i1 + zerocount( verp, i1 )


    elif (verp[i1] == 0 and inline1 == 0 and zerocount( verp, i1 ) >2):  # Enter the blank area from the text area

        end = i1
        print ("awa end" ,i1-1)
        i1 = i1 + zerocount( verp, i1 )-1
        print ("awa start" ,i1)
        # Save line split position
        # lfg[j1][1] = i1 - 14
        # j1 = j1 + 1



    i1 =i1 +1




