import sys
import os

def test_name():
    return os.path.isdir("./venv")

def venv_active():
    return sys.prefix != sys.base_prefix

def pybliometrics_installation():
    try:
        import pybliometrics
        if pybliometrics.__version__ == "4.0":
            return True
        return False
    except ModuleNotFoundError:
        return False

def requirements_file():
    return os.path.exists("./requirements.txt")

def pubmed_package():
    try:
        import pubmed_parser
        if pubmed_parser.__version__ == "0.4.0":
            return True
        return False
    except ModuleNotFoundError:
        return False

def pybliometrics_version():
    target_package = "pybliometrics==4.0"

    try:
        with open("./requirements.txt", 'r') as file:
            lines = file.readlines()

        for line in lines:
            if line.strip() == target_package:
                return True
    except FileNotFoundError:
        return False

def test():
    print("1. Correct") if test_name() else print("1. Incorrect creation of venv")
    print("2. Correct") if venv_active() else print("2. Incorrect activation of venv")
    print("3. Correct") if pubmed_package() else print("3. Incorrect pubmed_parser installation (version)")
    print("4. Correct") if requirements_file() else print("4. Incorrect creation of requirements file created")
    print("5. Correct") if pybliometrics_version() else print("5. Incorrect pybliometrics version in requirements file")
    print("6. Correct") if pybliometrics_installation() else print("6. Incorrect pybliometrics installation (version)")


