import re
#Check if the string starts with "The" and ends with "Spain":
with open("BranchPredictor.py", 'r') as file:
    filedata = file.read()
finaltag = ".*#btbentries$"
value = re.split("\n",filedata)
array1 = []
#print(value)
for i in range (0,len(value)):
    #print(" loop " + str(i))

    #print(value[i])
    t = re.match(finaltag, value[i])
    if t is None:
        if i == 61:
            print (value[i])

    else :
        #print(t.group())
        array1.append(t.group())
    #print(array1)

    #print(t)
#print(" this is the array value ",array1)
variable = re.split("[0-9]",array1[0])
#print(" this is the variable value ",variable)



variable [1] = 42069   # dont use single digit values 2 digits to any other digits work fine




#print(re.findall('\n    BTBEntries = Param.Unsigned(1000, "Number of BTB entries")#btbentries\n',filedata) , " this is the match query")
#print(array1[0])
#print(variable[0] + str(variable[1]) + variable[len(variable)-1])

#filedata1 = re.sub(array1[0], variable[0] + str(variable[1]) + variable[len(variable)-1],filedata)
filedata = filedata.replace(array1[0], variable[0] + str(variable[1]) + variable[len(variable)-1])

#print("\n\n\n\n")
#print(filedata1)
f = open("BranchPredictor.py", "w")
f.write(filedata)  # writing back into the file
f.close()


#extraChar = first_difference(array1[0], variable[0] + str(variable[1]) + variable[len(variable)-1])
#print("Extra Character:", extraChar)
