
nums = []

lst = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
#replacements = {"eightwo": "82", "eighthree": "83", "twone": "21", "oneight": "18", "threight":"38"}
replacements1 = { "ei8ht":"eight","t2o":"two", "o1e":"one","th3ee":"three", "4":"four", "fi5e" :"five", "6" :"six", "se7en":"seven",  "n9ne" :"nine", "0":"zero" } 
lns = []
with open("day1.txt", "r") as fo, open("day1-2.txt", "w") as fi:
    for line in fo:
        #for src, target in replacements.items():
            #line = line.replace(src, target)
        for target, src in replacements1.items():
            #content = fi.read()
            line = line.replace(src, target)
        fi.write(line)
'''with open("day1-2.txt", "a+") as fo:
    fo.seek(0)
    for line in fo.readlines():
        print(line)
'''
fi = open("day1-2.txt", "r")
for line in fi.readlines():
    numl = []
    print(line)
    for i in line:     
        if i in lst:
            numl.append(i)
    if len(numl) == 1:
        numl[0] = str(numl[0])
        numl[0] += numl[0]
        numl[0] = int(numl[0])
        nums.append(numl[0])
    elif len(numl) > 1:
        ttl = str(numl[0]) + str(numl[(len(numl)-1)])
        ttl = int(ttl)
        nums.append(ttl)
print(nums)
print(sum(nums))
