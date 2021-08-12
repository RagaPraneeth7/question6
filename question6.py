n=int(input())                          # read input n
for i in range(n):                      # for each in in range between 0 and n
   a,b,c=map(int,input().split(" "))    # raed inputs of number of cats and dogsand legs
   c1=a+b
   c2=c1*4
   if(c1==2 and c%4==0):                #if c1 satisfies the condition print yes
      print("yes")
   elif(c1==1 and c%4==0):              # else if condition satisfies print no
      print("yes")
   else:                                # else print no
      print("no")