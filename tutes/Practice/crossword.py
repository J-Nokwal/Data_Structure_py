

# Complete the crosswordPuzzle function below.
def crosswordPuzzle(word_pos=0):
    if word_pos<len(words):
        wrd=words[word_pos]
        print("wrdwrdwrd: ",wrd)
    elif word_pos==len(words): 
        global waitForYes
        waitForYes = True
        return
    lenMatrix=len(crossword)
    for i in range(lenMatrix):
        for j in range(lenMatrix):
            if crossword[i][j]=='-' or crossword[i][j]==wrd[0]:
                if (canWePassHorizontal(wrd,i,j)):
                    boolValues=placeHorizontal(wrd,i,j)
                    crosswordPuzzle(word_pos=word_pos+1)
                    if waitForYes==True: return
                    unPlaceHorizontal(wrd,i,j,boolValues)
                if (canWePassVertical(wrd,i,j)):
                    boolValues=placeVertical(wrd,i,j)
                    crosswordPuzzle(word_pos= word_pos+1)
                    if waitForYes==True: return
                    unPlaceVertical(wrd,i,j,boolValues)
    if word_pos==len(words):
        return crossword
    print(wrd," Dont work")
    
def canWePassHorizontal(wrd,i,j):
    #print("hwrd: ",wrd,"i: ",i,"j: ",j)
    if j-1>=0 and  crossword[i][j-1]!='+':
        #print("hhhhh1")
        return False
    elif j+len(wrd)<10 and crossword[i][j+len(wrd)]!='+' :
        return False
    k=0
    while(k<len(wrd)):
        if j+k >=10:return False
        #print("1111111kcrossword[i+k][j] ",crossword[i+k][j],"wrd[k+1] ",wrd[k])
        if crossword[i][j+k]=='-' or crossword[i][j+k]==wrd[k]:
            k+=1
            continue
        else: 
            #print(wrd[k])
            return False
        k+=1
    return True
def canWePassVertical(wrd,i,j):
    #print("vwrd: ",wrd,"i: ",i,"j: ",j)
    if i-1>=0 and crossword[i-1][j]!='+':
        #print("vvvvv1")
        return False
    elif i+len(wrd)<10 and crossword[i+len(wrd)][j]!='+':
        #print("vvvvv2",+len(wrd)<10 ,crossword[i-1][j]!='+', crossword[i-1][j]!='X')
        return False
    k=0
    while(k<len(wrd)):
        if i+k >=10:return False
        #print("1111111kcrossword[i+k][j] ",crossword[i+k][j],"wrd[k+1] ",wrd[k])
        if crossword[i+k][j]=='-' or crossword[i+k][j]==wrd[k]:
            k+=1
            continue
        else: 
            #print(wrd[k])
            return False
        k+=1
    return True



def placeHorizontal(wrd, i,j):
    boolValues=[]
    print("wrd: ",wrd)
    for ii in wrd:
        if crossword[i][j]=='-':
            crossword[i][j]=ii
            boolValues.append(True)
        elif crossword[i][j]==ii:
            boolValues.append(False) 
        j+=1
    print(boolValues)
    for i in crossword:
        print(i)
    return boolValues

def placeVertical(wrd, i,j):
    boolValues=[]
    print("vwrd: ",wrd)
    for jj in wrd:
        if crossword[i][j]=='-':
            crossword[i][j]=jj
            boolValues.append(True)
        else:
            boolValues.append(False) 
        i+=1
    print(boolValues)
    for i in crossword:
        print(i)
    return boolValues

def unPlaceHorizontal(wrd,i,j,boolValues):
    print("123456k",len(wrd))
    for ii in range(len(wrd)):
        print(ii)
        if boolValues[ii]==True:
            crossword[i][j+ii]='-'

def unPlaceVertical(wrd,i,j,boolValues):
    for jj in range(len(wrd)):
        # print("jj: ",jj,"wrd: ",wrd)
        if boolValues[jj]==True:
            crossword[i+jj][j]='-'

        
if __name__ == '__main__':

    crossword = []
    
    ls="""XXXXXX-XXXXX------XXXXXXXX-XXXXXXXXX-XXXXXX------XXXXXXX-X-XXXXXXX-X-XXXXXXXXX-XXXXXXXXX-XXXXXXXXX-X"""
    ls="""+-+++++++++-+++++++++-------+++-+++++++++-+++++++++------++++-+++-+++++++++-+++++++++-++++++++++++++"""
    for _ in range(10):
        #crossword_item = input('crossword')
        crossword_item = ls[(0+10*_):(10+10*_)]
        crossword_item= list(crossword_item)
        crossword.append(crossword_item)

    cross=False
    for i in range(10):
        for j in range(10):
            if crossword[i][j]=='X':
                #print(j)
                cross=True
                crossword[i][j]='+'
    for i in crossword:
        print(i)
    #words = input('names')
    words ='ICELAND;MEXICO;PANAMA;ALMATY'
    words='AGRA;NORWAY;ENGLAND;GWALIOR'
    words=words.split(';')
    global waitForYes
    waitForYes=False
    result = crosswordPuzzle()
    if cross:
        for i in range(10):
            for j in range(10):
                if crossword[i][j]=='+':
                    crossword[i][j]='X'
    for i in crossword:
        str1=''
        i=str1.join(i)
        print(i)
    #'+'