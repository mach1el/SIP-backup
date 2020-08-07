#!/usr/bin/env python3
import sys
from asterisk.agi import *

bl_phone_num = ['0937375404','0881111111']
agi = AGI()

try:
	agi.verbose("python agi started")
	exten = agi.get_variable("phone_num")
	agi.verbose("User to call",exten)
	if exten in bl_phone_num:
		agi.set_variable('BLACKLISTED',"True")
	else:
		agi.set_variable('BLACKLISTED',"False")

except: agi.set_variable('BLACKLISTED',"False")