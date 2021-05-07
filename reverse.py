 
n=int(input("Enter number:"))
temp=n
rev=0
String_number =str(temp) 
sum=rev=0 

while(n>0):
    dig=n%10
    rev=rev*10+dig
    rem = n % 10
    sum=sum+rem
    n=n//10
print("the sum is ",sum)
       
if(temp==rev):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")


