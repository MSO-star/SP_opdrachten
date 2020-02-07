
def gemmidelde(list):
    x= sum(list)/len(list)



def gemidelde(list):
    count= 0
    totaal= 0
    for n in list:
        for i in n:
          count= count+1
          totaal= totaal+ i
    return totaal/count

print(gemidelde([[1,2,4],[1,9,3]]))
