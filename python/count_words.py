countWordDic={}
specialChar=['.',',','\"','\'','!','?','\n',':','-','/']

with open('the_little_prince.txt', 'r') as file:
    while True:
        data=file.readline()
        if not data: break
        if data=='\r' or data=='\n' or data=='\t':
            continue
        else:
            tmpList=[]

            for i in specialChar:
                if i in data:
                    data=data.replace(i, '')

            tmpList=data.split(' ')
            # tmpList is one line continually
            print('Start split words by one line.\n')

            for j in tmpList: #get j index of data to one line

                print('',end='.')
                if j in countWordDic.keys() :
                    countWordDic[j]=countWordDic[j]+1
                else :
                    countWordDic[j]=1
            print('\n')
    print('End count words.\n')

print('Sort Dictionary.\n')
#make sort list
sortDic=sorted(countWordDic.items(), reverse=False, key=lambda item:item[1])
for i in sortDic:
    print(i)
	
'''execute result
...
('He', 74)        
('from', 74)      
('this', 76)      
('him', 77)       
('had', 79)       
('will', 80)      
('as', 80)        
('very', 81)      
('with', 92)      
('all', 93)       
('on', 94)        
('at', 96)        
('It', 102)       
('be', 106)       
('one', 107)      
('his', 114)      
('for', 115)      
('But', 116)      
('The', 128)      
('are', 131)      
('And', 142)      
('have', 145)     
('my', 146)       
('me', 151)       
('not', 156)      
('it', 160)       
('in', 170)       
('prince', 189)   
('was', 193)      
('said', 195)     
('and', 212)      
('he', 226)       
('you', 233)      
('little', 255)   
('that', 281)     
('is', 301)       
('of', 337)       
('a', 399)        
('to', 453)       
('I', 546)        
('the', 889)
'''  