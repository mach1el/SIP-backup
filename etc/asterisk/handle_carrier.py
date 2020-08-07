#!/usr/bin/env python3
import sys
from asterisk.agi import *

agi = AGI()
match_prefix = {
		"VIETTEL" : ["096","097","098","086","032","033","034","035","036","037","038","039"],
		"VINA" : ["091","094","081","082","083","084","085","088"],
		"MOBI" : ["090","093","089","070","077","078","079","076"],
		"vietnam mobile" : ["092","052","056","058"],
		"gtel" : ["099","059"]
}

agi.verbose("python agi started")
digits = agi.get_variable("digits")
agi.verbose(" Digits of carrier",digits)
x = [ i for i in match_prefix.keys() if str(digits) in match_prefix[i] ]
agi.set_variable("Call_Network",str(x[0]))