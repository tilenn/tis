import numpy as np

# fs je stevilo vzorcev, ki jih vzamemo na sekundo
def is_contained(arr, val):
    for v in arr:
        if abs(v - val) < 5:
            return False
    return True


def naloga4(vhod: list, fs: int) -> str:
    """
    Poisce akord v zvocnem zapisu.

    Parameters
    ----------
    vhod : list
        vhodni zvocni zapis
    fs : int
        frekvenca vzorcenja

    Returns
    -------
    izhod : str
        ime akorda, ki se skriva v zvocnem zapisu;
        ce frekvence v zvocnem zapisu ne ustrezajo nobenemu od navedenih akordov,
        vrnemo prazen niz ''
    """

    toni = {
        261.63: "C1",
        523.25: "C2",
        277.18: "CIS1",
        554.37: "CIS2",
        293.66: "D1",
        587.33: "D2",
        311.13: "DIS1",
        622.25: "DIS2",
        329.63: "E1",
        659.25: "E2",
        349.23: "F1",
        698.46: "F2",
        369.99: "FIS1",
        739.99: "FIS2",
        392: "G1",
        783.99: "G2",
        415.30: "GIS1",
        830.61: "GIS2",
        440: "A1",
        880: "A2",
        466.16: "B1",
        932.33: "B2",
        493.88: "H1",
        987.77: "H2",
    }
    akordi = {
        "Cdur": ["C1", "E1", "G1"],
        "Cmol": ["C1", "DIS1", "G1"],
        "Ddur": ["D1", "FIS1", "A1"],
        "Dmol": ["D1", "F1", "A1"],
        "Edur": ["E1", "GIS1", "H1"],
        "Emol": ["E1", "G1", "H1"],
        "Fdur": ["F1", "A1", "C2"],
        "Fmol": ["F1", "GIS1", "C2"],
        "Gdur": ["G1", "H1", "D2"],
        "Gmol": ["G1", "B1", "D2"],
        "Adur": ["A1", "CIS2", "E2"],
        "Amol": ["A1", "C2", "E2"],
        "Hdur": ["H1", "DIS2", "FIS2"],
        "Hmol": ["H1", "D2", "FIS2"],
    }

    stevilo_vzorcev = len(vhod)

    X = np.fft.fft(vhod)

    P = np.square(np.abs(X)) / stevilo_vzorcev
    delta_f = fs / stevilo_vzorcev

    frekvence = []
    counter = 0
    for i in range(int(len(vhod) / 2)):
        index_max = np.where(P == np.max(P))
        frequency = index_max[0][0] * delta_f
        P = np.delete(P, index_max[0][0])
        if frequency < 1000 and counter < 3 and is_contained(frekvence, frequency):
            counter += 1
            # print(frekvence, frequency)
            frekvence.append(frequency)
            if counter == 3:
                break
            # print(frequency)

    izhod_tmp = []
    # za vsako frekvenco dobimo ton
    for f in frekvence:
        for key in toni:
            if np.abs(key - f) < 5:
                # izhod += toni[key]
                izhod_tmp.append(toni[key])
                break

    # print(izhod_tmp)
    if len(izhod_tmp) < 3:
        return ""

    izhod_tmp = set(izhod_tmp)
    for key, val in akordi.items():
        # print(key, val)
        if izhod_tmp <= set(val):
            return key

    return ""
