#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#  first.py
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

a = input("Enter some value: ")
b = input("Enter some value: ")

if (a < b) and (a == b):
	print "%d is less than %d" % (a, b)
	print "Not Errornous statement"
else:
	print "%d is greater than or equal to %d" % (a, b)
	print "Else body still works.."
	print "Else body still works.."
	print "Else body still works.."
	
print "Main body"