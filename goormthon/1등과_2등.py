user_input = input()

idx12 = user_input.find('12')
idx21 = user_input.find('21', idx12+2)
if idx12 != -1 and idx21 != -1:
    print("Yes")
else:
    idx21 = user_input.find('21')
    idx12 = user_input.find('12', idx21+2)
    if idx12 != -1 and idx21 != -1:
        print("Yes")
    else:
        print("No")