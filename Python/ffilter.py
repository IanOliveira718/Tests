def par (i):
    if(i%2==0):return(True);
    else:return(False);
def ffilter (f,l):
    l1=[];
    for i in range(0,len(l)-1):
        if(f(l[i])):
            l1.append(l[i]);
    return l1
            
print(ffilter(par,[1,2,3]))
