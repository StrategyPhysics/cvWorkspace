# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 11:26:27 2012

@author: m1srh
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
    help="query string", default="spam")

parser.add_option('-b', '--block',
    action="store", dest="block",
    help="set to False for non interactive behaviour", default="True")

# read command line arguments 
options, args = parser.parse_args()

savename = options.filename[:-4] + '.png'
print ('Filename: ', options.filename)
print ('Savename: ', savename)

block = True
if options.block == 'False':
	block = False

# load data
data = np.loadtxt(options.filename, delimiter='\t', skiprows=1)

# create figure
figure = plt.figure(figsize=(12,4), dpi=100)
ax1 = figure.add_subplot(131)
ax2 = figure.add_subplot(132)
ax3 = figure.add_subplot(133)

# create subplot 1
ax1.bar(data[:,0],data[:,1],width=0.7, bottom=0, color='blue')
ax1.grid(True)
ax1.set_xlabel('Tile Number')
ax1.set_ylabel('Cells detected')

# create subplot 2
ax2.bar(data[:,0],data[:,2],width=0.7, bottom=0, color='green')
ax2.grid(True)
ax2.set_xlabel('Tile Number')
ax2.set_ylabel('Cells in total')

# create subplot 3
ax3.plot(data[:,3],data[:,4],'ro', markersize = 5)
ax3.grid(True)
ax3.set_xlim([data[:,3].min()-100,data[:,3].max()+100])
ax3.set_ylim([data[:,4].min()-100,data[:,4].max()+100])
ax3.set_xlabel('X Stage Position')
ax3.set_ylabel('Y Stage Position')

# add frame number directly to every data point
for X, Y, Z in zip(data[:,3], data[:,4], data[:,0]):
    # Annotate the points
    #ax3.annotate('{}'.format(int(Z)), xy=(X,Y), xytext=(5, 10), ha='right', textcoords='offset points')
    ax3.annotate('{}'.format(int(Z)), xy=(X,Y), xytext=(0, 15), ha='right',
                 textcoords='offset points',arrowprops=dict(arrowstyle='->', shrinkA=0))

# configure plot
figure.subplots_adjust(left=0.07, bottom=0.12, right=0.95, top=0.95,wspace=0.30, hspace=0.20)
# save figure
plt.savefig(savename)
# show graph
plt.show(block=block)