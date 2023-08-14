# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()

W, R = user_input.split()
RM = int(W) * (1+int(R)/30)
print(int(RM))