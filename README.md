# branchpredictors
1. specify your benchmark directory , gem 5 directory information in main_program.py
2. In replacment.py specify your branchprediction.py and tsimplecpu.py path locations.
3. enter the command for running gem5 with all the paths specified from home to the final location.
4. before the first run in basesimplecpu.py change the branch value to be "NULL"
5. place comment tags for the places we need to change like as shown in the sample branchpredictor.py
6. main program.py and replacementfunctions.py has to be kept in the same directory.
7. the output files are configured to be saved in the benchmark directory/output  so you have to make sure you set this directory  is the output directory when you call the program
8. build function is disabled currently after each run . if you want you can uncomment and use it.
9.  a lot of extra files you see were build during the initial testing phase they are not deleted yet because there is a possiblity of bugs and such. never mind about them. 
10. The outputs will be in the format  btb_C_:_lbp_X_:_"+"iteration_" + str(i) whre btb_c it means btb value is constant and  lbp_x whre local branch predictor value is constant. it also has an iteration count value too for it so see which iteration it is . for quickly finding your data try to see it in list mode as the file names are pretty large
