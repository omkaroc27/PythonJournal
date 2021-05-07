
series_range=int(input("upto which number you want a series ?"))
f0=0
f1=1
 
print("series is :")
print(f0)
print(f1)
for i in range(0,series_range):
                    f2=f0+f1
                    f0=f1
                    f1=f2
                    print(f2)