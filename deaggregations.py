'''
    This script is used to bulk download data from USGS 2008 deaggint tool
    home = 'http://geohazards.usgs.gov/deaggint/2008/'
    Author: Charles Wang
    Clemson University
    Date:12-27-2015
'''

from multiprocessing.dummy import Pool as ThreadPool
from goodman import worker

# parse paras
parsFile = open('pars.txt', 'r')
food = []
for line in parsFile:
    food.append(line)

# get some workers
pool = ThreadPool()
# send job to workers, make sure to give them food.
# no food no work.
results = pool.map(worker, food)
# jobs are done, clean the site
pool.close()
pool.join()

