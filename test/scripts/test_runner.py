import pytest
import pytest_cov
import csv
import pprint

import os
import subprocess

INPUT_FILES_ROOT = r"..\data\inputs"
OUTPUTS_RESULTS_ROOT = r"..\data\outputs"
PD_SCRIPT_PATH = r"..\..\src\Control.py"
PD_OUTPUT_FILE_PATH = r"output.txt"

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

def parse_output():
    output_file = open (PD_OUTPUT_FILE_PATH)
    output_data = output_file.read()
    output_list = output_data.split(",")
    output_file.close()
    return float(output_list[-1].replace("]",""))


def run(test_case, tolerance=0.001):

    if os.path.exists(PD_OUTPUT_FILE_PATH):
        os.remove(PD_OUTPUT_FILE_PATH)

    ip_file = os.path.normpath(os.path.join(INPUT_FILES_ROOT, test_case + ".txt" ))
    ip_contents = ""
    with open (ip_file) as ip_file_obj:
        ip_contents = ip_file_obj.readlines()
        ip_contents = " ".join(ip_contents)
        ip_contents = ip_contents.replace("\n","")
        ip_contents = ip_contents.replace("# ",", \n")

    args = ["python", PD_SCRIPT_PATH, ip_file]
    p = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    try:
        pprint.pprint("Inputs:")
        pprint.pprint(ip_contents)
        pprint.pprint("Outputs:")
        pprint.pprint(args)
        stdout, stderr = p.communicate(timeout=10)
        if (test_lookup_table[test_case]["Error"] == "Y"):
            err = stderr.decode("utf-8")
            err = err.split("\r\n")
            err = [i.lstrip() for i in err]
            pprint.pprint(err)
            assert ("InputError" in err[-2])
        else:
            actual_output = parse_output()
            expected_output = float(test_lookup_table[test_case]["yt"])
            delta = abs(expected_output - actual_output)
            pprint.pprint("Expected Output: {}".format(expected_output))
            pprint.pprint("Actual Output: {}".format(actual_output))
            pprint.pprint("Relative Error: +/- {}".format(tolerance))
            assert (delta < tolerance)

    except subprocess.TimeoutExpired:
        print("Process timedout")
        p.kill()