#You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']

# Length of the list
l = len(heros)
print(l)
#Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)

#3. You realize that you need to add 'black panther' after 'hulk',
#   so remove it from the list first and then add it after 'hulk'

for i in range (len(heros)):
    if heros[i] == 'hulk':
        heros.insert(i+1,'blankpanther')
        i+=1

heros.pop(len(heros)-1)
print(heros)

heros[1:3]=['doctor strange']
print(heros)

heros = [re.replace('thor','doctor strange') for re in heros]  
for i in heros:
    if i == 'hulk':
        heros.remove('hulk')
print(heros)


heros = sorted(heros)
print(heros)
