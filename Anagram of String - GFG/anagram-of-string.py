# function to calculate minimum numbers of characters
# to be removed to make two strings anagram
def remAnagram(str1,str2):
    arr=[0 for i in range(26)]
    for i in str1:
        arr[ord(i)-ord('a')]+=1
    for i in str2:
        arr[ord(i)-ord('a')]-=1
    count=0
    for i in arr:
        if i!=0:
            count+=abs(i)
    return count
    

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        str1=input()
        str2=input()
        print(remAnagram(str1,str2))
# } Driver Code Ends