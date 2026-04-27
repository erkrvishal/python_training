import re

# pattern = '^a...s$'
# test = 'alias'

# result = re.match(pattern, test)
# # print(result.end())
# if result:
#     print("Search successful")
# else:
#     print("Search unsuccessful")



''' re.findall() - Returns a list of strings containing all matches

    re.split() - Splits the strings where there is a match & 
        returns a list of strings where the split occurred.
        'abc' -- input
        b -- matching
        ['a','c'] -- output
        
    re.sub() - re.sub(pattern, replace, string) - returns a string 
                where matched occurrences are replaced with the content 
                of replace variable.
                
    re.subn() - returns the tuple containing new string and number of substitutions made
    "abc","acd" -> string
    a -> search
    z -> replace character
    re.subn()
    ('zbc','zcd'),2
    
    re.search() - it looks for the 1st location where the RegEx pattern
                    produces a match'''


'''Match Objects:
   match.group() - returns the part of the string where there is a match
   match.start() - returns the first index matched
   match.end() - returns the end of the index

'''


string = "Hello 12 34 hi 45"
pattern = '\d+'

# result = re.search(pattern, string)
result = re.match(pattern, string)
print(result)

if result:
    print(result.group())
    print(result.start())
    print(result.end())
    print("Search successful")
else:
    print("Search unsuccessful")



