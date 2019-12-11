from scipy.io import wavfile
from utils import plot_time_and_freq_domain


def main():
    freq_sample, audio = wavfile.read('audio/test2.wav')
    plot_time_and_freq_domain(freq_sample, audio, "Message Signal")


if __name__ == '__main__':
    main()
