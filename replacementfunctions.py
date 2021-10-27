
import re
import subprocess
branch_pred_path = 'BranchPredictor.py' #branch predictor file loaction
simplecpu_path = 'BaseSimpleCPU.py'  #simple cpu file location
def btbreplace(current_value , replacement_value ):
  with open(branch_pred_path, 'r') as file:
    filedata = file.read()  #file reading portion of the code
  string1 = 'BTBEntries = Param.Unsigned\('
  string2 = ', "Number of BTB entries"\)#btbentries'

  pattern = string1 + str(current_value) + string2
  result = re.findall(pattern, filedata)
  variable = result[0]  # store the extracted portion
  variable1 = re.sub(str(current_value), str(replacement_value), variable)  # switch and replace wit the required value

  print(variable1)
  filedata1 = re.sub(string1 + str(current_value) + string2,
                     variable1, filedata)  # puttting back into the main string with no errors

  f = open(branch_pred_path, "w")
  f.write(filedata1)  # writing back into the file
  f.close()


  return

'''
current_value = 1200
replacement_value = 1300
#btbreplace(current_value,replacement_value)
pro1 = subprocess.Popen(["./test1.sh"],shell= True)
pro1.wait()
pro1 = subprocess.Popen(["./test2.sh"],shell= True)
pro1.wait()
pro1 = subprocess.Popen(["./test3.sh"],shell= True)
pro1.wait()
'''
def lbp_local_replace(current_value , replacement_value ):
  with open(branch_pred_path, 'r') as file:
    filedata = file.read()  #file reading portion of the code
  string1 = 'localPredictorSize = Param.Unsigned\('
  string2 =  ', "Size of local predictor"\)#local_predictor_local'

  pattern = string1 + str(current_value) + string2
  result = re.findall(pattern, filedata)
  variable = result[0] #store the extracted portion
  variable1 = re.sub(str(current_value), str(replacement_value), variable)  #switch and replace wit the required value

  print(variable1)
  filedata1 = re.sub(string1 + str(current_value) + string2,
                     variable1, filedata)   # puttting back into the main string with no errors

  f = open(branch_pred_path, "w")
  f.write(filedata1)   #writing back into the file
  f.close()
  return

def bi_global_replace(current_value,replacement_value):
  with open(branch_pred_path, 'r') as file:
    filedata = file.read()  #file reading portion of the code
  string1 = 'globalPredictorSize = Param.Unsigned\('
  string2 =  ', "Size of global predictor"\)#bi_predictor_local'

  pattern = string1 + str(current_value) + string2
  result = re.findall(pattern, filedata)
  variable = result[0] #store the extracted portion
  variable1 = re.sub(str(current_value), str(replacement_value), variable)  #switch and replace wit the required value

  print(variable1)
  filedata1 = re.sub(string1 + str(current_value) + string2,
                     variable1, filedata)   # puttting back into the main string with no errors

  f = open(branch_pred_path, "w")
  f.write(filedata1)   #writing back into the file
  f.close()
  return
def bi_choice_replace(current_value,replacement_value):
  with open(branch_pred_path, 'r') as file:
    filedata = file.read()  #file reading portion of the code
  string1 = 'choicePredictorSize = Param.Unsigned\('
  string2 =  ', "Size of choice predictor"\)#bi_predictor_choice'

  pattern = string1 + str(current_value) + string2
  result = re.findall(pattern, filedata)
  variable = result[0] #store the extracted portion
  variable1 = re.sub(str(current_value), str(replacement_value), variable)  #switch and replace wit the required value

  print(variable1)
  filedata1 = re.sub(string1 + str(current_value) + string2,
                     variable1, filedata)   # puttting back into the main string with no errors

  f = open(branch_pred_path, "w")
  f.write(filedata1)   #writing back into the file
  f.close()
  return
def tpb_choice_replace(current_value,replacement_value):
  with open(branch_pred_path, 'r') as file:
    filedata = file.read()  #file reading portion of the code
  string1 = 'choicePredictorSize = Param.Unsigned\('
  string2 =  ', "Size of choice predictor"\)#tpb_predictor_choice'

  pattern = string1 + str(current_value) + string2
  result = re.findall(pattern, filedata)
  variable = result[0] #store the extracted portion
  variable1 = re.sub(str(current_value), str(replacement_value), variable)  #switch and replace wit the required value

  print(variable1)
  filedata1 = re.sub(string1 + str(current_value) + string2,
                     variable1, filedata)   # puttting back into the main string with no errors

  f = open(branch_pred_path, "w")
  f.write(filedata1)   #writing back into the file
  f.close()
  return
def tpb_global_replace(current_value,replacement_value):
  with open(branch_pred_path, 'r') as file:
    filedata = file.read()  #file reading portion of the code
  string1 = 'globalPredictorSize = Param.Unsigned\('
  string2 =  ', "Size of global predictor"\)#tpb_predictor_global'

  pattern = string1 + str(current_value) + string2
  result = re.findall(pattern, filedata)
  variable = result[0] #store the extracted portion
  variable1 = re.sub(str(current_value), str(replacement_value), variable)  #switch and replace wit the required value

  print(variable1)
  filedata1 = re.sub(string1 + str(current_value) + string2,
                     variable1, filedata)   # puttting back into the main string with no errors

  f = open(branch_pred_path, "w")
  f.write(filedata1)   #writing back into the file
  f.close()
  return
def tpb_local_replace(current_value , replacement_value ):
  with open(branch_pred_path, 'r') as file:
    filedata = file.read()  #file reading portion of the code
  string1 = 'localPredictorSize = Param.Unsigned\('
  string2 =  ', "Size of local predictor"\)#tpb_predictor_local'

  pattern = string1 + str(current_value) + string2
  result = re.findall(pattern, filedata)
  variable = result[0] #store the extracted portion
  variable1 = re.sub(str(current_value), str(replacement_value), variable)  #switch and replace wit the required value

  print(variable1)
  filedata1 = re.sub(string1 + str(current_value) + string2,
                     variable1, filedata)   # puttting back into the main string with no errors

  f = open(branch_pred_path, "w")
  f.write(filedata1)   #writing back into the file
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


