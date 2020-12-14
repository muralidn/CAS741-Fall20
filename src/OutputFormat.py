## \file OutputFormat.py
# \author Naveen Ganesh Muralidharan
# \brief Provides the function for writing outputs
## \brief Writes the output values to output.txt
# \param y_t Process Variable: The output value from the power plant
def write_output(y_t):
    outfile = open("log.txt", "a")
    print("function write_output called with inputs: {", file=outfile)
    print("  y_t = ", end="", file=outfile)
    print(y_t, file=outfile)
    print("  }", file=outfile)
    outfile.close()
    
    outputfile = open("output.txt", "w")
    print("y_t = ", end="", file=outputfile)
    print(y_t, file=outputfile)
    outputfile.close()
