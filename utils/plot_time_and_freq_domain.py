import numpy as np
import matplotlib.pyplot as plt
from utils import frequency_domain


def plot_time_and_freq_domain(sampling_rate, signal, signal_name):
    t = np.arange(len(signal)) / float(sampling_rate)

    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(t, signal)
    plt.xlabel('T')
    plt.ylabel(signal_name)

    frq, signal_f = frequency_domain(signal, sampling_rate)

    neg_arr = -1 * frq
    frq = np.append(neg_arr[::-1], frq)
    frq = frq[frq.shape[0] // 4:(3 * frq.shape[0]) // 4]
    signal_f = np.append(signal_f[::-1], signal_f)
    signal_f = signal_f[signal_f.shape[0] // 4:(3 * signal_f.shape[0]) // 4]

    plt.subplot(2, 1, 2)
    plt.plot(frq, signal_f, 'b')
    plt.xlabel('Freq (Hz)')
    plt.ylabel('|X(freq)|')
    plt.tight_layout()
    plt.show()
