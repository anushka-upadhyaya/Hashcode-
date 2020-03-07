import heapq

import os
for file in (os.listdir('req')):
    # file='d_tough_choices.txt'
    with open("./req/"+file) as f:
        r=(([list(map(int,a.strip().split())) for a in f.readlines()]))

    books,days,libraries=r[0]
    scores={i:r[1][i] for i in range(0,len(r[1]))}
    data=[]
    # print(len(r))
    for i in range(2,len(r),2):
        try:
            data.append([r[i],r[1+i]])
        except Exception as e:
    #         # print(i,libraries,file,end=" ")
            continue
    # # data = [[r[i],r[i+1]] for i in range(2,len(r),2)]

    class PrioritySet(object):
        def __init__(self,l=[]):
            heapq.heapify(l)
            self.heap = l
            self.S = set()

        def add(self, d):
            if not d in self.S:
                heapq.heappush(self.heap, d)
                self.S.add(d)
                return True
            return False

        def get(self):
            pri, d = heapq.heappop(self.heap)
            self.S.remove(d)
            return d


    value_of_each=[]
    sizes=[]
    sizes=PrioritySet(sizes)
    k=[]
    for elem in data:
        value=0
        power=1
        unique=len(sizes.heap)
        for i in range(len(elem[1])):
            if(sizes.add(elem[1][i])):
                power+=scores[elem[1][i]]
            value+=scores[elem[1][i]]
        days_taken=elem[0][1]+(elem[0][0]/elem[0][2])
        # print(value,power,days_taken,days_taken*power)
        unique=len(sizes.heap)-unique
        if(unique==0):
            value_of_each.append(-1)
            continue
        # value_of_each.append(days_taken*power)
        value_of_each.append(value*power)
        k.append([value,power,days_taken,days_taken*power," "])
        
    # print()
    d={i:value_of_each[i] for i in range(len(value_of_each))}
    print(d)
    # if not os.path.exists('./debug'):
    #     os.mkdir('debug')
    

    order = []
    for i in sorted(d.items(),key=lambda x: x[1]):
        if(i[1]!=-1):
            # print(1/0)
            order.append(i[0])
    # print(order)

    with open('./debug/'+file[:-4]+'_debug.txt','w') as f:
        f.writelines(str(order))
        f.write('\n')
        
    s=[]
    print(len(data))

    s.append([len(order)])

    for i in range(len(order)):
        print(order[i],data[order[i]][0][0])
        s.append([order[i],data[order[i]][0][0]])
        s.append(data[order[i]][1])
        for elem in data[order[i]][1]:
            print(elem,end=" ")
        print()
    k=([" ".join(list(map(str,l)))+'\n' for l in s])
    if not os.path.exists('./out'):
        os.mkdir('out')

    with open('./out/'+file[:-4]+'_out.txt','w') as f:
        # f.writelines(k)
        for i in range(len(k)):
            f.write(k[i])
            # f.write('\n')
    # break