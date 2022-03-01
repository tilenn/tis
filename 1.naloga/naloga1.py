import collections
from math import log2


def naloga1(besedilo, p):
    """Izracun povprecne nedolocenosti na znak

    Parameters
    ----------
    besedilo : str
        Vhodni niz
    p : int
        Stevilo poznanih predhodnih znakov: 0, 1 ali 2.
        p = 0: H(X1)
            racunamo povprecno informacijo na znak abecede
            brez poznanih predhodnih znakov
        p = 1: H(X2|X1)
            racunamo povprecno informacijo na znak abecede
            pri enem poznanem predhodnemu znaku
        p = 2: H(X3|X1,X2)

    Returns
    -------
    H : float
        Povprecna informacija na znak abecede z upostevanjem
        stevila poznanih predhodnih znakov 'p'
    """

    # formatira besedilo v bolj prijazno obliko
    besedilo = "".join([crka for crka in besedilo if crka.isalpha()]).upper()
    # print(besedilo)

    counter_za_crke = collections.Counter(besedilo)
    # print(counter_za_crke)

    str_len = len(besedilo)
    H = 0

    for val in counter_za_crke.values():
        H -= (val / str_len) * log2(val / str_len)

    # print("H", H)
    if p == 0:
        return H

    dvojcki = collections.defaultdict(int)
    for i, j in zip(besedilo, besedilo[1:]):
        dvojcki[i + j] += 1

    st_vseh_dvojckov = sum(dvojcki.values())
    H2 = 0
    for val in dvojcki.values():
        H2 += (val / st_vseh_dvojckov) * log2(st_vseh_dvojckov / val)
    # print("H2", H2)

    if p == 1:
        return H2 - H

    trojcki = collections.defaultdict(int)
    for i, j, k in zip(besedilo, besedilo[1:], besedilo[2:]):
        trojcki[i + j + k] += 1

    st_vseh_trojckov = sum(trojcki.values())

    H3 = 0
    for val in trojcki.values():
        H3 += (val / st_vseh_trojckov) * log2(st_vseh_trojckov / val)
    # print("H3", H3)
    return H3 - H2

    # return H
