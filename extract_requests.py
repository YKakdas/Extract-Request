import re
import sys

x=sys.argv.pop()
file=open(x[:-4]+'_requests.txt','w')

for line in open(x):
    s=re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',line)
    correct=False
    if(len(s)!=0):
        str=s.pop()
        temp=str
        for i in range (1,5) :
            if(i!=4):
                str2=str[:str.index('.')]
            else:
                str2=str
            if(int(str2)<=255):
                correct=True
            else:
                correct=False
                break;
            if(i!=4):
                str=str[str.index('.')+1:]
        if(correct==True):
            s2 = re.findall(r'(?:[0-9][0-9]|[1-9]).(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec).'
                            r'(?:19|20)[0-9][0-9].\d{2}.\d{2}.\d{2}', line)
            s3 = re.search(r'(?:POST|GET|HEAD|PUT|DELETE|CONNECT|OPTIONS|TRACE|PATCH)', line)
            s4 = re.search(r'\".\d{3}',line)
            str4=s4.group()[-3:]
            str5=''
            s5 = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}.\-.[a-zA-Z]{1,}.\[',line)
            if (len(s5) != 0):
                str5=s5.pop()
                str5=str5[str5.index('-')+2:len(str5)-2]
            if (len(s2) != 0):
                str3 = s2.pop()
                index = str3.index(':')
                if (str3[1] != '/'):
                    if (int(str3[:2]) <= 31):
                        correct2 = True
                    else:
                        correct2 = False
                if (str3[1] == '/'):
                    str3=('0' + str3[:index] + '   ' + str3[index + 1:] )
                    file.write(str3+'    '+temp+'   '+s3.group()+' '+str4+' '+str5+'\n')
                elif (str3[1] != '/'):
                    if (correct2):
                     file.write(str3[:index] + '   ' + str3[index + 1:]+'    '+temp+'   '+s3.group()+' '+str4+' '+str5+'\n')






