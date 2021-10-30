import subprocess
import shutil
import os
from replacementfunctions import *
localbp_predictor = "LocalBP"
bi_predictor = 'BiModeBP'
tbp_predictor = 'TournamentBP'
bp_string = "NULL"
#______________________________________________________________________________________________________
#specify the previous values
btb_entry_array  = [1000,2000,3000]
local_pred_array = [1000,2000,3000]

def local_bp_run_and_copy(btb_array_entry,pred_array_entry,i):
    shell_script_location = "./runGem5.sh"  # script location # have to look into the location information
    branchpredictor_replacement(bp_string, localbp_predictor)
    pro1 = subprocess.Popen([shell_script_location], shell=True)
    pro1.wait()
    directory = localbp_predictor
    parent_dir = '/home/johnj/gem5/m5out/benchmarks/458.sjeng/output'
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    src_path = "/home/johnj/gem5/m5out/benchmarks/458.sjeng/m5out/config.ini"
    dst_path = r"/home/johnj/gem5/m5out/benchmarks/458.sjeng/output/" + directory + "config" + str[i] + ".ini"
    shutil.copy(src_path, dst_path)
    print('Copied configi file with  values '+ str(i)+ 'iteration')
    src_path = "/home/johnj/gem5/m5out/benchmarks/458.sjeng/m5out/stats.txt"
    dst_path = r"/home/johnj/gem5/m5out/benchmarks/458.sjeng/output/" + directory + "stats" + str(i) + ".txt"
    print('Copied stats file with default values '+ str(i)+ 'iteration')
    return



shell_script_location = "./runGem5.sh" #script location # have to look into the location information
branchpredictor_replacement(bp_string, localbp_predictor)
pro1 = subprocess.Popen([shell_script_location],shell= True)
pro1.wait()
i = 0
directory =  localbp_predictor
parent_dir = '/home/johnj/gem5/m5out/benchmarks/458.sjeng/output'
path = os.path.join(parent_dir, directory)
os.mkdir(path)
src_path = "/home/johnj/gem5/m5out/benchmarks/458.sjeng/m5out/config.ini"
dst_path = r"/home/johnj/gem5/m5out/benchmarks/458.sjeng/output/" + directory + "config" + str[i]+ ".ini"
shutil.copy(src_path, dst_path)
print('Copied configi file with default values ')
src_path = "/home/johnj/gem5/m5out/benchmarks/458.sjeng/m5out/stats.txt"
dst_path = r"/home/johnj/gem5/m5out/benchmarks/458.sjeng/output/" + directory + "stats" + str(i)+ ".txt"
print('Copied stats file with default values ')
