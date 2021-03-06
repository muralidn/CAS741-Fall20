## \file Calculations.py
# \author Naveen Ganesh Muralidharan
# \brief Provides functions for calculating the outputs
import scipy.integrate

import Constants

## \brief Calculates Process Variable: The output value from the power plant
# \param r_t Set-Point: The desired value that the control system must reach. This also knows as the reference variable
# \param K_p Proportional Gain: Gain constant of the proportional controller
# \param K_d Derivative Gain: Gain constant of the derivative controller
# \param t_sim Simulation Time: Total execution time of the PD simulation (s)
# \param t_step Step Time: Simulation step time (s)
# \return Process Variable: The output value from the power plant
def func_y_t(r_t, K_p, K_d, t_sim, t_step):
    outfile = open("log.txt", "a")
    print("function func_y_t called with inputs: {", file=outfile)
    print("  r_t = ", end="", file=outfile)
    print(r_t, end="", file=outfile)
    print(", ", file=outfile)
    print("  K_p = ", end="", file=outfile)
    print(K_p, end="", file=outfile)
    print(", ", file=outfile)
    print("  K_d = ", end="", file=outfile)
    print(K_d, end="", file=outfile)
    print(", ", file=outfile)
    print("  t_sim = ", end="", file=outfile)
    print(t_sim, end="", file=outfile)
    print(", ", file=outfile)
    print("  t_step = ", end="", file=outfile)
    print(t_step, file=outfile)
    print("  }", file=outfile)
    outfile.close()
    
    def f(t, y_t):
        return [(r_t * K_p - (1 + K_p) * y_t[0]) / (2 + K_d)]
    
    r = scipy.integrate.ode(f)
    outfile = open("log.txt", "a")
    print("var 'r' assigned ", end="", file=outfile)
    print("Instance of ode object", end="", file=outfile)
    print(" in module Calculations", file=outfile)
    outfile.close()
    r.set_integrator("dopri5", atol=Constants.Constants.AbsTol, rtol=Constants.Constants.RelTol)
    r.set_initial_value(0.0, 0.0)
    y_t = [0.0]
    outfile = open("log.txt", "a")
    print("var 'y_t' assigned ", end="", file=outfile)
    print(y_t, end="", file=outfile)
    print(" in module Calculations", file=outfile)
    outfile.close()
    while r.successful() and r.t < t_sim:
        r.integrate(r.t + t_step)
        y_t.append(r.y[0])
    
    return y_t
