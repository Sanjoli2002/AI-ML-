import numpy as np
from scipy import stats
speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

avg_mean = np.mean(speed)
avg_median= np.median(speed)
avg_mode = stats.mode(speed)
avg_percentile= np.percentile(speed, 75)
Q1 = np.median(speed[:10])
Q3 = np.median(speed[10:])
avg_iquantile= Q3 - Q1

print("spped data:", speed)
print("mean:",avg_mean)
print("median:",avg_median)
print(avg_mode)
print("percentile:",avg_percentile)
print("quartile:", Q1)
print("interquartile:",avg_iquantile)