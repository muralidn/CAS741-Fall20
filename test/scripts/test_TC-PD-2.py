import pytest
import pytest_cov
import test_runner

test_runner.build_output_dict(r'TC-PD-2.csv')
    
def test_PD_2_1():
    test_runner.run("TC-PD-2-1", tolerance=0.001)

def test_PD_2_2():
    test_runner.run("TC-PD-2-2", tolerance=0.001)

def test_PD_2_3():
    test_runner.run("TC-PD-2-3", tolerance=0.001)    




