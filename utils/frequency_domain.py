import numpy as np
from scipy import fft, arange


def frequency_domain(signal, sampling_frequency):
    """
    Derive frequency spectrum of a signal from time domain
    :param signal: signal in the time domain
    :param  sampling_frequency: sampling frequency
    :returns frequencies and their content distribution
    """
    signal = signal - np.average(signal)  # zero-centering

    n = len(signal)
    k = np.arange(n)
    tarr = n / float(sampling_frequency)
    frqarr = k / float(tarr)  # two sides frequency range

    frqarr = frqarr[range(n // 2)]  # one side frequency range

    signal = fft(signal) / n  # fft computing and normalization
    signal = signal[range(n // 2)]

    return frqarr, abs(signal)

