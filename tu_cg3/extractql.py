import re
teststring = "helloworld hhh test wowo"
def word_count(file_name):
    import collections
    word_freq = collections.defaultdict(int)
    with open(file_name) as f:
        for l in f:
            for w in l.strip().split():  
                word_freq[w] += 1
    return word_freq
def regtest(file_name):
    mlist = []
    with open(file_name) as f:
        txt = f.read().replace('\n', '')
    x = re.search("wo", txt)
    print(x.start())
    cur = -1
    while x != None:
        cur = cur + 1 + x.start()
        x = re.search("wo", txt[cur+1:])
        if x != None:
            print(cur+1 + x.start())
    return mlist
def extractp(file_name):
    resulttxtlist = []
    with open(file_name,encoding='utf-8') as f:
        for linetxt in f:
        #linetxt = f.readline():
            #print(linetxt)
            x = re.search("qq ", linetxt)
            splitslide = re.search("---", linetxt)
            sectionmark = re.search("ok-", linetxt)
            preservmark = re.search("> ", linetxt)
            if preservmark != None:
                resulttxtlist.append(linetxt)
            if sectionmark != None:
                resulttxtlist.append(linetxt)
            if splitslide != None:
                resulttxtlist.append(linetxt)
            if x != None:
                resulttxtlist.append(linetxt)
    resulttxtlist.append("\n---\n")            
    with open(file_name,encoding='utf-8') as f:
        for linetxt in f:
        #linetxt = f.readline():
            #print(linetxt)
            linetxt = linetxt.lstrip()
            preservmark_1 = re.search("lan ", linetxt)
            if preservmark_1 != None:
                resulttxtlist.append("\t\t"+linetxt)
    #print(resulttxtlist)
    with open("question_list_extraction.txt","w",encoding='utf-8') as fout:
        for l in resulttxtlist:
            fout.write(l)
extractp("mixed.txt")

#split()