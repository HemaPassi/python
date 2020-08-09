#for number in range(1,10,2):
# print(number)

students = {
    "male" : ['anil', 'akash', 'som'],
    "female" : ['anu', 'barkha', 'seema'] 
    }
for key in students.keys():
    for name in students[key]:
        if 'a' in name:
         print(name)


# list comperhensions - it works with numbers/ string etc
even_numbers = [x for x in range(1,101) if x % 2 == 0 ]
print(even_numbers)

words = ['the', 'quick', 'brown', 'fox', 'jumps']
answer = [[w.upper(), w.lower(), len(w)] for w in words]
print(answer)
[['THE', 'the', 3], ['QIUICK', 'quick', 5], ['BROWN', 'brown', 5] ... ]]
 
