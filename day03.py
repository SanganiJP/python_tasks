mydict = {
    'nilesh-geography': 89,
    'alpesh-history': 77,
    'shital-math': 93,
    'dimpal-hindi': 68,
    'nilesh-english': 74,
    'alpesh-sci': 85,
    'shital-history': 91,
    'dimpal-geography': 87,
    'nilesh-sci': 83,
    'alpesh-math': 92,
    'dimpal-english': 78,
    'shital-hindi': 81,
    'nilesh-history': 90,
    'alpesh-geography': 79,
    'dimpal-math': 84,
    'shital-sci': 88,
    'nilesh-hindi': 71,
    'alpesh-english': 80,
    'dimpal-sci': 89,
    'shital-geography': 82,
    'nilesh-math': 93,
    'alpesh-hindi': 75,
    'dimpal-history': 90,
    'shital-english': 87
}

total_marks = {}
sub = {}
avg_marks = {}
count = 0

for key,val in mydict.items():
    name = key.split("-")[0]

    if total_marks.get(name):
        total_marks[name] += val
        sub[name] += 1
        #count += 1
        avg_marks[name] = total_marks.get(name)/sub.get(name)

    else:
        total_marks[name] = val
        sub[name] = 1
        #count += 1
        avg_marks[name] = val

print(total_marks)
# print(sub)
# print(avg_marks)

maxMarkspersub = {}

for key,val in mydict.items() :
    subject = key.split("-")[1]
    # print(subject)
    if maxMarkspersub.get(subject):
        maxMarkspersub[subject] = max(maxMarkspersub[subject],val)
    else:
        maxMarkspersub[subject] = val
print(maxMarkspersub)

highestMarks_std = max(total_marks,key = total_marks.get)
print(f'{highestMarks_std} : {total_marks.get(highestMarks_std)}')

highestScore = 0
for n,marks in total_marks.items():
    if highestScore < marks:
        highestScore = marks
        name = n

print(f'Highest Scorer student {name} : marks {highestScore}')

#Sort and display the students based on their total marks from highest to lowest.
#sorted_dict = {key: val for key, val in sorted(total_marks.items(),key = lambda item : item[1], reverse=True)}
#print(sorted_dict)

myvalues = list(total_marks.values())
myvalues.sort()
myvalues.reverse()
print(myvalues)
