def designerPdfViewer(h, word):
    t=[]
    a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in word:
        x=a.index(i)
        t.append(h[x])                                                                          """hackerrank"""
    return max(t)*len(word)
