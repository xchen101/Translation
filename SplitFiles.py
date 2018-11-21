import re
import sys
import glob
import math
import random
from array import *

def ReadLogFileEntries (logfilename,outName,badlines,StoppLine) :
    f = open(outName,'w')
    for filename in glob.iglob(logfilename):
        linenumber = 0
        for line in open(filename, 'r'):
           linenumber += 1
           isGoodLine = True
           for i in badlines:
              if i == linenumber:
                 isGoodLine = False
           if isGoodLine == True:
              line=line.split("\n")[0]
              print(line,file=f)
           if linenumber >= StoppLine:
              linenumber = 0 

ReadLogFileEntries(".srt","English.srt",[1,2],4)
#numbers in the square bracket is what's being taken out. 
#ReadLogFileEntries("YGWS_Sub_full.txt","outputfileEnglish.txt",[3,5],6)
#ReadLogFileEntries("YGWS_Sub_full.txt","outputfileChinese.txt",[4,5],6)

