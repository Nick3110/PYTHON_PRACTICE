x='what_is_this._how_are_you?_what_to_do?_wow!!'
# length of string
print(len(x))
# slicing of string 
print(x[:8])# it will print all alnum and special charachter till  7th index as indexing start from zero and range is exclusive
print(x[::]) # it will print whole string coz. interpreter takes argument as 0 to end
# stepping in string
print(x[0:30:2])# it will print every second charatcher of string
# Negative slicing
print(x[:-7]) # actually it will interprete it as len(x)-7 i.e 0 to len(x)-7
print(x[:len(x)-7]) # above and this both will be same

print(x[-23:-5])# working is same len(x)-23 to len(x)-5 i.e 21 to 39 
print(x[21:39]) #now above and this will same



