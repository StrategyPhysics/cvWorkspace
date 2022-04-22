#################################################################
# File       : EF_09_Jurkat_Activation.py
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
lastindex = 0
cn_last = 0
soundfile1 = r'C:\SoundFiles\PsychoScream.wav'
soundfile2 = r'C:\SoundFiles\YEAH.WAV'


### -------------------- LoopScript --------------------------------------------- ###


# get parameters
frame = ZenService.Analysis.Cells.ImageIndexTime
cn = ZenService.Analysis.Cells.RegionsCount

# calculate the change of cell numbers
delta = cn - cn_last

# write to log file (optional)
logfile = ZenService.Xtra.System.AppendLogLine(str(frame)+'\t'+str(cn)+'\t'+str(delta))
cn_last = cn

# check if the number of active cells has changed

# if active cell number has increased, play soundfile 1
if (delta > 0):
    ZenService.Xtra.System.PlaySound(soundfile2)

# if actice cell number has decreased, play soundfile 2
elif (delta < 0):
    ZenService.Xtra.System.PlaySound(soundfile1)


### -------------------- PostScript --------------------------------------------- ###


ZenService.Xtra.System.ExecuteExternalProgram(r"C:\Program Files\Notepad++\notepad++.exe", logfile)

filename = ZenService.Experiment.ImageFileName[:-4] + '_Log.txt'
exeloc = 'python'
script = r"C:\Python_Scripts\display_jurkat.py"
cmd = script + ' -f ' + filename

# start Python
app = Process()
app.StartInfo.FileName = exeloc
app.StartInfo.Arguments = cmd
app.Start()
