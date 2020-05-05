import subprocess


def run_ls():
    lsData = ""
    for line in subprocess.getstatusoutput('ls -l'):
        line = str(line)
        # print("Type of line: ", type(line))
        lsData += line
    return lsData


def run_quit():
    print("Ending program")

# def run_get(name_of_file, sock):
#     pass
#
#
# def run_put(name_of_file, sock):
#     # if os.path.exists(name_of_file):
#     pass
