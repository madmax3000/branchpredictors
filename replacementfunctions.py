
import re
import subprocess
branch_pred_path = 'BranchPredictor.py' #branch predictor file loaction
simplecpu_path = 'BaseSimpleCPU.py'  #simple cpu file location
def btbreplace(replacement_value ):
  with open(branch_pred_path, 'r') as file:
    filedata = file.read()


  finaltag = ".*#btbentries$"
  value = re.split("\n", filedata)
  array1 = []
  # print(value)s
  for i in range(0, len(value)):
    # print(" loop " + str(i))

    # print(value[i])
    t = re.match(finaltag, value[i])
    if t is None:
      if i == 61:
        print(value[i])

    else:
      # print(t.group())
      array1.append(t.group())
    # print(array1)

    # print(t)
  # print(" this is the array value ",array1)
  variable = re.split("[0-9]", array1[0])
  # print(" this is the variable value ",variable)


  variable[1] = replacement_value # dont use single digit values 2 digits to any other digits work fine

  # print(re.findall('\n    BTBEntries = Param.Unsigned(1000, "Number of BTB entries")#btbentries\n',filedata) , " this is the match query")
  # print(array1[0])
  # print(variable[0] + str(variable[1]) + variable[len(variable)-1])

  # filedata1 = re.sub(array1[0], variable[0] + str(variable[1]) + variable[len(variable)-1],filedata)
  filedata = filedata.replace(array1[0], variable[0] + str(variable[1]) + variable[len(variable) - 1])

  # print("\n\n\n\n")
  # print(filedata1)
  f = open(branch_pred_path, "w")
  f.write(filedata)  # writing back into the file
  f.close()
  return


'''
current_value = 1200
replacement_value = 1300
#btbreplace(current_value,replacement_value) 
pro1 = subprocess.Popen(["/home/johnj/PycharmProjects/branchpredictors/test/test1.sh"],shell= True)
pro1.wait()

pro1 = subprocess.Popen(["./test2.sh"],shell= True)
pro1.wait()
pro1 = subprocess.Popen(["./test3.sh"],shell= True)
pro1.wait()
'''
def lbp_local_replace(replacement_value ):
  with open(branch_pred_path, 'r') as file:
    filedata = file.read()


  finaltag = ".*#local_predictor_local$"
  value = re.split("\n", filedata)
  array1 = []
  # print(value)
  for i in range(0, len(value)):
    # print(" loop " + str(i))

    # print(value[i])
    t = re.match(finaltag, value[i])
    if t is None:
      if i == 61:
        print(value[i])

    else:
      # print(t.group())
      array1.append(t.group())
    # print(array1)

    # print(t)
  # print(" this is the array value ",array1)
  variable = re.split("[0-9]", array1[0])
  # print(" this is the variable value ",variable)


  variable[1] = replacement_value # dont use single digit values 2 digits to any other digits work fine

  # print(re.findall('\n    BTBEntries = Param.Unsigned(1000, "Number of BTB entries")#btbentries\n',filedata) , " this is the match query")
  # print(array1[0])
  # print(variable[0] + str(variable[1]) + variable[len(variable)-1])

  # filedata1 = re.sub(array1[0], variable[0] + str(variable[1]) + variable[len(variable)-1],filedata)
  filedata = filedata.replace(array1[0], variable[0] + str(variable[1]) + variable[len(variable) - 1])

  # print("\n\n\n\n")
  # print(filedata1)
  f = open(branch_pred_path, "w")
  f.write(filedata)  # writing back into the file
  f.close()
  return



def bi_global_replace(replacement_value):
  with open(branch_pred_path, 'r') as file:
    filedata = file.read()


  finaltag = ".*#bi_predictor_global$"
  value = re.split("\n", filedata)
  array1 = []
  # print(value)
  for i in range(0, len(value)):
    # print(" loop " + str(i))

    # print(value[i])
    t = re.match(finaltag, value[i])
    if t is None:
      if i == 61:
        print(value[i])

    else:
      # print(t.group())
      array1.append(t.group())
    # print(array1)

    # print(t)
  # print(" this is the array value ",array1)
  variable = re.split("[0-9]", array1[0])
  # print(" this is the variable value ",variable)


  variable[1] = replacement_value # dont use single digit values 2 digits to any other digits work fine

  # print(re.findall('\n    BTBEntries = Param.Unsigned(1000, "Number of BTB entries")#btbentries\n',filedata) , " this is the match query")
  # print(array1[0])
  # print(variable[0] + str(variable[1]) + variable[len(variable)-1])

  # filedata1 = re.sub(array1[0], variable[0] + str(variable[1]) + variable[len(variable)-1],filedata)
  filedata = filedata.replace(array1[0], variable[0] + str(variable[1]) + variable[len(variable) - 1])

  # print("\n\n\n\n")
  # print(filedata1)
  f = open(branch_pred_path, "w")
  f.write(filedata)  # writing back into the file
  f.close()
  return
def bi_choice_replace(replacement_value):
  with open(branch_pred_path, 'r') as file:
    filedata = file.read()


  finaltag = ".*#bi_predictor_choice$"
  value = re.split("\n", filedata)
  array1 = []
  # print(value)
  for i in range(0, len(value)):
    # print(" loop " + str(i))

    # print(value[i])
    t = re.match(finaltag, value[i])
    if t is None:
      if i == 61:
        print(value[i])

    else:
      # print(t.group())
      array1.append(t.group())
    # print(array1)

    # print(t)
  # print(" this is the array value ",array1)
  variable = re.split("[0-9]", array1[0])
  # print(" this is the variable value ",variable)


  variable[1] = replacement_value # dont use single digit values 2 digits to any other digits work fine

  # print(re.findall('\n    BTBEntries = Param.Unsigned(1000, "Number of BTB entries")#btbentries\n',filedata) , " this is the match query")
  # print(array1[0])
  # print(variable[0] + str(variable[1]) + variable[len(variable)-1])

  # filedata1 = re.sub(array1[0], variable[0] + str(variable[1]) + variable[len(variable)-1],filedata)
  filedata = filedata.replace(array1[0], variable[0] + str(variable[1]) + variable[len(variable) - 1])

  # print("\n\n\n\n")
  # print(filedata1)
  f = open(branch_pred_path, "w")
  f.write(filedata)  # writing back into the file
  f.close()
  return
def tpb_choice_replace(replacement_value):
  with open(branch_pred_path, 'r') as file:
    filedata = file.read()


  finaltag = ".*#tpb_predictor_choice$"
  value = re.split("\n", filedata)
  array1 = []
  # print(value)
  for i in range(0, len(value)):
    # print(" loop " + str(i))

    # print(value[i])
    t = re.match(finaltag, value[i])
    if t is None:
      if i == 61:
        print(value[i])

    else:
      # print(t.group())
      array1.append(t.group())
    # print(array1)

    # print(t)
  # print(" this is the array value ",array1)
  variable = re.split("[0-9]", array1[0])
  # print(" this is the variable value ",variable)


  variable[1] = replacement_value # dont use single digit values 2 digits to any other digits work fine

  # print(re.findall('\n    BTBEntries = Param.Unsigned(1000, "Number of BTB entries")#btbentries\n',filedata) , " this is the match query")
  # print(array1[0])
  # print(variable[0] + str(variable[1]) + variable[len(variable)-1])

  # filedata1 = re.sub(array1[0], variable[0] + str(variable[1]) + variable[len(variable)-1],filedata)
  filedata = filedata.replace(array1[0], variable[0] + str(variable[1]) + variable[len(variable) - 1])

  # print("\n\n\n\n")
  # print(filedata1)
  f = open(branch_pred_path, "w")
  f.write(filedata)  # writing back into the file
  f.close()
  return
def tpb_global_replace(replacement_value):
  with open(branch_pred_path, 'r') as file:
    filedata = file.read()


  finaltag = ".*#tpb_predictor_global$"
  value = re.split("\n", filedata)
  array1 = []
  # print(value)
  for i in range(0, len(value)):
    # print(" loop " + str(i))

    # print(value[i])
    t = re.match(finaltag, value[i])
    if t is None:
      if i == 61:
        print(value[i])

    else:
      # print(t.group())
      array1.append(t.group())
    # print(array1)

    # print(t)
  # print(" this is the array value ",array1)
  variable = re.split("[0-9]", array1[0])
  # print(" this is the variable value ",variable)


  variable[1] = replacement_value # dont use single digit values 2 digits to any other digits work fine

  # print(re.findall('\n    BTBEntries = Param.Unsigned(1000, "Number of BTB entries")#btbentries\n',filedata) , " this is the match query")
  # print(array1[0])
  # print(variable[0] + str(variable[1]) + variable[len(variable)-1])

  # filedata1 = re.sub(array1[0], variable[0] + str(variable[1]) + variable[len(variable)-1],filedata)
  filedata = filedata.replace(array1[0], variable[0] + str(variable[1]) + variable[len(variable) - 1])

  # print("\n\n\n\n")
  # print(filedata1)
  f = open(branch_pred_path, "w")
  f.write(filedata)  # writing back into the file
  f.close()
  return
def tpb_local_replace(replacement_value ):
  with open(branch_pred_path, 'r') as file:
    filedata = file.read()


  finaltag = ".*#tpb_predictor_local$"
  value = re.split("\n", filedata)
  array1 = []
  # print(value)
  for i in range(0, len(value)):
    # print(" loop " + str(i))

    # print(value[i])
    t = re.match(finaltag, value[i])
    if t is None:
      if i == 61:
        print(value[i])

    else:
      # print(t.group())
      array1.append(t.group())
    # print(array1)

    # print(t)
  # print(" this is the array value ",array1)
  variable = re.split("[0-9]", array1[0])
  # print(" this is the variable value ",variable)


  variable[1] = replacement_value # dont use single digit values 2 digits to any other digits work fine

  # print(re.findall('\n    BTBEntries = Param.Unsigned(1000, "Number of BTB entries")#btbentries\n',filedata) , " this is the match query")
  # print(array1[0])
  # print(variable[0] + str(variable[1]) + variable[len(variable)-1])

  # filedata1 = re.sub(array1[0], variable[0] + str(variable[1]) + variable[len(variable)-1],filedata)
  filedata = filedata.replace(array1[0], variable[0] + str(variable[1]) + variable[len(variable) - 1])

  # print("\n\n\n\n")
  # print(filedata1)
  f = open(branch_pred_path, "w")
  f.write(filedata)  # writing back into the file
  f.close()
  return
def branchpredictor_replacement(current_value , replacement_value ):
  with open(simplecpu_path, 'r') as file:
    filedata = file.read()  #file reading portion of the code
  string1 = 'branchPred = Param.BranchPredictor\('
  string2 = ', "Branch Predictor"\)'

  pattern = string1 + str(current_value) + string2
  result = re.findall(pattern, filedata)
  variable = result[0]  # store the extracted portion
  variable1 = re.sub(str(current_value), str(replacement_value), variable)  # switch and replace wit the required value

  print(variable1)
  filedata1 = re.sub(string1 + str(current_value) + string2,
                     variable1, filedata)  # puttting back into the main string with no errors

  f = open(simplecpu_path, "w")
  f.write(filedata1)  # writing back into the file
  f.close()


  return

'''
btbreplace(2048)
bi_choice_replace(2048)
bi_global_replace(2048)
lbp_local_replace(2048)
tpb_local_replace(2048)
tpb_choice_replace(2048)
tpb_global_replace(2048)
'''