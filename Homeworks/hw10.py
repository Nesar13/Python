'''
Created on Apr 8, 2016

@author: Nesar Ahmed
Worked with Gorav Kumar
I pledge my honor that I have abided by the Stevens Honor System.
'''
Data ={}
file_name = 'musicrecplus.txt'

def read():
    '''reads a file'''
    F = open(file_name,'r')
    for line in F:
        if line!='\n' and line!='':
            s = line.strip().split(':')
            name = s[0]
            artists = s[1].split(',')
            Data[name]=artists
    F.close()
    
def write():
    '''writes a file'''
    s=''
    F=open(file_name,'w')
    for i in Data:
        prefs = ''
        for a in Data[i]:
            prefs=prefs+a+','
        s += i+':'+prefs[:-1]+'\n'
    F.write(s)
    F.close()
    
def get_name():
    '''gets name '''
    a=input('Enter name (or E to exit): ')
    a=a.strip()
    a=a.title()
    return a

def get_artists():
    '''gets list of artists'''
    L=[]
    while(1):
        m=input('Enter artist (or E to exit): ')
        if m=='E':
            break
        m=m.strip().title()
        L+=[m]
    return L

def artists():
    '''prints favorite artists'''
    read()
    while(1):
        name=get_name()
        if name=='E':
            break
        fav_artists=get_artists()
        Data[name]=fav_artists
    print(Data)
    write()
    
def getrecomm():
    '''gives recommendation'''
    user=get_name()
    if user not in Data:
        print('You must enter preferences first')
        return
    LofMatches=[]
    for i in Data:
        if i!=user:
            x=matches(Data[user],Data[i])
            LofMatches+=[[i,x]]
    bM = bestMatch(LofMatches)
    if bM=='':
        print('No preferences available for you')
        return
    r=drop_matches(Data[user],Data[bM])
    return r
    
def matches(l1,l2):
    '''shows matches'''
    l1.sort()
    l2.sort()
    result=0
    i=0
    j=0
    while i<len(l1) and j<len(l2):
        if l1[i]==l2[j]:
            result+=1
            i+=1
            j+=1
        elif l1[i]<l2[j]:
            i+=1
        else: 
            j+=1
    return result  
 
def drop_matches(l1,l2):
    '''discard matches'''
    l1.sort()
    l2.sort()
    result=[]
    i=0
    j=0
    while i<len(l1) and j<len(l2):
        if l1[i]==l2[j]:
            i+=1
            j+=1
        elif l1[i]<l2[j]:
            result.append(l1[i])
            i+=1
        else: 
            result.append(l2[j])
            j+=1
    while i < len(l1):
        result.append(l1[i])
        i+=1
    while j<len(l2):
        result.append(l2[j])
        j+=1
    return result
    
def bestMatch(L):
    '''shows the best match'''
    max=0
    bm=''
    for i in L:
        if i[1]>max:
            max=i[1]
            bm=i[0]
    return bm

def mostPopArtist(Data):
    '''Determines the artist with the most likes'''
    artistDict = {}
    popularity = 0 
    for i in Data:
        for j in Data[i]:
            if j in artistDict:
                artistDict[j] += 1
            elif j not in artistDict:
                artistDict[j] = 1
    mostPopVotes = max(artistDict.values())
    popDict = {}
    for i in artistDict:
        if artistDict[i] == mostPopVotes:
            popDict[i] = artistDict[i]
    return list(popDict.keys())

def howPopArtist(Data):
    '''Looks for how many times each artists occurs in user preferences and returns the number of occurences'''
    artistDict = {}
    popularity = 0 
    for i in Data:
        for j in Data[i]:
            if j in artistDict:
                artistDict[j] += 1
            elif j not in artistDict:
                artistDict[j] = 1
    return max(artistDict.values())

def mostLikes(Data):
    '''Determines the user with the most preferences'''
    likesDic = {}
    L = list(Data.keys())
    for i in Data:
        likesDic[i] = 0
        for j in Data[i]:
            likesDic[i] += 1
    likes = max(likesDic.values())
    anotherDic = {}
    for i in likesDic:
        if likesDic[i] == likes:
            anotherDic[i] = likes
    L2 = list(anotherDic.keys())
    for keys, values in Data.items():
        if keys in L2:
            if '$' in keys:
                print('This user has opted out of this feature.')
                return 'NA',values
            else:
                return keys, values
         
def main():
    read()
    while(1):
        x = ''
        while x != 'q':
            print('Enter a letter to choose an option:')
            print(' e - enter preferences ')
            print(' r - get recommendations')
            print(' p - show most popular artists')
            print(' h - how popular is the most popular')
            print(' m - which user has the most likes')
            x = input(' q - save and quit\n')
            if x == 'e':
                get_artists() 
            elif x == 'r':
                print(getrecomm())
            elif x == 'p':
                print(mostPopArtist(Data))
            elif x == 'h':
                print(howPopArtist(Data))
            elif x == 'm':
                print(mostLikes(Data))
            elif x == 'q':
                write()
                return
            else:
                print('dummy, thats not a choice')
main()           