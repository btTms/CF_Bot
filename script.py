import os
from typing import final

current_dir = os.getcwd()

folder_name = input("What's the folder's name to be created? \n")


folder_made = os.path.join(current_dir, folder_name)

if not os.path.exists(folder_made):
    os.mkdir(folder_made)

os.chdir(folder_made)

current_dir = os.getcwd()

nr_of_dirs = input("Number of directories to be made: \n")

for i in range(int(nr_of_dirs)):

    template_txt = open(r'D:\Informatika\CF_bot\template.txt')

    final_dir = os.path.join(current_dir, "Problem " + chr(65 + i))

    if not os.path.exists(final_dir):
        os.mkdir(final_dir)

    else:
        for l in os.listdir(final_dir):
            os.remove(os.path.join(final_dir, l))

    n = os.path.join(final_dir, "in.txt");    
    e = os.path.join(final_dir, "expected_output.txt")
    m = os.path.join(final_dir, "mo.txt")
    c = os.path.join(final_dir, "sol.cpp")

    cpp = open(c, "w")
    for line in template_txt:
        cpp.write(line)
    cpp.close()

    input = open(n, "w")
    input.close()

    expected = open(e, "w")
    expected.close()

    mine = open(m, "w")
    mine.close()

print("Working on it...")
print("----------------")
print("Done!")
