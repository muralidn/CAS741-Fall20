## \file Control.py
# \author Naveen Ganesh Muralidharan
# \brief Controls the flow of the program
import sys

import Calculations
import InputParameters
import OutputFormat

filename = sys.argv[1]
outfile = open("log.txt", "a")
print("var 'filename' assigned ", end="", file=outfile)
print(filename, end="", file=outfile)
print(" in module Control", file=outfile)
outfile.close()
r_t, K_d, K_p, t_step, t_sim = InputParameters.get_input(filename)
InputParameters.input_constraints(r_t, K_d, K_p, t_step, t_sim)
y_t = Calculations.func_y_t(r_t, K_p, K_d, t_sim, t_step)
outfile = open("log.txt", "a")
print("var 'y_t' assigned ", end="", file=outfile)
print(y_t, end="", file=outfile)
print(" in module Control", file=outfile)
outfile.close()
OutputFormat.write_output(y_t)
