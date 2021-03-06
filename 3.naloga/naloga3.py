import numpy as np
from math import log2


def calc_crc(vhod: list) -> str:
    poly = 217
    reg = 255
    p_8 = 0

    for bit in vhod:
        p_8 = (reg & 1) ^ bit
        if p_8 == 0:
            reg = reg >> 1
        else:
            reg = ((reg >> 1) ^ poly) | 128

    tmp = "{0:08b}".format(reg)[::-1]
    f = hex(int(tmp[:4], 2))[-1:]
    crc = [f]
    if f.islower():
        crc[0] = f.upper()
    s = hex(int(tmp[4:], 2))[-1:]
    crc.append(s)
    if s.islower():
        crc[1] = s.upper()

    # print("".join(crc))
    return "".join(crc)


# def calc_crc(vhod: list) -> str:
#     poly = np.packbits([1, 1, 0, 1, 1, 0, 0, 1])
#     reg = np.packbits([1, 1, 1, 1, 1, 1, 1, 1])
#     p_8 = np.packbits([0, 0, 0, 0, 0, 0, 0, 0])

#     enka = np.packbits([0, 0, 0, 0, 0, 0, 0, 1])
#     l = np.packbits([1, 0, 0, 0, 0, 0, 0, 0])
#     for bit in vhod:
#         p_8 = np.bitwise_xor(np.bitwise_and(reg, enka), bit)
#         if np.all(p_8 == 0):
#             reg = np.right_shift(reg, enka)
#         else:
#             reg = np.bitwise_or(
#                 np.bitwise_xor(np.right_shift(reg, enka), poly),
#                 l,
#             )
#     tmp = np.unpackbits(reg)[::-1]
#     tmp = np.array2string(tmp, separator="")[1:-1]
#     # print(tmp)
#     f = hex(int(tmp[:4], 2))[-1:]
#     crc = [f]
#     if f.islower():
#         crc[0] = f.upper()
#     s = hex(int(tmp[4:], 2))[-1:]
#     crc.append(s)
#     if s.islower():
#         crc[1] = s.upper()

#     # print("".join(crc))
#     return "".join(crc)


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

    m_identity_matrix = np.eye(m, dtype=np.uint8)

    H_transponse = np.vstack((non_powers_of_two, m_identity_matrix))
    syndrome = (y @ (H_transponse)) % 2

    # spremenimo v stevilo
    H_transponse = np.packbits(H_transponse, axis=-1, bitorder="little")
    syndrome = np.packbits(syndrome, axis=-1, bitorder="little")

    izhod = np.array([], dtype=np.uint8)
    for i, col_s in enumerate(syndrome):
        # preverimo, ce je sindrom razlicen od 0
        if col_s != 0:
            # pogledamo katera vrstica je povrsti
            for j, col_h in enumerate(H_transponse):
                if col_s == col_h:
                    y[i][j] = 0 if y[i][j] == 1 else 1
                    break
        izhod = np.append(izhod, y[i][:-m])

    # print(izhod)
    crc = calc_crc(vhod)
    return (izhod.tolist(), crc)
