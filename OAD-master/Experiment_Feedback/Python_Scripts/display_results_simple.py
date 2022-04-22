# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 11:26:27 2012

@author:Sebastian Rhode
"""
import numpy as np
import optparse
import os
env = os.environ
env.update({'QT_API':'pyside'})

import matplotlib.pyplot as plt

# configure parsing option for command line usage
parser = optparse.OptionParser()

parser.add_option('-f', '--file',
    action="store", dest="filename",
    help="query string", default="No filename passed")

parser.add_option('-b', '--block',
    action="store", dest="block",
    help="set to False for interactive behaviour", default="True")

# read command line arguments 
options, args = parser.parse_args()
savename = options.filename[:-4] + '.png'
print('Filename: ', options.filename)
print('Savename: ', savename)

block = True
if options.block == 'False':
	block = False

# load data
data = np.loadtxt(options.filename, delimiter='\t')
# create figure
figure = plt.figure(figsize=(10,5), dpi=100)
ax1 = figure.add_subplot(121)
ax2 = figure.add_subplot(122)

# create subplot 1
ax1.plot(data[:,0],data[:,1],'bo-', lw=2, label='Cell Count')
ax1.grid(True)
ax1.set_xlim([data[0,0]-1,data[-1,0]+1])
ax1.set_xlabel('Frame Number')
ax1.set_ylabel('Cells detected')

# create subplot 2
ax2.bar(data[:,0],data[:,1],width=0.7, bottom=0)
ax2.grid(True)
ax2.set_xlim([data[0,0]-1,data[-1,0]+1])
ax2.set_xlabel('Frame Number')

# adjust subplots
figure.subplots_adjust(left=0.10, bottom=0.12, right=0.95, top=0.95,wspace=0.20, hspace=0.20)
# save figure
plt.savefig(savename)
# show graph
plt.show(block=block)
