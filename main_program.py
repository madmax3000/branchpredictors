import subprocess
from replacementfunctions import *
localbp_predictor = "LocalBP"
bi_predictor = 'BiModeBP'
tbp_predictor = 'TournamentBP'
bp_string = "NULL"
shell_script_location = "./runGem5.sh" #script location
branchpredictor_replacement(bp_string, localbp_predictor)
pro1 = subprocess.Popen([shell_script_location],shell= True)
pro1.wait()
