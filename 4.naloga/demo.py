from turtle import color
import numpy as np
from scipy.io.wavfile import write
from matplotlib import pyplot as plt

# Ustvarjanje zvoka
T = 2  # sekunde, trajanje zvoka
fs = 44100  # frekvenca vzorcenja
N = T * fs  # stevilo vzorcev

# casovna os
t = np.arange(0, N, 1)

# frekvence
f_C1 = 261.63
f_E1 = 329.63
f_G1 = 392

# amplitude
A_C1 = 1.0
A_E1 = 1.0
A_G1 = 1.0

pit = 2 * np.pi * t

x = A_C1 * np.sin(f_C1 * pit) + A_E1 * np.sin(f_E1 * pit) + A_G1 * np.sin(f_G1 * pit)

# normalizacija na interval [-1, 1]
x = x / max(abs(x))

write("c_dur.wav", fs, x.astype(np.float32))

################ razpoznavanje akordov #######################
# pomagali si bomo s diskretno fourierijevo transformacijo (fft)

f = np.arange(0, N) * (fs / N)  # frekvencna os

# dft
X = np.fft.fft(x)

# mocnostni spekter
P = np.square(np.abs(X)) / N

# matplotlib NI INSTALIRAN ZA PREVERJANJE (pazi)
# narisemo mocnostni spekter
figure, axis = plt.subplots(2, 1)
axis[0].plot(t, x, color="blue")
axis[0].set_title("Jakost v odvisnosti od casa")
axis[0].set_xlabel("t [s]")

axis[1].plot(f, P, color="red")
axis[1].set_title("Moc v odvisnosti od frekvence")
axis[1].set_xlabel("f [Hz]")

plt.show()

# 1 oktava visje samo pomnozis z 2
# ce tona ni v tabeli, ga ignoriramo
# tudi ce manjka samo 1 ton ali vsebujejo prevec tonov, vrnemo prazen niz
