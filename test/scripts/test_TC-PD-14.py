import sys
sys.path.append(r"..\\..\\src\\")

import Calculations

import pytest

def test_PD_14 ():

    r_t = 1
    K_p = 10
    K_d = 1
    t_step = 0.01
    t_sim = 1

    y_t = Calculations.func_y_t(r_t,K_p,K_d,t_sim,t_step)

    assert(len(y_t) == (int((t_sim/t_step)) + 1) )

