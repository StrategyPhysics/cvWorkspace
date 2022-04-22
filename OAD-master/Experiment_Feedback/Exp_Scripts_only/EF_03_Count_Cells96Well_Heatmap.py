#################################################################
# File       : EF_03_Count_Cells96Well_Heatmap.py
# Version    : 1.0
# Author     : czmla
# Date       : 06.12.2018
# Institution : Carl Zeiss Microscopy GmbH
#
# Copyright (c) 2018 Carl Zeiss AG, Germany. All Rights Reserved.
#
# Permission is granted to use, modify and distribute this code,
# as long as this copyright notice remains part of the code.
#################################################################

### -------------------- PreScript ---------------------------------------------- ###


from System.Diagnostics import Process

filename = ' -f ' + ZenService.Experiment.ImageFileName[:-4] + '_Log.txt'
# !!! watch the space before the -c in params !!!
params = ' -c 12 -r 8'  # specify well plate format, e.g. 12 x 8 = 96 Wells

# specify the script used to display the data and call the script with arguments
exeloc = 'python'
script = r"C:\Python_Scripts\dynamic_plot_96well_animate.py"
cmd = script + filename + params


# start Python Option 1
ZenService.Xtra.System.ExecuteExternalProgram(script, filename + ' -c 12 -r 8')

# start Python Option 2
#app = Process();
#app.StartInfo.FileName = exeloc
#app.StartInfo.Arguments = cmd
# app.Start()


### -------------------- LoopScript --------------------------------------------- ###


# get number of cells from current image
cn = ZenService.Analysis.Cells.RegionsCount

# get the current well name, column idex, row index and position index
well = ZenService.Analysis.Cells.ImageSceneContainerName
col = ZenService.Analysis.Cells.ImageSceneColumn
row = ZenService.Analysis.Cells.ImageSceneRow

# create logfile
logfile = ZenService.Xtra.System.AppendLogLine(str(well)+'\t'+str(cn)+'\t'+str(col)+'\t'+str(row))


### -------------------- PostScript --------------------------------------------- ###


ZenService.Xtra.System.ExecuteExternalProgram(r"C:\Program Files\Notepad++\notepad++.exe", logfile)
