import subprocess #subprocess is used will look into the issue
import shutil
import os
from replacementfunctions import *
global pro1
localbp_predictor = "LocalBP()"
bi_predictor = 'BiModeBP()'
tbp_predictor = 'TournamentBP()'
bp_string = "NULL"
benchmark_directory = "/home/johnj/gem5/m5out/benchmarks/458.sjeng"
gem5_directory = '/home/johnj/gem5'

benchmark_script = "./runGem5_458.sh"

#build_command = "scons build/X86/gem5.opt -j 4"
#run_command = "time /home/johnj/gem5/build/X86/gem5.opt -d /home/johnj/gem5/m5out/benchmarks/458.sjeng/output /home/johnj/gem5/configs/example/se.py -c /home/johnj/gem5/m5out/benchmarks/458.sjeng/src/benchmark -o /home/johnj/gem5/m5out/benchmarks/458.sjeng/data/test.txt -I 1000 --cpu-type=TimingSimpleCPU --caches --l2cache --l1d_size=128kB --l1i_size=128kB --l2_size=1MB --l1d_assoc=2 --l1i_assoc=2 --l2_assoc=1 --cacheline_size=64"
try:
    os.mkdir(benchmark_directory + "/output")
except OSError as error:
    print("\n folder already exists neglecting command")
try:
    os.mkdir(benchmark_directory+"/output/"+localbp_predictor)
except OSError as error:
    print("\n folder already exists neglecting command")
try:
    os.mkdir(benchmark_directory+"/output/"+tbp_predictor)
except OSError as error:
    print("\n folder already exists neglecting command")
try:
    os.mkdir(benchmark_directory+"/output/"+bi_predictor)
except OSError as error:
    print( "\n folder already exists neglecting command")

print(" we have went through")

#______________________________________________________________________________________________________
#specify the previous values
btb_entry_array  = [1000,2000,3000]
lbp_local_array = [1000,2000,3000]
bi_choice_array = [1000,2000,3000]
bi_global_array = [1000,2000,3000]
tbp_local_array = [1000,2000,3000]
tbp_choice_array = [1000,2000,3000]
tbp_global_array = [1000,2000,3000]


def local_bp_run_and_copy(i):
    print("************************\nstarting run and copy commands\n *******************************8")

    #shell_script_command = benchmark_directory # script location # have to look into the location information
    #shell_script_command = "/home/johnj/PycharmProjects/branchpredictors/test2.sh"
    #pro1 = subprocess.Popen([shell_script_command], shell=True)
    #pro1.wait()
    #shell_script_command = "/home/johnj/PycharmProjects/branchpredictors/test3.sh"
    
    os.system(benchmark_script)
    br_directory = localbp_predictor
    src_config_path = benchmark_directory + "/m5out/config.ini"
    dst_config_path = benchmark_directory + "/output/" + br_directory + "/config_" + str(i) + ".ini"
    shutil.copyfile(src_config_path, dst_config_path)
    print('Copied configi file with  values '+ str(i)+ 'iteration')
    src_stats_path = benchmark_directory + "/m5out/stats.txt"
    dst_stats_path = benchmark_directory + "/output/" + br_directory + "/stats_" + str(i) + ".txt"
    shutil.copy(src_stats_path, dst_stats_path)
    print('Copied stats file with default values '+ str(i)+ '   iteration')
    return


def bi_bp_run_and_copy(i):
    print("************************\nstarting run and copy commands\n *******************************8")

    #shell_script_command = benchmark_directory + "/runGem5.sh"  # script location # have to look into the location information
    # shell_script_command = "/home/johnj/PycharmProjects/branchpredictors/test2.sh"
    # pro1 = subprocess.Popen([shell_script_command], shell=True)
    # pro1.wait()
    # shell_script_command = "/home/johnj/PycharmProjects/branchpredictors/test3.sh"

    os.system(benchmark_script)
    br_directory = bi_predictor
    src_config_path = benchmark_directory + "/m5out/config.ini"
    dst_config_path = benchmark_directory + "/output/" + br_directory + "/config_" + str(i) + ".ini"
    shutil.copyfile(src_config_path, dst_config_path)
    print('Copied configi file with  values ' + str(i) + 'iteration')
    src_stats_path = benchmark_directory + "/m5out/stats.txt"
    dst_stats_path = benchmark_directory + "/output/" + br_directory + "/stats_" + str(i) + ".txt"
    shutil.copy(src_stats_path, dst_stats_path)
    print('Copied stats file with default values ' + str(i) + '   iteration')
    return

def tbp_bp_run_and_copy(i):
    print("************************\nstarting run and copy commands\n *******************************8")

    #shell_script_command = benchmark_directory + "/runGem5.sh"  # script location # have to look into the location information
    # shell_script_command = "/home/johnj/PycharmProjects/branchpredictors/test2.sh"
    # pro1 = subprocess.Popen([shell_script_command], shell=True)
    # pro1.wait()
    # shell_script_command = "/home/johnj/PycharmProjects/branchpredictors/test3.sh"

    os.system(benchmark_script)
    br_directory = tbp_predictor
    src_config_path = benchmark_directory + "/m5out/config.ini"
    dst_config_path = benchmark_directory + "/output/" + br_directory + "/config_" + str(i) + ".ini"
    shutil.copyfile(src_config_path, dst_config_path)
    print('Copied configi file with  values ' + str(i) + 'iteration')
    src_stats_path = benchmark_directory + "/m5out/stats.txt"
    dst_stats_path = benchmark_directory + "/output/" + br_directory + "/stats_" + str(i) + ".txt"
    shutil.copy(src_stats_path, dst_stats_path)
    print('Copied stats file with default values ' + str(i) + '   iteration')
    return





print(" the program officially starts from this point \n")
branchpredictor_replacement(bp_string,localbp_predictor)








# local branch predictor
# first btb enntry is taken as constant
print ("local branch predictor testing now ")





print(" btb array is constant \n *******************************************")





for i in range(len(lbp_local_array)):
    print(btb_entry_array[0], " the constant btb entries which are going to use")
    print(lbp_local_array[i]," the current local branch predictor size value we would be using")
    btbreplace(btb_entry_array[0])
    lbp_local_replace(lbp_local_array[i])
    k = " btb_C_:_lbp_X_:_"+"iteration_" + str(i)
    #pro1 = subprocess.Popen(["scons build/X86/gem5.opt -j 4"], shell=True, cwd=gem5_directory)
    #pro1.wait()
    os.system("scons build/X86/gem5.opt -j 4")
    print("build sucessfull")
    local_bp_run_and_copy(k) 
'''    
shell_script_command = "/home/johnj/PycharmProjects/branchpredictors/test1.sh"
pro1 = subprocess.Popen([shell_script_command], shell=True)
pro1.wait()
'''

print (" now considering the local branch predictor size as constant")

for i in range(len(btb_entry_array)):
    print(btb_entry_array[i], " the current btb entries which are going to use")
    print(lbp_local_array[0], " the constant local branch predictor size value we would be using")
    btbreplace(btb_entry_array[i])
    lbp_local_replace(lbp_local_array[0])
    k = " btb_X_:_lbp_C:_" + "iteration_" + str(i)
    #pro1 = subprocess.Popen(["scons build/X86/gem5.opt -j 4"], shell=True , cwd = gem5_directory)
    #pro1.wait()
    os.system("scons build/X86/gem5.opt -j 4")
    local_bp_run_and_copy(k)

print(" local branch predictor combinations are  done")







print("********************************************88\n************************************\n\n")







print("bi mode predictor mode \n")






# bi mode predictor

branchpredictor_replacement(localbp_predictor,bi_predictor)

print(" btb entry  and global values are constant")
for i in range(len(bi_choice_array)):
    print(btb_entry_array[0], " the constant btb entries which are going to use")
    print(bi_global_array[0]," the constant global predictor size  which are going to use" )
    print(bi_choice_array[i], " the current choice  branch predictor size value we would be using")
    btbreplace(btb_entry_array[0])
    bi_global_replace(bi_global_array[0])
    bi_choice_replace(bi_choice_array[i])
    k = " btb_C_:_bi_global_C_:_bi_choice_X"+"iteration_" + str(i)
    #pro1 = subprocess.Popen(["scons build/X86/gem5.opt -j 4"], shell=True, cwd=gem5_directory)
    #pro1.wait()
    os.system("scons build/X86/gem5.opt -j 4")
    bi_bp_run_and_copy(k)

print("\n\n\n\n btb entry and choice values are constant")
for i in range(len(bi_global_array)):
    print(btb_entry_array[0], " the constant btb entries which are going to use")
    print(bi_global_array[i]," the constant global predictor size  which are going to use" )
    print(bi_choice_array[0], " the current choice  branch predictor size value we would be using")
    btbreplace(btb_entry_array[0])
    bi_global_replace(bi_global_array[i])
    bi_choice_replace(bi_choice_array[0])
    k = " btb_C_:_bi_global_X_:_bi_choice_C"+"iteration_" + str(i)
    #pro1 = subprocess.Popen(["scons build/X86/gem5.opt -j 4"], shell=True, cwd=gem5_directory)
    #pro1.wait()
    os.system("scons build/X86/gem5.opt -j 4")
    bi_bp_run_and_copy(k)
print("\n\n\n global and choice values are constnat")
for i in range(len(btb_entry_array)):
    print(btb_entry_array[i], " the constant btb entries which are going to use")
    print(bi_global_array[0]," the constant global predictor size  which are going to use" )
    print(bi_choice_array[0], " the current choice  branch predictor size value we would be using")
    btbreplace(btb_entry_array[i])
    bi_global_replace(bi_global_array[0])
    bi_choice_replace(bi_choice_array[0])
    k = " btb_X_:_bi_global_C_:_bi_choice_C"+"iteration_" + str(i)
    #pro1 = subprocess.Popen(["scons build/X86/gem5.opt -j 4"], shell=True, cwd=gem5_directory)
    #pro1.wait()
    os.system("scons build/X86/gem5.opt -j 4")
    bi_bp_run_and_copy(k)

print("\n bi mode predcicton calculations are done")






print("\n****************************************************\n**********************************88")






branchpredictor_replacement(bi_predictor,tbp_predictor)

print("\n tournamnet predictor calculations would be starting")
print(" btb entry ,local  ,global values are constant")
for i in range(len(bi_choice_array)):
    print(btb_entry_array[0], " the constant btb entries which are going to use")
    print(tbp_local_array[0], " the constant global predictor size  which are going to use")
    print(tbp_global_array[0]," the constant global predictor size  which are going to use" )
    print(tbp_choice_array[i], " the current choice  branch predictor size value we would be using")
    btbreplace(btb_entry_array[0])
    tbp_local_replace(tbp_local_array[0])
    tbp_global_replace(tbp_global_array[0])
    tbp_choice_replace(tbp_choice_array[i])
    k = " btb_C_:_tpb_local_C:_tpb_global_C_:_tpb_choice_X"+"iteration_" + str(i)
    #pro1 = subprocess.Popen(["scons build/X86/gem5.opt -j 4"], shell=True, cwd=gem5_directory)
    #pro1.wait()
    os.system("scons build/X86/gem5.opt -j 4")
    tbp_bp_run_and_copy(k)
print(" btb entry ,local  ,choice values are constant")
for i in range(len(bi_choice_array)):
    print(btb_entry_array[0], " the constant btb entries which are going to use")
    print(tbp_local_array[0], " the constant global predictor size  which are going to use")
    print(tbp_global_array[i]," the constant global predictor size  which are going to use" )
    print(tbp_choice_array[0], " the current choice  branch predictor size value we would be using")
    btbreplace(btb_entry_array[0])
    tbp_local_replace(tbp_local_array[0])
    tbp_global_replace(tbp_global_array[i])
    tbp_choice_replace(tbp_choice_array[0])
    k = " btb_C_:_tpb_local_C:_tpb_global_X_:_tpb_choice_C"+"iteration_" + str(i)
    #pro1 = subprocess.Popen(["scons build/X86/gem5.opt -j 4"], shell=True, cwd=gem5_directory)
    #pro1.wait()
    os.system("scons build/X86/gem5.opt -j 4")
    tbp_bp_run_and_copy(k)
print(" btb entry ,global  ,choice values are constant")
for i in range(len(bi_choice_array)):
    print(btb_entry_array[0], " the constant btb entries which are going to use")
    print(tbp_local_array[i], " the constant global predictor size  which are going to use")
    print(tbp_global_array[0]," the constant global predictor size  which are going to use" )
    print(tbp_choice_array[0], " the current choice  branch predictor size value we would be using")
    btbreplace(btb_entry_array[0])
    tbp_local_replace(tbp_local_array[i])
    tbp_global_replace(tbp_global_array[0])
    tbp_choice_replace(tbp_choice_array[0])
    k = " btb_C_:_tpb_local_X:_tpb_global_C_:_tpb_choice_C"+"iteration_" + str(i)
    #pro1 = subprocess.Popen(["scons build/X86/gem5.opt -j 4"], shell=True, cwd=gem5_directory)
    #pro1.wait()
    os.system("scons build/X86/gem5.opt -j 4")
    tbp_bp_run_and_copy(k)
print(" local ,global  ,choice values are constant")
for i in range(len(bi_choice_array)):
    print(btb_entry_array[i], " the constant btb entries which are going to use")
    print(tbp_local_array[0], " the constant global predictor size  which are going to use")
    print(tbp_global_array[0]," the constant global predictor size  which are going to use" )
    print(tbp_choice_array[0], " the current choice  branch predictor size value we would be using")
    btbreplace(btb_entry_array[i])
    tbp_local_replace(tbp_local_array[0])
    tbp_global_replace(tbp_global_array[0])
    tbp_choice_replace(tbp_choice_array[0])
    k = " btb_C_:_tpb_local_X:_tpb_global_C_:_tpb_choice_C"+"iteration_" + str(i)
    #pro1 = subprocess.Popen(["scons build/X86/gem5.opt -j 4"], shell=True, cwd=gem5_directory)
    #pro1.wait()
    os.system("scons build/X86/gem5.opt -j 4")
    tbp_bp_run_and_copy(k)

print("\n\n program has sucessfully ran and all possible data values are collected ")

branchpredictor_replacement(tbp_predictor,bp_string)