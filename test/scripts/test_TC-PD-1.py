import pytest
import pytest_cov
import test_runner

test_runner.build_output_dict(r'TC-PD-1.csv')
    
def test_PD_1_1():
    test_runner.run("TC-PD-1-1", tolerance=0.001)

def test_PD_1_2():
    test_runner.run("TC-PD-1-2")

def test_PD_1_3():
    test_runner.run("TC-PD-1-3") 

def test_PD_1_4():
    test_runner.run("TC-PD-1-4") 

def test_PD_1_5():
    test_runner.run("TC-PD-1-5") 

def test_PD_1_6():
    test_runner.run("TC-PD-1-6") 

def test_PD_1_7():
    test_runner.run("TC-PD-1-7") 

def test_PD_1_8():
    test_runner.run("TC-PD-1-8")
    




