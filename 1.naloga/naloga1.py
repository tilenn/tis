def naloga1(besedilo, p):
    """ Izracun povprecne nedolocenosti na znak 

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

    H = None
    return H
