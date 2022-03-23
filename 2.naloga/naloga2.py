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
    print("dekodiraj")
    izhod = []

    # zgradimo osnovni slovar, ki vsebuje vse 8-bitne vrednosti
    slovar = dict((chr(i), i) for i in range(2**8))
    indeks_naslednejga_vnosa_v_slovar = 256

    return ["d", "e", "l", "a"], 3.14


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
    # return dekodiraj(vhod)

    # izhod = []
    # R = float('nan')
    # return (izhod, R)
