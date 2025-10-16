from trouve import *
from transforme import *


def opstart(block1, couche1, direction1):
    compres1 = trensfo(block1, couche1, direction1)
    blockF1 = compres1[0]
    couche1 = compres1[1]
    for i in [1, 2, 3]:
        if blockF1.get("[0, 0]", "Non") == "Non":
            compres1 = trouvedepart(blockF1, couche1)
            somme1 = compres1[1]
            proba1 = compres1[0]
            TheBF1 = final(proba1, somme1)
            blockF1["[0, 0]"] = [TheBF1, 1]

        compres1 = detrensfo(blockF1, direction1, i, couche1)
        blockF1 = compres1[0]
        couche1 = compres1[1]
    blockM1 = detrensfofinal(blockF1, direction1)
    print(blockM1)
    blockMF1 = []
    for i in blockM1:
        if i[3] == 1:
            blockMF1 += [("B" + (i[2][1:]) + ("({},".format(i[0])) + ("{})".format(i[1])))]
    return blockMF1