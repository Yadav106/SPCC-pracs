def clean(input):
    op = ['+', '-', '*', '/', '=']
    input = [i.strip() for i in input]
    input = [i for i in input if len(i) > 0]

    new_input = []
    for i in input:
        split_i = []
        i = i.replace(" ", '')
        temp_str = ""
        for s in i:
            if s in op:
                split_i.append(temp_str)
                split_i.append(s)
                temp_str = ""
                continue
            temp_str += s

        split_i.append(temp_str)

        new_input.append(split_i)
    return new_input

def remove_common_subexpression(input):
    new_expressions = []
    changed = set([])
    encountered = set([])

    for i in range(len(input)):
        curr = input[i]
        encountered.add(curr[0])

        if (curr[2] not in encountered) or (curr[4] not in encountered):
            new_expressions.append(curr)
            encountered.add(curr[2])
            encountered.add(curr[4])
            changed.add(curr[0])
            if curr[2] in changed:
                changed.remove(curr[2])
            if curr[4] in changed:
                changed.remove(4)
            continue

        if (curr[2] in changed) or (curr[4] in changed):
            new_expressions.append(curr)
            changed.add(curr[0])
            if curr[2] in changed:
                changed.remove(curr[2])
            if curr[4] in changed:
                changed.remove(4)
            continue

        j = i-1
        while(j >= 0):
            expr = new_expressions[j]
            if curr[2] == expr[2] and curr[3] == expr[3] and curr[4] == expr[4]:
                curr[2] = expr[0]
                curr[3] = ''
                curr[4] = ''
                break

            j -= 1

        new_expressions.append(curr)
        changed.add(curr[0])
        if curr[2] in changed:
            changed.remove(curr[2])
        if curr[4] in changed:
            changed.remove(curr[4])

    new_expressions = [" ".join(expr) for expr in new_expressions]
    res = "\n".join(new_expressions)
    return res

input_data = []
print("Enter all expressions, write 'end' when finished")
while True:
    user_input = input()
    user_input.strip()
    if user_input.lower() == "end":
        break
    input_data.append(user_input)

cleaned_input = clean(input_data)
print("-------------Output--------------")
print(remove_common_subexpression(cleaned_input))
