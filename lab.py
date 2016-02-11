import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# for curve fitting
def gauss(x, *p):
    A, mu, sigma = p
    return A*np.exp(-(x-mu)**2/(2.*sigma**2))

anglecounterror = [
(15, 20, 3),
(20, 27, 5),
(25, 27, 5),
(30, 17, 3),
(35, 15, 3),
(40, 33, 3),
(45, 160, 20),
(50, 8, 3),
(55, 10, 3),
(60, 5, 3),
(65, 6, 3),
(70, 5, 3),
(75, 6, 3),
(80, 5, 3),
(85, 5, 3),
(90, 6, 3),
(95, 6, 3),
(100, 50, 10),
(105, 5, 3),

(40, 40, 2),
(40.5, 57, 7),
(41, 53, 7),
(41.5, 32, 10),
(42, 16, 7),
(43, 15, 3),
(44, 30, 5),
(44.5, 86, 5),
(45, 190, 10),
(45.5, 175, 30),
(46, 77, 15),
(47, 14, 3),

(95, 6, 5),
(97, 7, 5),
(98, 7, 3),
(99, 8, 3),
(99.5, 30, 3),
(100, 30, 3),
(100.5, 45, 5),
(101, 27, 7),
(102, 10, 5),

(91.5, 7, 3),
(92, 7, 3),
(92.5, 5, 3),
(93, 7, 3),

(87.5, 12, 3),
(87, 7, 3),
(88, 11, 5),
(88.5, 7, 3),
]

angle, count, error = [np.array(_) for _ in zip(*anglecounterror)]

sortindxs = np.argsort(angle)
angle, count, error = angle[sortindxs], count[sortindxs], error[sortindxs]

kamin, kamax = np.argwhere(angle>43)[0], np.argwhere(angle<55)[-1]
kaangle, kacount = angle[kamin:kamax], count[kamin:kamax]
p0 = [200., 43, 3]
coeff, var_matrix = curve_fit(gauss, kaangle, kacount, p0=p0)
fitx = np.linspace(43, 48, 100)

plt.errorbar(angle, count, xerr=0.25, yerr=error)
plt.plot(fitx, gauss(fitx, *coeff), 'r')
#plt.plot(angle[kamin:kamax], count[kamin:kamax], 'r')

plt.show()
