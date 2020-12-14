import pytest
import pytest_cov
import csv
import pprint

import os
import subprocess
import shutil
from sys import platform

if platform == "linux" or platform == "linux2" or platform == "darwin":
    # linux
    INPUT_FILES_ROOT = r"../data/inputs"
    OUTPUTS_RESULTS_ROOT = r"../data/outputs"
    PD_SCRIPT_PATH = r"../../src/Control.py"
    PD_OUTPUT_FILE_PATH = r"output.txt"
    PD_LOG_FILE_PATH = r"log.txt"
    PYTHON_BINARY = r"python3"
else:
    # Windows...
    INPUT_FILES_ROOT = r"..\data\inputs"
    OUTPUTS_RESULTS_ROOT = r"..\data\outputs"
    PD_SCRIPT_PATH = r"..\..\src\Control.py"
    PD_OUTPUT_FILE_PATH = r"output.txt"
    PD_LOG_FILE_PATH = r"log.txt"
    PYTHON_BINARY = r"python"

test_lookup_table = dict()

def build_output_dict (output_file_path):
    global test_lookup_table 
    output_csv_path = os.path.join(OUTPUTS_RESULTS_ROOT, output_file_path)
    output_csv = open(output_csv_path)
    output_dict = csv.DictReader(output_csv)

    for test_case in output_dict:
        test_lookup_table[test_case["ID"]] = test_case

    output_csv.close()

#pprint.pprint(test_lookup_table)

def parse_output(test_case):
    output_file = open (PD_OUTPUT_FILE_PATH)
    output_data = output_file.read()
    output_list = output_data.split(",")
    output_file.close()
    shutil.copyfile(PD_OUTPUT_FILE_PATH, "output_{}.txt".format(test_case))
    return float(output_list[-1].replace("]",""))


def run(test_case, tolerance=0.001):

    if os.path.exists(PD_OUTPUT_FILE_PATH):
        os.remove(PD_OUTPUT_FILE_PATH)

    if os.path.exists(PD_LOG_FILE_PATH):
        os.remove(PD_LOG_FILE_PATH)

    ip_file = os.path.normpath(os.path.join(INPUT_FILES_ROOT, test_case + ".txt" ))
    ip_contents = ""
    with open (ip_file) as ip_file_obj:
        pprint.pprint(os.path.join(INPUT_FILES_ROOT, test_case + ".txt" ))
        ip_contents = ip_file_obj.readlines()
        ip_contents = " ".join(ip_contents)
        ip_contents = ip_contents.replace("\n","")
        ip_contents = ip_contents.replace("# ",", \n")

    args = [PYTHON_BINARY, PD_SCRIPT_PATH, ip_file]
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        pprint.pprint("Inputs:")
        pprint.pprint(ip_contents)
        pprint.pprint("Outputs:")
        pprint.pprint(args)
        stdout, stderr = p.communicate(timeout=10)
        if (test_lookup_table[test_case]["Error"] == "Y"):
            err = stderr.decode("utf-8")
            pprint.pprint(err)
            err = err.splitlines()
            err = [i.lstrip() for i in err]
            #pprint.pprint(err)
            assert ("InputError" in err[-2])
        else:
            actual_output = parse_output(test_case)
            expected_output = float(test_lookup_table[test_case]["yt"])
            delta = abs(expected_output - actual_output)
            pprint.pprint("Expected Output: {}".format(expected_output))
            pprint.pprint("Actual Output: {}".format(actual_output))
            pprint.pprint("Relative Error: +/- {}".format(tolerance))
            assert (delta < tolerance)

        shutil.copyfile(PD_LOG_FILE_PATH, "log_{}.txt".format(test_case))
    except subprocess.TimeoutExpired:
        print("Process timedout")
        p.kill()