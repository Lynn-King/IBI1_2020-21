import re
fastq = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
count = 0
all = ''
names = []
number = []
dic = {}
for line in fastq:
    s=str(line)
    if re.search('>',line):
        key=line
        dic[key]=''
    else:
        ori=dic[key]
        dic[key]=ori + line
for key in dic.keys():
    if re.search('unknown_function',key):
        name = str(key)
        output = re.findall(r'^>([^ ]+)_mRNA',key)
        print(output,len(dic[key]))
        print(dic[key])
file=open('unknown_function.fa','w')
for key in dic.keys():
    name = str(key)
    output = re.findall(r'^>([^ ]+)_mRNA',key)
    cc = len(dic[key])
    cc = str(cc)
    output=str(output)
    file.write(output)
    file.write(cc)
    file.write('\n')
                        

