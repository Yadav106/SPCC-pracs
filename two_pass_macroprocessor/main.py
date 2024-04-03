from prettytable import PrettyTable
mdt_table = PrettyTable()
mnt_table = PrettyTable()

def clean(input):
    input = input.split("\n")
    input = [i.strip() for i in input]
    return input
    

def phase_one(input):
    for line in range(len(input)):
        # print(i)
        i = input[line]
        temp = i.split(' ')
        # print(temp)
        if len(temp) > 2 and temp[1].lower() == 'macro':
            # print(i)
            index = len(MDT)
            MNT.append([index, temp[0]])
            line += 1
            while line < len(input):
                curr = input[line]
                MDT.append(curr)
                curr_split = curr.split(' ')
                if curr_split[0].lower() == 'endm':
                    break
                line += 1

    print_mdt()
    print_mnt()

def check_for_macro(line):
    if len(line) < 2:
        return -1
    
    for name in MNT:
        if line[0] in name and line[1].lower() != 'macro':
            return name[0]

    return -1

def phase_two():
    # print(input)
    res = []
    for i in range(len(input)):
        line = input[i]
        temp = line.split(' ')
        index = check_for_macro(temp)
        if index != -1:
            while (MDT[index].lower() != "endm"):
                temp_line = MDT[index]
                if 'XX' in temp_line:
                    temp_line = temp_line.replace("XX", temp[1])
                res.append(temp_line)
                index += 1
        else:
            res.append(line)
    return res

def print_mdt():
    mdt_table.field_names = ["Index", "MDT"]
    for i in range(len(MDT)):
        mdt_table.add_row([i, MDT[i]])
    print(mdt_table)

def print_mnt():
    mnt_table.field_names = ["Index", "MNT"]
    for name in MNT:
        mnt_table.add_row([name[0], name[1]])
    print(mnt_table)

# MDT : Macro Definition Table
MDT = []
# MNT : Macro Name Table
MNT = []

input = ""
with open('input.asm','r') as f:
    input = f.read()

input = clean(input)
# print(input)
phase_one(input)
res = phase_two()

print('\n--------------OUTPUT--------------------')
for i in res:
    print(i)
