# branchpredictors
1. specify your benchmark directory , gem 5 directory information in main_program.py
2. In replacment.py specify your branchprediction.py and tsimplecpu.py path locations.
3. enter the command for running gem5 with all the paths specified from home to the final location.
4. before the first run in basesimplecpu.py change the branch value to be "NULL"
5. place comment tags for the places we need to change like as shown in the sample branchpredictor.py or copy the simplecpu.py and branchpredictor.py  to the locations in your gem5 and replace with the ones given
6. main program.py and replacementfunctions.py has to be kept in the gem5directory.
7. the output files are configured to be saved in the benchmark directory/output  so you have to make sure you set this directory  is the output directory when you call the program
8. runGem5_485.sh , runGem5_470.sh in the gem5 directories along with the files we needed. rungem5_429 and other will  be found in gem5 scripts
