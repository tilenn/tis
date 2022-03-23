def zakodiraj(vhod: list) -> tuple[list, float]:
    izhod = []

    # zgradimo osnovni slovar, ki vsebuje vse 8-bitne vrednosti
    slovar = dict((chr(i), i) for i in range(2**8))
    idx_next_vnos = 256

    curr_niz = ""
    for znak in vhod:
        if curr_niz + znak in slovar:
            curr_niz += znak
        else:
            izhod.append(slovar[curr_niz])
            if idx_next_vnos < 4096:
                slovar[curr_niz + znak] = idx_next_vnos
                idx_next_vnos += 1
            curr_niz = znak
    izhod.append(slovar[curr_niz])

    return izhod, (12 * len(izhod)) / (8 * len(vhod))


def dekodiraj(vhod: list) -> tuple[list, float]:
    izhod = []

    # zgradimo osnovni slovar, ki vsebuje vse 8-bitne vrednosti
    slovar = dict((i, chr(i)) for i in range(2**8))
    idx_next_vnos = 256

    curr_niz = slovar[vhod[0]]
    izhod.append(curr_niz)

    for znak in vhod[1:]:
        n = slovar.get(znak, curr_niz + curr_niz[0])
        for letter in n:
            izhod.append(letter)
        if idx_next_vnos < 4096:
            slovar[idx_next_vnos] = curr_niz + n[0]
            idx_next_vnos += 1
        curr_niz = n

    return izhod, (12 * len(vhod)) / (8 * len(izhod))


def naloga2(vhod: list, nacin: int) -> tuple[list, float]:
    """
    Izvedemo kodiranje ali dekodiranje z algoritmom LZW.
    Zacetni slovar vsebuje vse 8-bitne vrednosti (0-255).
    Najvecja dolzina slovarja je 4096.

    Parameters
    ----------
    vhod : list
        Seznam vhodnih znakov: bodisi znaki abecede
        (ko kodiramo) bodisi kodne zamenjave
        (ko dekodiramo).
    nacin : int
        Stevilo, ki doloca nacin delovanja:
            0: kodiramo ali
            1: dekodiramo.

    Returns
    -------
    (izhod, R) : tuple[list, float]
        izhod : list
            Ce je nacin = 0: "izhod" je kodiran "vhod"
            Ce je nacin = 1: "izhod" je dekodiran "vhod"
        R : float
            Kompresijsko razmerje
    """
    if nacin == 0:
        return zakodiraj(vhod)
    return dekodiraj(vhod)

    # izhod = []
    # R = float('nan')
    # return (izhod, R)
