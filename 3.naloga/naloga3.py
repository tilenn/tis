import numpy as np
from math import log2


def naloga3(vhod: list, n: int) -> tuple[list, str]:
    """
    Izvedemo dekodiranje binarnega niza `vhod`, zakodiranega
    s Hammingovim kodom dolzine `n` in poslanega po zasumljenem kanalu.
    Nad `vhod` izracunamo vrednost `crc` po standardu CRC-8/CDMA2000.

    Parameters
    ----------
    vhod : list
        Sporocilo y, predstavljeno kot seznam bitov (stevil tipa int)
    n : int
        Stevilo bitov v kodni zamenjavi

    Returns
    -------
    (izhod, crc) : tuple[list, str]
        izhod : list
            Odkodirano sporocilo y (seznam bitov - stevil tipa int)
        crc : str
            Vrednost CRC, izracunana nad `vhod`. Niz dveh znakov.
    """

    # vhod
    y = np.array(vhod, dtype=np.uint8).reshape(len(vhod) // n, n)
    print("y (vhodno sporocilo): ", y, sep="\n")

    # stevilo varnostnih bitov
    m = int(log2(n + 1))

    # matrika H (oziroma H transponirano), dimenzije n x m
    # po vrsticah ima binarno zapisana stevila
    # v zadnjih vrsticah so potence stevila 2, tako da rata identiteta

    non_powers_of_two = np.unpackbits(
        np.array(
            [i for i in range(1, n + 1) if (i & (i - 1) != 0)],
            dtype=np.uint8,
        ),
        bitorder="little",
    ).reshape(n - m, 8)[:, :m]
    # print(tmp)

    m_identity_matrix = np.eye(m, dtype=np.uint8)
    # print(m_identity_matrix)

    H_transponse = np.vstack((non_powers_of_two, m_identity_matrix))
    # print(H_transponse)

    S = y.dot(H_transponse) % 2
    print(S)

    izhod = []
    crc = ""
    return (izhod, crc)
