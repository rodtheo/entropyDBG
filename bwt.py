import os
from collections import OrderedDict
from operator import itemgetter
os.chdir(".")
f=open("seq.in","r")
lines=f.readlines()
s=lines[0].strip()+'$'
p=lines[1].strip()
msa=list()
for i in range(2,len(lines)):
    msa.append((int(lines[i].split()[0]),int(lines[i].split()[1]),int(lines[i].split()[2])))

print(p)

def suffixarray(s):
    suff=list()
    for i in range(len(s)):
        suff.append((i,s[i:]))
    suff_arr=sorted(suff,key=itemgetter(1))
    return list(map(lambda x: x[0], suff_arr))

def bwt(s):
    bw=list()
    for i in suffixarray(s):
        if i==0: bw.append("$")
        else: bw.append(s[i-1])
    return ''.join(bw)

sa=suffixarray(s)
bw=bwt(s)
print(bw)
print("sa:", sa)
def rankbwt(bw):
    rank=list()
    totals={}
    for c in bw:
        if c not in totals:
            totals[c]=1
            rank.append(0)
        else:
            rank.append(totals[c])
            totals[c]+=1
    return totals, rank


def firstcol(tots):
    first={}
    i=0
    for c in sorted(tots):
        first[c]=i
        i+=tots[c]
    return first

totals, rank=rankbwt(bw)
first=firstcol(totals)
#print(first)
bits=list()
print(first)
print("rank=", rank)
print("totals:", totals)
print("msa:", msa)

def overlap():
        return 0

def bsearch(bw,p):
    l=first[p[-1]]
    r=l+totals[p[-1]]
    i=len(p)-2
    n_occ=0
    l_extra=list()
    while i>=0 and (l<r or l_extra):
        extra=[]
        l_last_extra=[]
    #    print(l_extra)
    #    print(list(map(lambda x:sa[x],l_extra)))
        z=l
        if i!=0:
            for j in range(len(msa)):
                while bw[z:r].find(str(j))!=-1:
                    f=bw[z:r].find(str(j))
                    jc=str(j)
                    print("c:", jc)
                    print("z:",z,"r:",r, "f:", f)
                    print("sa[z+f]=", sa[z+f])
                    # a operacao abaixo eh verdadeira quando a marcacao
                    # do sitio analisada no BWT marca o final do mesmo
                    if sa[z+f]==msa[j][0]+(msa[j][1]+1)*msa[j][2]:
                        print("msa[j][0]=", str(msa[j][0]+(msa[j][1]+1)*msa[j][2]))
                        # quando este eh o caso adicionamos a lista
                        # extra da posicao dos alelos
                        l_alts=first[str(j)]
                        r_alts=l_alts+totals[str(j)]
                        extra.extend(range(l_alts,r_alts))
                    elif sa.index(msa[j][0]) not in extra:
                        print("extra not in")
                        # inicio do sitio
                        extra.append(sa.index(msa[j][0]))
                    print("extra=", extra)
                    z=z+f+1
                for jj in l_extra:
                    jc=str(j)
                    #print("c:", jc)
                    if bw[jj]==str(j):
                        print("l_extra LOOOOOOP")
                        if sa[jj]==msa[j][0]+(msa[j][1]+1)*msa[j][2]:
                            l_alts=first[str(j)]
                            r_alts=l_alts+totals[str(j)]
                            extra.extend(range(l_alts,r_alts))
                        elif sa.index(msa[j][0]) not in extra:
                            extra.append(sa.index(msa[j][0]))
        #print(list(map(lambda x:sa[x],extra)))
        print("l=",l,"r=",r,"p[i]=",p[i])
        if extra:
            for j in extra:
                if bw[j]==p[i]:
                    l_last_extra.append(j)
                    print("l_last extra:", l_last_extra)
        if l_extra:
            for jj in l_extra:
                if bw[jj]==p[i]:
                    l_last_extra.append(jj)
                    print("l_last l_extra:", l_last_extra)
        if bw[l:r].find(p[i])!=-1:
            print("l={},r={},find bw[l:r].find(p[i]={})={}".format(l,r,p[i],bw[l:r].find(p[i])))
            l_last=l+bw[l:r].find(p[i])
            print("l=",l,"l_last=", l_last)
        else:
            l=-1
            r=-1
            print("else l_last_extra", l_last_extra)
            if not l_last_extra:
                return 0, 'n'
        if bw[l:r].rfind(p[i])!=-1:
            # repare que aqui usamou rfind (hightest index)
            r_last=l+bw[l:r].rfind(p[i])
            print("r=",r,"r_last=", r_last)
        if l>=0:
            l=first[p[i]]+rank[l_last]
            r=first[p[i]]+rank[r_last]+1
            print("Update: l=",l,"r=", r)
        if l>=r:
            l=-1
            r=-1
            if not l_last_extra:
                return 0, 'n'
        if l_last_extra:
            l_extra=list(map(lambda x:first[p[i]]+rank[x],l_last_extra))
            print ("l_extra map=", l_extra, "p[i]=", p[i])
        else: l_extra=[]
        i=i-1
        print("i decremented ---------------")
    offsets=list()
    if i<0:
        print("Going i<0")
        if r<l:
            n_occ=r-l
            offsets.extend(sa[l:r])
            offsets.append('o')
        if l_extra:
            n_occ+=len(l_extra)
            offsets.extend(list(map(lambda x:sa[x],l_extra)))
    return n_occ,offsets

print(bsearch(bw,p))
