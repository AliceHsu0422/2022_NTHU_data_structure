n = int(input()) #enter no of strings
l = [] #list for storing input
flag = False #this flag determines wether the inputs satisfy constraints or not
#User input
for i in range(n):
    l.append(input().lower())
    #checking Constraints
if (1 <= n <= 10):
    for i in l:
        if(1 <= len(i) <= 10**5):
            flag = True
        else:
            flag = False
            break

if(flag):
    index = 0
    for i in l:
        s = [] #For storing splitted strings
        ress = [] #for storing the resultant string
        i+=']' #adding at the end to split the string using the brackets.
        res = '' #Temporary variable for split operations

        #Splitting the string based on brackets
        for j in i:
            if(j == '[' or j == ']'):
                if(res!=''): #if it is not consecutivee repeated operations
                    s.append(res)
                    s.append(j)
                else:
                    s.append(j)
                res = '' #making result to empty for new string
            else:
                res+=j #creating the string before operations
        original_str=[]
        char_index=0
        for idx,word in enumerate(s):
            if (word == '['):
                char_index = 0
            elif (word == ']'):
                char_index = len(original_str)
            else:
                original_str.insert(char_index,s[idx])
                char_index+=1
        original_str=''.join(original_str)
        print(original_str)
        
        
        
        
        
        
        
        
        
    