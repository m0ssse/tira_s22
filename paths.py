#ratkaisu perustuu seuraavaan havaintoon: jos joukosta 2...99 valitaan n:n alkion osajoukko,
#niin tällöin sellaisten polkujen määrä, jossa kuljetaan vain tämän osajoukon alkioiden kautta
#on korkeintaan 2**n, kun huomioidaan tapaus, jossa kuljetaan suoraan 1->100. näin ollen voidaan
#etsiä pienin sellainen n, että 2**n>=x. kun tämän joukon kaikki solmut yhdistetään keskenään kaarilla
#ja lisäksi lisätään kaaret luvusta 1 näihin kaikkiin solmuihin sekä kaaret näistä solmuista solmuun 100
#(yht. n*(n-1)/2+2*n), saadaan juurikin 2**n polkua. tämä on yleensä liikaa, joten polkuja voidaan vähentää
#kun huomioidaan seuraava

#joukon alkioiden kautta kulkevat polut voidaan esittää binäärilukuina siten, että jos polkuu kulkee joukon i:nnen
#alkion kautta, on luvun i:s bitti 1 ja muuten 0. nyt jos poistamme i:nnen alkion ja luvun 100 välisen kaaren, kelvollisia
#polkuja eivät ole enää sellaiset, jotka päättyisivät kyseiseen alkioon. näin ollen olemme vähentäneet polkujen määrää luvun
#2**i verran. (esimerkiksi jos joukossa on alkiot 2...10 ja poistamme alkion 2 ja 100 välisen kaaren, olemme poistaneet tasan yhden polun
#jos poistamme alkion 3 ja 100 välisen kaaren, olemme poistaneet kaksi polkua: 1->3->100 ja 1->2->3->100 jne.

#näin ollen kun esitämme binäärilukuna poistettavien polkujen kokonaismäärän, voimme päätellä ne luvut, joista pitää poistaa suoraan lukuun
#100 johtava kaari

#palataksemme edelliseen esimerkkiin: joukossa on alkiot 2...10, joten tämän joukon kautta saadaan yhteensä 2**9=512 polkua. oletetaan nyt, että
#x=487, jolloin ylimääräisiä polkuja on 25. 25 on binäärilukuna 11001. näin ollen meidän pitää poistaa seuraavista solmuista kaaret solmuun 100: 2, 5 ja 6,
#mikä saadaan lukemalla binääriesitys käänteisessä järjestyksessä


from math import ceil, log

def create(x):
    n=ceil(log(x)/log(2))
    N=2**n
    excess=N-x
    exc2bin=bin(excess)[2:]
    remto100=exc2bin[::-1]
    midpoints=list(range(2, 2+n))
    edges=[(1,100)]
    for i in range(len(midpoints)):
        edges.append((1, midpoints[i])) #lisätään kaari solmusta 1 käsiteltävään solmuun
        for j in range(i+1, len(midpoints)):
            edges.append((midpoints[i], midpoints[j]))
        if i<len(remto100):
            if remto100[i]=="0":
                edges.append((midpoints[i],100))
        else:
            edges.append((midpoints[i], 100))
    return edges
    

if __name__ == "__main__":
    print(create(2)) # esim. [(1,2),(1,100),(2,100)]
    print(create(8))
    print(create(7))
##    print(create(10))
##    print(create(123456789))
