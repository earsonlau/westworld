# def printallsubsequence(str,index,ans,path):
#     if index == len(str):
#         ans.append(path)
#         return
#     no = path
#     printallsubsequence(str,index+1,ans,no)#选择1：不要str[index]
#     yes = path + str[index]
#     printallsubsequence(str,index+1,ans,yes)#选择2：要str[index]

# ans=[]
# printallsubsequence("abc",0,ans,"")
# print(ans)
def printallsubsequence_no_repeat(str,index,ans,path):
    if index == len(str):
        ans.add(path)
        return
    no = path
    printallsubsequence_no_repeat(str,index+1,ans,no)#选择1：不要str[index]
    yes = path + str[index]
    printallsubsequence_no_repeat(str,index+1,ans,yes)#选择2：要str[index]
ans=set()
printallsubsequence_no_repeat("abc",0,ans,"")
print(ans)