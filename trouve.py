from random import *
from math import *


def final(proba2, somme2):
    TheBF = "N"
    TheBN = choice(range(1, (somme2 + 1)))
    print(TheBN)
    print("tttyty")
    somme2 = 0
    for a in proba2:
        somme2 += proba2[a]
        if TheBN <= somme2 and TheBF[0] != "T":
            TheBF = a
    return TheBF


def trouvedepart(blockF2, couche2):
    block2 = {}
    for c in blockF2:
        block2[c] = blockF2[c][0]

    def calcul(x2, proba2):
        VnombreM2 = {}
        for a in proba2:
            VnombreM2[a] = 0
        Nmodif2 = []
        total2 = 100
        nombre2 = 0
        nombreM2 = 0
        # (
        for a in proba2:
            nombre2 += 1
            total2 -= proba2[a]
            teste = 0
            for b in x2:
                if a == b[0]:
                    teste = 1
                    nombreM2 += 1
                    VnombreM2[b[0]] += 1
        # )teste si val actuelle (a) modifie
        # (
        for i in VnombreM2:
            if VnombreM2[i] == 0:
                Nmodif2 += [i]
        # )si pas modif2ie ajout a Nmodif2
        infini2 = 0
        while total2 != 0 and total2 != infini2 and nombre2 - nombreM2 > 0:
            add2 = total2 / (nombre2 - nombreM2)
            if isfinite(add2):
                add2 = floor(add2)
                infini2 = total2 - add2 * (nombre2 - nombreM2)
            total2 = 100
            for a in Nmodif2:
                if proba2[a] + add2 > 0:
                    proba2[a] += add2
                else:
                    proba2[a] = 0
                    if proba2[a] == 0:
                        x2 += [a]
                        nombreM2 += 1
                        Nmodif2.remove(a)
            for a in proba2:
                total2 -= proba2[a]
        return proba2

    proba2 = {
        "Tbois": 0,
        "Tair": 50,
        "Tterre": 25,
        "Tfeuille": 25
    }
    modif2 = [["Tbois", 0, 0]]

    if couche2< 0:
        modif2 += [["Tterre", 0, 100]]
    elif block2.get("[-1, 0]", "") == "Tterre":
        print("oui1")
        if block2.get("[-1, 1]", "") == "Tfeuille" or block2.get("[1, 1]", "") == "Tfeuille":
            modif2 += [["Tbois", "Tbois", 25]]
            print("oui")
        if block2.get("[-1, 2]", "") == "Tfeuille" or block2.get("[1, 2]", "") == "Tfeuille":
            modif2 += [["Tbois", "Tbois", 25]]
            print("oui2")
    elif block2.get("[-1, 0]", "") == "Tbois":
        if block2.get("[-1, 2]", "") != "Tfeuille" and block2.get("[1, 2]", "") != "Tfeuille" and block2.get("[-1, 1]","") != "Tfeuille" and block2.get("[1, 1]","") != "Tfeuille":
            modif2 += [["Tbois", 0, 100]]
        elif block2.get("[-1, 1]", "") == "" and block2.get("[1, 1]", "") == "":
            modif2 += [["Tbois", 0, 67]]
            modif2 += [["Tfeuille", 0, 33]]
        else:
            modif2 += [["Tfeuille", 0, 100]]
    elif block2.get("[-1, 1]", "") == "Tbois" and block2.get("[1, 1]", "") == "Tbois":
        modif2 += [["Tfeuille", 0, 100]]
    elif block2.get("[-1, 1]", "") != "Tfeuille" and block2.get("[1, 1]", "") != "Tfeuille":
        modif2 += [["Tfeuille", 0, 100]]
    for i in modif2:
        if i[1] == 0:
            tem2 = 0
        else:
            tem2 = proba2[i[1]]
        tem2 += i[2]
        proba2[i[0]] = tem2
    for a in proba2:
        if proba2[a] > 100:
            proba2[a] = 100
        elif proba2[a] < 0:
            proba2[a] = 0
    print(proba2)
    proba2 = calcul(modif2, proba2)
    somme2 = 0
    for a in proba2:
        somme2 += proba2[a]
    return [proba2, somme2]