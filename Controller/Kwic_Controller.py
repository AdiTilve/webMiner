# This is a sample Python script.
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from Kwic_Modules import *
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    i=Input()

    i.read_input()
    input_lines=i.get_input()
    for i in input_lines:
        cs=Circular_shift()
        cs.setline(i)
        cs_lines=cs.getline()
        alpha=Alphabetizer()
        alpha.setline(cs_lines)
        alpha_lines=alpha.get_lines()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
