# encoding: utf-8

str1 = "abcfbc"
str2 = "abfcab"
itr = 0

def maxLen(str1,len1,str2,len2):
    global itr
    itr = itr + 1
    if len1==0 or len2 == 0:
        return 0
    if str1[len1-1] == str2[len2-1]:
        return 1 + maxLen(str1,len1-1,str2,len2-1)
    else:
        return max(maxLen(str1,len1-1,str2,len2),maxLen(str1,len1,str2,len2-1))

print(maxLen(str1,len(str1),str2,len(str2)))
print(itr)


def aMaxLen(str1,len1,str2,len2):
    mlen = [[0]*(len(str2)+1)]*(len(str1)+1)
    for i in range(1,len1+1):
        for j in range(1,len2+1):
            if str1[i-1] == str2[j-1]:
                mlen[i][j] = mlen[i-1][j-1] + 1
            else:
                mlen[i][j] = max(mlen[i-1][j],mlen[i][j-1])
    print(mlen[len(str1)-1][len(str2) - 1])
aMaxLen(str1,len(str1),str2,len(str2))

