liste1=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
liste2=[[1, 2], [3, 4], [5, 6, 7]]

def parcala(liste):
    '''
    iç içe listeleri düzleştiren fonksiyon
    '''
    if type(liste)==list:
        return [i for item in liste for i in parcala(item) ]
    return [liste]
print(parcala(liste1))

def terscevir(liste):
    '''
    iç içe listeleri tersine çeviren fonksiyon
    '''
    if type(liste) == list:
        liste.reverse()
    for i in liste:
        if type(i) == list:
            terscevir(i)
        else:
            break
    return [liste]


print(terscevir(liste2))












