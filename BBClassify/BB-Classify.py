import scipy.special
from scipy.integrate import quad
from scipy.stats import binom, beta
import statistics as stats
import math
import pandas as pd
import numpy as np
import csv


## Turn a string with numbers delimited by commas (,) into numbers.
# s = a string of numbers separated by commas (,).
# notlist: Store as single value if list is length 1.
def string_to_number(s: str, notlist: bool = True):
    out = [int(x) if x.isdigit() else float(x) for x in s.replace(', ', ',').split(',')]
    if any(isinstance(x, float) for x in out):
        out = list(map(float, out))
    if len(out) == 1 and notlist == True:
        out = out[0]
    return out

## Load a .csv file and turn it into a list of lists.
# x = A string specifying the path to the .csv file.
# sumscores = Whether to create a single list withe ach entry being the sum of each sub-list.
def csv_to_list(x: str, sumscores: bool = True) -> list:
    data = []
    with open(x, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            row = list(map(float, row))
            data.append(row)
    if sumscores:
        for i in range(len(data)):
            data[i] = sum(data[i])
    return data

## The Cronbach's Alpha reliability coefficient.
# x = a list of lists, where rows are items and columns respondents.
def cronbachs_alpha(x: list) -> float:
    x = np.transpose(np.array(x))
    x = np.cov(x)
    n = x.shape[1]
    diag = sum(np.diag(x))
    var = sum(sum(x))
    alpha = (n / (n - 1)) * (1 - (diag / var))
    return alpha

## Livingston and Lewis' effective test length.
# mean = the mean of the observed-score distribution.
# var = the variance of the observed-score distribution.
# reliability = the reliability of the scores.
# min = the minimum possible value.
# max = the maximum possible value.
def etl(mean: float, var: float, reliability: float, min: float = 0, max: float = 1) -> float:
    return ((mean - min) * (max - mean) - (reliability * var)) / (var * (1 - reliability))

## Lord's k.
# mean = the mean of the observed-score distribution.
# var = the variance of the observed-score distribution.
# reliability = the reliability of the scores.
# length = the test-length.
def k(mean: float, var: float, reliability: float, length: int) -> float:
    vare = var * (1 - reliability)
    num = length * ((length - 1) * (var - vare) - length * var + mean * (length - mean))
    den = 2 * (mean * (length - mean) - (var - vare))
    return num / den

## Density function for the four-parameter beta distribution.
# x = specific point along the four-parameter beta distribution.
# a = alpha shape parameter.
# b = beta shape paramter.
# l = lower-bound location parameter.
# u = upper-bound location parameter.
def dbeta4p(x: float, a: float, b: float, l: float, u: float) -> float:
    if x < l or x > u:
        return 0
    else:
        return (1 / scipy.special.beta(a, b)) * (((x - l)**(a - 1) * (u - x)**(b - 1)) / (u - l)**(a + b - 1))

def rbeta4p(n: float, a: float, b: float, l: float = 0, u: float = 1) -> float:
    return np.random.beta(a, b, n) * (u - l) + l

## Function for fitting a four-parameter beta distribution to a vector of values-
# x = vector of values.
# moments = an optional list of the first four raw moments
def beta4fit(x: list, moments: list = []) -> list[float]:
    if len(moments) == 1:
        m1 = stats.mean(x)
        s2 = stats.variance(x)
        x3 = list(x)
        x4 = list(x)
        for i in range(len(x)):
            x3[i] = ((x3[i] - m1)**3) / (s2**0.5)**3
            x4[i] = ((x4[i] - m1)**4) / (s2**0.5)**4
        g3 = (1 / len(x3)) * sum(x3)
        g4 = (1 / len(x4)) * sum(x4)
    else:
        m1 = moments[0]
        s2 = moments[1] - moments[0]**2
        g3 = (moments[2] - 3 * moments[0] * moments[1] + 2 * moments[0]**3) / ((s2**0.5)**3)
        g4 = (moments[3] - 4 * moments[0] * moments[2] + 6 * moments[0]**2 * moments[0] - 3 * moments[0]**3) / ((s2**0.5)**4)
    r = 6 * (g4 - g3**2 - 1) / (6 + 3 * g3**2 - 2 * g4)
    if g3 < 0:
        a = r / 2 * (1 + (1 - ((24 * (r + 1)) / ((r + 2) * (r + 3) * g4 - 3 * (r - 6) * (r + 1))))**0.5)
        b = r / 2 * (1 - (1 - ((24 * (r + 1)) / ((r + 2) * (r + 3) * g4 - 3 * (r - 6) * (r + 1))))**0.5)
    else:
        b = r / 2 * (1 + (1 - ((24 * (r + 1)) / ((r + 2) * (r + 3) * g4 - 3 * (r - 6) * (r + 1))))**0.5)
        a = r / 2 * (1 - (1 - ((24 * (r + 1)) / ((r + 2) * (r + 3) * g4 - 3 * (r - 6) * (r + 1))))**0.5)
    l = m1 - ((a * (s2 * (a + b + 1))**0.5) / (a * b)**0.5)
    u = m1 + ((b * (s2 * (a + b + 1))**0.5) / (a * b)**0.5)
    return [a, b, l, u]

## Function for fitting a two-parameter beta distribution to a vector of values.
# x = vector of values.
# l = lower-bound location parameter.
# u = upper-bound location parameter.
def beta2fit(x: list, l: float, u: float, moments: list = []) -> list[float]:
    if len(list) == 1:
        m1 = stats.mean(x)
        s2 = stats.variance(x)
    else:
        m1 = moments[0]
        s2 = moments[1] - moments[0]**2
    a = ((l - m1) * (l * (m1 - u) - m1**2 + m1 * u - s2)) / (s2 * (l - u))
    b = ((m1 - u) * (l * (u - m1) + m1**2 - m1 * u + s2)) / (s2 * (u - l))
    return [a, b, l, u]

## Density function for Lord's two-term approximation of the compound binomial distribution.
# p = probability of success.
# N = total number of trials.
# n = specific number of successes.
# k = Lord's k.
def dcbinom(p: float, N: int, n: int, k: float) -> float:
    a = binom.pmf(n, N, p)
    b = binom.pmf(n, N - 2, p)
    c = binom.pmf(n - 1, N - 2, p)
    d = binom.pmf(n - 2, N - 2, p)
    e = k * p * (1 - p)
    return a - e * (b - 2*c + d)

## Integrate across univariate BB distribution.
# a = alpha shape parameter.
# b = beta shape parameter.
# l = lower-bound location parameter.
# u = upper-bound location parameter.
# N = upper-bound of binomial distribution.
# n = specific binomial outcome.
# k = Lord's k.
# lower = lower-bound of integration.
# upper = upper bound of intergration.
# method = specify Livingston and Lewis ("LL") or Hanson and Brennan approach.
def bbintegrate1(a: float, b: float, l: float, u: float, N: int, n: int, k: float, lower: float, upper: float, method: str = "ll", limit = 100) -> float:
    if method != "ll":
        def f(x, a, b, l, u, N, n, k):
            return dbeta4p(x, a, b, l, u) * dcbinom(x, N, n, k)
        return quad(f, lower, upper, args = (a, b, l, u, N, n, k), limit = limit)
    else:
        def f(x, a, b, l, u, N, n):
            return dbeta4p(x, a, b, l, u) * binom.pmf(n, N, x)
        return quad(f, lower, upper, args = (a, b, l, u, N, n), limit = limit)

## Integrate across bivariate BB distribution.
# a = alpha shape parameter.
# b = beta shape parameter.
# l = lower-bound location parameter.
# u = upper-bound location parameter.
# N = upper-bound of binomial distribution.
# n1 = specific binomial outcome on first binomial trial.
# n2 = specific binomial outcome on second binomial trial.
# lower = lower-bound of integration.
# upper = upper bound of intergration.
# method = specify Livingston and Lewis ("LL") or Hanson and Brennan approach.
def bbintegrate2(a: float, b: float, l: float, u: float, N: int, n1: int, n2: int, k: float, lower: float, upper: float, method: str = "ll", limit = 100) -> float:
    if method != "ll":
        def f(x, a, b, l, u, N, n1, n2, k):
            return dbeta4p(x, a, b, l, u) * dcbinom(x, N, n1, k) * dcbinom(x, N, n2, k)
        return quad(f, lower, upper, args = (a, b, l, u, N, n1, n2, k), limit = limit)
    else:
        def f(x, a, b, l, u, N, n1, n2):
            return dbeta4p(x, a, b, l, u) * binom.pmf(n1, N, x) * binom.pmf(n2, N, x)
        return quad(f, lower, upper, args = (a, b, l, u, N, n1, n2), limit = limit)

## Function for calculating the descending factorial each value of a vector.
# x = vector of values.
# r = the power x is to be raised to.
def dfac(x: list, r = int):
    x1 = list(x)
    for i in range(len(x)):
        if r <= 1:
            x1[i] = x1[i]**r
        else:
            for j in range(1, r + 1):
                if j > 1:
                    x1[i] = x1[i] * (x[i] - j + 1)
    return x1

## Function for calculating the first four raw moments of the true-score distribution.
# x = vector of values.
# n = the effective or actual test length.
# k = Lord's k.
def tsm(x: list, n: int, k: float):
    m = [0, 0, 0, 0]
    for i in range(0, 4):
        if i == 0:
            m[i] = stats.mean(x) / n
        else:
            M = i + 1
            a = (dfac([n], 2)[0] + k * dfac([M], 2)[0])
            b = stats.mean(dfac(x, M)) / dfac([n - 2], M - 2)[0]
            c = k * dfac([M], 2)[0] * m[i]
            m[i] = (b / a) + c
    return m

## Estimate the true-score 2 or 4 parameter beta distribution parameters.
# x = vector of values
# n = actual or effective test length.
# k = Lord's k.
# model = whether 2 or 4 parameters are to be fit.
# l = if model = 2, specified lower-bound of 2-parameter distribution.
# u = if model = 2, specified upper-bound of 2-parameter distribution.
def betaparameters(x: list, n: int, k: float, model: int = 4, l: float = 0, u: float = 1):
    m = tsm(x, n, k)
    s2 = m[1] - m[0]**2
    g3 = (m[2] - 3 * m[0] * m[1] + 2 * m[0]**3) / (math.sqrt(s2)**3)
    g4 = (m[3] - 4 * m[0] * m[2] + 6 * m[0]**2 * m[1] - 3 * m[0]**4) / (math.sqrt(s2)**4)
    if model == 4:
        r = 6 * (g4 - g3**2 - 1) / (6 + 3 * g3**2 - 2 * g4)
        if g3 < 0:
            a = r / 2 * (1 + (1 - ((24 * (r + 1)) / ((r + 2) * (r + 3) * g4 - 3 * (r - 6) * (r + 1))))**0.5)
            b = r / 2 * (1 - (1 - ((24 * (r + 1)) / ((r + 2) * (r + 3) * g4 - 3 * (r - 6) * (r + 1))))**0.5)
        else:
            b = r / 2 * (1 + (1 - ((24 * (r + 1)) / ((r + 2) * (r + 3) * g4 - 3 * (r - 6) * (r + 1))))**0.5)
            a = r / 2 * (1 - (1 - ((24 * (r + 1)) / ((r + 2) * (r + 3) * g4 - 3 * (r - 6) * (r + 1))))**0.5)
        l = m[0] - ((a * (s2 * (a + b + 1))**0.5) / (a * b)**0.5)
        u = m[0] + ((b * (s2 * (a + b + 1))**0.5) / (a * b)**0.5)
    if model == 2:
        a = ((l - m[0]) * (l * (m[0] - u) - m[0]**2 + m[0] * u - s2)) / (s2 * (l - u))
        b = ((m[0] - u) * (l * (u - m[0]) + m[0]**2 - m[0] * u + s2)) / (s2 * (u - l))
    return {"alpha":  a, "beta": b, "l": l, "u": u}

## Function for estimating accuracy and consistency from beta-binomial models.
# x = vector of values representing test-scores, or a list of model parameters.
# reliability = the reliability coefficient of the test-scores.
# min = the minimum possible score to attain on the test (only necessary for 
#       the Livingston and Lewis approach).
# max = for the Livingston and Lewis approach, the maximum possible score to 
#       attain on the test. For the Hanson and Brennan approach, the actual
#       test length (number of items).
# model = how many parameters of the true-score distribution that is to be
#       estimated (4 or 2). Default is 4.
# l = the lower-bound location parameter for the two-parameter distribution.
# u = the lower-bound location parameter for the two-parameter distribution.
# failsafe = whether the function should automatically revert to a two-
#       parameter solution if the four-parameter fitting procedure produces
#       impermissible location-parameter estimates.
# method = string specifying whether it is the Livingston and Lewis or the 
#       Hanson and Brennan approach is to be employed. Default is "ll" 
#       (Livingston and Lewis). Any other value passed means the Hanson and 
#       Brennan approach.
# output = list of strings which state what analyses to do and include in the 
#       output.
# print_output = Whether to print the output to the consoel as it is estimated.
def cac(x, reliability: float, min: float, max: float, cut: float, model: int = 4, l: float = 0, u: float = 1, failsafe: bool = False, method: str = "ll", output: list[str] = ["parameters", "accuracy", "consistency"], print_output = True):
    out = {}
    cut = [min] + cut + [max]
    tcut = list(cut)
    for i in range(len(cut)):
        tcut[i] = (tcut[i] - min) / (max - min)
    if isinstance(x, dict):
        pars = x
        if method == "ll":
            N = pars["etl"]
        else:
            N = pars["atl"]
    else:
        if method == "ll":
            Nnotrounded = etl(stats.mean(x), stats.variance(x), reliability, min, max)
            N = round(Nnotrounded)
            pars = betaparameters(x, N, 0, model, l, u)
            if (failsafe == True and model == 4) and (l < 0 or u > 1):
                pars = betaparameters(x, N, 0, 2, l, u)
            pars["etl"] = Nnotrounded
            pars["etl rounded"] = N
            pars["lords_k"] = 0
            for i in range(len(cut)):
                cut[i] = tcut[i] * N
                cut[i] = round(cut[i])
        else:
            N = max 
            K = k(stats.mean(x), stats.variance(x), reliability, N)
            pars = betaparameters(x, N, K, model, l, u)
            if (failsafe == True and model == 4) and (l < 0 or u > 1):
                pars = betaparameters(x, max, N, 2, l, u)
            pars["lords_k"] = K
    if "parameters" in output:
        out["parameters"] = pars
        if print_output:
            print("Model parameter estimates:")
            print(out["parameters"])
            print("")

    if "accuracy" in output:
        print("Estimating accuracy...\n")
        confmat = np.zeros((N + 1, len(cut) - 1))
        for i in range(len(cut) - 1):
            for j in range(N + 1):
                confmat[j, i] = bbintegrate1(pars["alpha"], pars["beta"], pars["l"], pars["u"], N, j, pars["lords_k"], tcut[i], tcut[i + 1], method)[0]
        confusionmatrix = np.zeros((len(cut) - 1, len(cut) - 1))
        for i in range(len(cut) - 1):
            for j in range(len(cut) - 1):
                if i != len(cut) - 2:
                    confusionmatrix[i, j] = sum(confmat[cut[i]:cut[i + 1], j])
                else:
                    confusionmatrix[i, j] = sum(confmat[cut[i]:, j])
        accuracy = []
        for i in range(len(cut) - 1):
            accuracy = accuracy + [confusionmatrix[i, i]]
        accuracy = sum(accuracy)
        out["Confusion matrix"] = pd.DataFrame(confusionmatrix)
        out["Overall accuracy"] = accuracy
        if print_output:
            print("Confusion matrix:")
            print(out["Confusion matrix"])
            print("")
            print("Overall accuracy:")
            print(out["Overall accuracy"])
            print("")
    
    if "consistency" in output:
        print("Estimating consistency...\n")
        consmat = np.zeros((N + 1, N + 1))
        for i in range(N + 1):
            for j in range(N + 1):
                if i <= j:
                    consmat[i, j] = bbintegrate2(pars["alpha"], pars["beta"], pars["l"], pars["u"], N, i, j, pars["lords_k"], 0, 1, method)[0]
        lower_triangle = np.tril_indices(consmat.shape[0], 0)
        consmat[lower_triangle] = consmat.T[lower_triangle]
        consistencymatrix = np.zeros((len(cut) - 1, len(cut) - 1))
        for i in range(len(cut) - 1):
            for j in range(len(cut) - 1):
                if i == 0 and j == 0:
                    consistencymatrix[i, j] = sum(sum(consmat[0:cut[i + 1], 0:cut[j + 1]]))
                if i == 0 and (j != 0 and j != len(cut) - 2):
                    consistencymatrix[i, j] = sum(sum(consmat[0:cut[i + 1], cut[j]:cut[j + 1]]))
                if i == 0  and j == len(cut) - 2:
                    consistencymatrix[i, j] = sum(sum(consmat[0:cut[i + 1], cut[j]:cut[j + 1] + 1]))
                if (i != 0 and i != len(cut) - 2) and j == 0:
                    consistencymatrix[i, j] = sum(sum(consmat[cut[i]:cut[i + 1], 0:cut[j + 1]]))
                if (i != 0 and i != len(cut) - 2) and (j != 0 and j != len(cut) - 2):
                    consistencymatrix[i, j] = sum(sum(consmat[cut[i]:cut[i + 1], cut[j]:cut[j + 1]]))
                if (i != 0 and i != len(cut) - 2) and j == len(cut) - 2:
                    consistencymatrix[i, j] = sum(sum(consmat[cut[i]:cut[i + 1], cut[j]:cut[j + 1] + 1]))
                if i == len(cut) - 2 and j == 0:
                    consistencymatrix[i, j] = sum(sum(consmat[cut[i]:cut[i + 1] + 1, 0:cut[j + 1]]))
                if i == len(cut) - 2 and (j != 0 and j != len(cut) - 2):
                    consistencymatrix[i, j] = sum(sum(consmat[cut[i]:cut[i + 1] + 1, cut[j]:cut[j + 1]]))
                if i == len(cut) - 2 and j == len(cut) - 2:
                        consistencymatrix[i, j] = sum(sum(consmat[cut[i]:cut[i + 1] + 1, cut[j]:cut[j + 1] + 1]))
            consistency = []
            for i in range(len(cut) - 1):
                consistency = consistency + [consistencymatrix[i, i]]
            consistency = sum(consistency)
        out["Consistency matrix"] = pd.DataFrame(consistencymatrix)
        out["Overall consistency"] = consistency
        if print_output:
            print("Consistency matrix:")
            print(out["Consistency matrix"])
            print("")
            print("Overall consistency:")
            print(out["Overall consistency"])
    return out

# Setting the seed
np.random.seed(123456)

# Define the parameters for the beta distribution
a, b = 6, 4
# The first two parameters are for the location and scale parameters respectively
p_success = rbeta4p(100000, 6, 4, .15, .85)

# Preallocate a matrix of zeros with 1000 rows and 20 columns
rawdata = np.zeros((100000, 100))

# Loop over the columns
for i in range(100000):
    for j in range(100):
    # For each column, generate binomially distributed data
        rawdata[i, j] = np.random.binomial(1, p_success[i], 1)
sumscores = np.sum(rawdata, axis = 1)
meanscores = np.mean(rawdata, axis = 1)

output = cac(sumscores, cronbachs_alpha(rawdata), 0, 100, [50, 75])