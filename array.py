# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

list1 = [ 
{'1' : 2200,
'2' : 2350,
'3' : 2600,
'4' : 2130,
'5' : 2190}
]
# In Feb, how many dollars you spent extra compare to January?
print ("expnditure spent in feb more than jan :")
print(list1[0]['2']-list1[0]['1'])

#Find out your total expense in first quarter (first three months) of the year.
print(list1[0]['1']+list1[0]['2']+list1[0]['3'])

for i in list1:
    for key in i:
        if i[key] == 2000:
            print("i spent exactly 2000")
        
        
#June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

list1[0]['6'] = 1980
print(list1)

#update +200 in April

list1[0]['4'] = list1[0]['4'] + 200
print(list1)