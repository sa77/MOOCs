# Radiation Exposure
# variables provided by edX test engine: 
#   f(x) - function that gives radiation activity at a given 'x' year
# 
# Example: 
# radiationExposure(0, 5, 1)
# ----- Output -----
# 39.1031878433
#

def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def frange(start, stop, step):
    while start < stop:
        yield start
        start += step

def radiationExposure(start, stop, step):
    '''
    start - int, time at which exposure begins
    stop - int, time at which exposure ends
    step - float, width of each rect on the graph along x- axis

    returns - float, amount of radiatiom exposed between start and stop years
    '''
    total_area = 0
    for year in frange(start, stop, step):
        total_area += f(year) * step
    return total_area

#print radiationExposure(0, 5, 1)
#print radiationExposure(5, 11, 1)
#print radiationExposure(0, 11, 1)
#print radiationExposure(40, 100, 1.5)


