## Don't Use `split` function , you are allowed to grab your Customized Find Function
#customized_find
def customized_find(sent , char):
    return [i for i , j in enumerate (sent) if j == char ]
#customized_split
def customized_split (sent ,char ):
    lst= customized_find(sent,char)
    final = []
    string=''
    string = sent[:lst[0]]
    final.append(string)
    for i in range (len(lst)-1):
        string= sent[lst[i]+1:lst[i+1]]
        final.append(string)
    string = sent[lst[-1]+1:]
    final.append(string)        
    
    
    return final 

print(customized_find('abcabcabc', 'c'))
print(customized_split('abcabcabcijwSIOFHASUOFAUIFA', 'c'))
