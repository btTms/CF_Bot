from cmath import exp
import os
import string


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    ASHGREY = '\033[90m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\x1B[3m'
    ITALIC_AND_BOLD = '\x1B[1;3m'
    
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

os.system("color")


with open("expected_output.txt", 'r') as f:
    nr_of_line = len(f.readlines())

f.close()

inp = open("in.txt", "r")
nr_of_test_cases = inp.readline()
inp.close()

my_output = open("mo.txt", "r")

expected_output = open("expected_output.txt", "r")

'''last_line = expected_output.readlines()[-1]

if(last_line != " "): 
    expected_output.write("\n ")
else:
    nr_of_line -= 1'''

constant = int(nr_of_line / int(nr_of_test_cases))
cnt = 0


for i in range(int(nr_of_test_cases)):

    print(colored(91, 110, 225, "Test case #" + str(i + 1) + ": "), end = "\n\n")

    e_o_list = list()
    m_o_list = list()

    is_ok = True

    for line in range(constant):

        e_o_line = expected_output.readline()
        m_o_line = my_output.readline()

        e_o_list.append(e_o_line)
        m_o_list.append(m_o_line)

        if(e_o_line == m_o_line):
            cnt += 1
        else:
            is_ok = False

    print(colored(55, 148, 110, "Expected output:"))

    print(*e_o_list, end = "")
    print(colored(51, 51, 51, "----------------"))
    print(colored(145, 145, 145, "Your output:"))
    print(*m_o_list, end = "")

    print(colored(105, 105, 106, "Verdict:"), end = "")

    if(is_ok):
        print(f"{bcolors.OKGREEN}Correct output!{bcolors.ENDC}")
    else:
        print(f"{bcolors.FAIL}Incorrect output!{bcolors.ENDC}")

    print("")


print(colored((int(nr_of_test_cases) - cnt) * 50 + 145, (cnt * 10) + 145, 100, str(int(nr_of_test_cases))+ "/" + str(cnt) + " tests passed!"))

expected_output.close()
my_output.close()
