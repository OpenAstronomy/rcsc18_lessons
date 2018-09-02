import numpy as np
import matplotlib.pyplot as plt


def analyse(filename):
    """
    Reads data from the specified file and plots the average, maximum and minimum along the first
    axis of the data.

    Parameters
    ----------
    filename : str
        Name or path to a file containing data to be plotted. Data should be 2-dimensional and
        values should be separated by commas.

    Examples
    --------
    >>> analyse('/path/to/mydata.csv')
    """

    data = np.loadtxt(fname=filename, delimiter=',')

    fig = plt.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(np.mean(data, axis=0))

    axes2.set_ylabel('max')
    axes2.plot(np.max(data, axis=0))

    axes3.set_ylabel('min')
    axes3.plot(np.min(data, axis=0))

    fig.tight_layout()
    plt.show()


def detect_problems(filename):
    """
    Tests data stored in the specified file for spurious or unexpected values.

    Parameters
    ----------
    filename : str
        Name or path to a file containing data to tested. Data should be 2-dimensional and values
        should be separated by commas.

    Examples
    --------
    >>> detect_problems('/path/to/mydata.csv')
    """
    data = np.loadtxt(fname=filename, delimiter=',')

    if np.max(data, axis=0)[0] == 0 and np.max(data, axis=0)[20] == 20:
        print('Suspicious looking maxima!')
    elif np.sum(np.min(data, axis=0)) == 0:
        print('Minima add up to zero!')
    else:
        print('Seems OK!')
