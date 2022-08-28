"""
- 후에는 최대한 많이 더하기
+ 후에는 최대한 적게 더하기
"""
bracket = list(map(str, input().split('-')))

sub = list()

for express in bracket:
    add = list(map(int, express.split('+')))
    sub.append(sum(add))
    
result = sub[0]
for i in range(1, len(sub)):
    result -= sub[i]

print(result)