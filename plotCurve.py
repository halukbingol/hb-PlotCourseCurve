import statistics as stat
import numpy as np
import matplotlib.pyplot as plt
# import matplotlib as plt
import math
import csv


#
#
def readData():
    """
    Read data.

    :return: courseName, arrayOfFloats
    """
    array = []
    with open('dataCourse.txt', 'r') as file:
        reader = csv.reader(file)
        is_first_line = True
        course = 'no'
        for row in reader:
            if is_first_line:
                course = row[0]
                # TODO check if it is a number, i.e. course is mission
                is_first_line = False
            else:
                array.append(float(row[0]))
    return course, array




def average(lst):
    """
    Find the mean value of a list

    eg
        average([1., 2., 6.])   # => 3.

    If the list is empty, return 0.
    """
    if lst:
        return sum(lst) / len(lst)
    else:
        return 0.


def make_weighted_sum_fn(weights):
    """
    Given a list of weights, return a function which
      calculates a final weighted score
    """
    weights = list(weights)
    len_ = len(weights)

    def weighted_sum_fn(values):
        values = list(values)
        assert len(values) == len_
        return sum(w * v for w, v in zip(weights, values))

    return weighted_sum_fn


def getBin(data):
    dataMin = math.ceil(min(data))
    dataMax = math.floor(max(data))
    number = dataMax - dataMin + 1
    bin = np.linspace(dataMin,
                      dataMax,
                      number)
    return bin


# Generated data set
def GenerateDataset(N, min, max):
    """
    Testing.

    :param N:
    :param min:
    :param max:
    :return:
    """
    lst = []
    #
    return [1, 2, 3]
    #
    import random as rd
    for i in range(N):
        x = rd.randint(min, max)
        x = rd.rand
        lst.append(x)
    return lst


#
#
def plotCurve(course, data):
    plot_figure = plt.figure()

    # set the mean and the variance:
    mu = np.mean(data)
    sigma = np.std(data, ddof=1)

    # @HB should not be manual
    # print(np.siz)
    data_count = 114
    # TODO check `data_count`
    data_min = math.floor(min(data)) - 1
    data_max = math.ceil(max(data)) + 1
    bin_nof = data_max - data_min + 1
    # bins = np.linspace(data_min,
    #                    dataMax,
    #                    bin_nof)
    bin_size = 101
    bins = np.linspace(0,
                       100,
                       bin_size)
    #
    print('min:', data_min, 'max:', data_max, 'bin_nof:', bin_nof)

    # sigma and mu
    #
    mu = stat.mean(grades)
    sigma = stat.stdev(grades)
    sig2m = math.floor(mu - 2 * sigma)
    sig1m = math.floor(mu - 1 * sigma)
    sig0m = math.floor(mu)
    sig1p = math.floor(mu + 1 * sigma)
    sig2p = math.floor(mu + 2 * sigma)
    #
    # sig_x = -5
    # sig_y = -1
    sig_x = 0
    sig_y = -1
    alpha = 0.5

    #
    # plt.text(sig2m + sig_x, sig_y, '$\mu-2\sigma=$' + "%2.1f" % (mu - 2 * sigma), color='r', alpha=alpha, size=6)
    # plt.text(sig1m + sig_x, sig_y, '$\mu-\sigma=$' + "%2.1f" % (mu - 1 * sigma), color='r', alpha=alpha, size=6)
    # plt.text(sig0m + sig_x, sig_y, '$\mu=$' + "%2.1f" % (mu - 0 * sigma), color='r', alpha=alpha, size=6)
    # plt.text(sig1p + sig_x, sig_y, '$\mu+\sigma=$' + "%2.1f" % (mu + 1 * sigma), color='r', alpha=alpha, size=6)
    # plt.text(sig2p + sig_x, sig_y, '$\mu+2\sigma=$' + "%2.1f" % (mu + 2 * sigma), color='r', alpha=alpha, size=6)
    plt.text(sig2m + sig_x, sig_y, '$\mu-2\sigma=$' + "%2.1f" % (mu - 2 * sigma), color='r', alpha=alpha, size=6, rotation=-90,verticalalignment='top')
    plt.text(sig1m + sig_x, sig_y, '$\mu-\sigma=$' + "%2.1f" % (mu - 1 * sigma), color='r', alpha=alpha, size=6, rotation=-90,verticalalignment='top')
    plt.text(sig0m + sig_x, sig_y, '$\mu=$' + "%2.1f" % (mu - 0 * sigma), color='r', alpha=alpha, size=6, rotation=-90,verticalalignment='top')
    plt.text(sig1p + sig_x, sig_y, '$\mu+\sigma=$' + "%2.1f" % (mu + 1 * sigma), color='r', alpha=alpha, size=6, rotation=-90,verticalalignment='top')
    plt.text(sig2p + sig_x, sig_y, '$\mu+2\sigma=$' + "%2.1f" % (mu + 2 * sigma), color='r', alpha=alpha, size=6, rotation=-90,verticalalignment='top')
    #
    plt.axvline(x=sig2m, color='r', alpha=alpha)
    plt.axvline(x=sig1m, color='r', alpha=alpha)
    plt.axvline(x=sig0m, color='r', alpha=alpha)
    plt.axvline(x=sig1p, color='r', alpha=alpha)
    plt.axvline(x=sig2p, color='r', alpha=alpha)
    # plot bell curve
    plt.plot(bins, data_count * 1 / (sigma * np.sqrt(2 * np.pi)) *
             np.exp(- (bins - mu) ** 2 / (2 * sigma ** 2)),
             linewidth=2, color='r', alpha=alpha)

    # data
    plt.hist(data, bins=bins, histtype='bar', rwidth=0.8, alpha=0.8)

    # plot
    plt.title('Curve of ' + course)
    plt.xlabel('overall grades')
    plt.ylabel('number of students')
    plt.xlim([0, bin_size + 1])
    # timestamp
    # plt.rcParams.update({'font.size': 6})
    plt.text(100, 8, "created at:" + get_time_stamp(), color='b', alpha=alpha, rotation='vertical', size=6)
    # plt.text(90, 7, "created at:" + get_time_stamp(), color='b', alpha=alpha, rotation='vertical', size=6)
    #
    plt.show()

    # f.savefig("/Users/bingol/Downloads/cmpe220-XXXX-3-curve.pdf", bbox_inches='tight')
    plot_figure.savefig("/Users/bingol/Downloads/" + course + "-curve.pdf", bbox_inches='tight')
    # ---- plotCurve


from datetime import datetime


def get_time_stamp():
    now = datetime.now()
    # print("now =", now)
    return now.strftime("%Y-%m-%dT%H:%M")


# ========================


# grades = np.array(
#     [
#         73.11,
#         82.99,
#         80.36,
#         75.16,
#         97.56
#     ])
(course, data) = readData()
print(course)

grades = np.array(data)
bins = np.linspace(1,
                   100,
                   101)

# gradeNumber = GenerateDataset(5, 1, 10)
# bins = np.linspace(dataMin,
#                    dataMax,
#                    binNOF)
# print(grades)

mu = stat.mean(grades)
sigma = stat.stdev(grades)
median_low = stat.median_low(grades)
# mode = stat.mode(gradeNumber)
print('mu:\t\t', mu)
print('sigma:\t\t', sigma)
print('median_low:', median_low)
# print('mode:', mode)


plotCurve(course, grades)

print("file at: " +
      "/Users/bingol/Downloads/" + course + "-curve.pdf")
