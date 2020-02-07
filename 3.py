#a. Funsctie berekent hoe vaak een  getal x in een lijst voorkomt.
def count(getal, list):
    count_getal= 0

    for i in (list):
        if  i == getal:
            count_getal = count_getal+1
    print("De gegeven getal komt", count_getal, "voor")
count(3, [2,3,4,4,4,4,3,4,4])



#b. functie die in een gegeven lijst het grootste verschil tussen twee op een volgende getallen bepaalt.

def grootste_verschil():
    list = [2, 3, 4, 4, 4, 4, 3, 4, 4]
    list_sort= sorted(list)
    verschil=   list_sort[-1] - list_sort[0]
    print("Het grootste verschil is :",verschil,",Tussen de getallen", list_sort[-1], "en", list_sort[0])


grootste_verschil()



# C
def een_nul():
    list= [1,1,1,1,0,0,0,0]
    nul= 0
    een= 0
    resultaat= True
    for i in list:
        if i == 0 :
            nul+=1
        elif i ==1:
            een+=1

    if een > nul and nul <= 12:
        resultaat= True
    else:
        resultaat= False
    print(resultaat)

een_nul()