print("Please enter the character with which you want to start")

character = chr(input())

print("Please enter the number of rows")

n = int(input())

#for i in range(0, n):

#   for j in range(69 - i, 70):

  #      a = chr(j)

   #     print(a, end="")

    #print()

for i in range(1,n+1):

    for j in range (1,i+1):

        print(chr(ord(character)-i+j), end="")

    print()

