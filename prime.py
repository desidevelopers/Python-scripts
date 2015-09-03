#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  prime.py
#  
#  Copyright 2015 Unknown <ajay@arch>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from sys import argv
from math import sqrt

def is_prime(n):
	for i in range(2, int(sqrt(n))):
		if n % i == 0:
			return False
			
	return True
	
for i in range(2, int(argv[1]) + 1):
	if is_prime(i):
		print i,
