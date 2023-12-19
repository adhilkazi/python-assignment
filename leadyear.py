year=int(input("enter year"))

if (year % 4 ==0) and (year % 100 !=0):
     print("{0} this the leadyear".format(year))
      
else:
    print("{0} this is not".format(year))
