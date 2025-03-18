import math

def corr(x, y):
    mean_x = sum(x)/len(x)
    mean_y = sum(y)/len(y)
    std_dev_x = math.sqrt(sum((xi-mean_x)**2 for xi in x)/len(x))
    std_dev_y = math.sqrt(sum((yi-(mean_y))**2 for yi in y)/len(y))
    cov_x_y = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))/len(x)
    return cov_x_y/(std_dev_x*std_dev_y)
