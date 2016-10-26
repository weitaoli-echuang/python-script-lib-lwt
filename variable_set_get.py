# coding=utf-8
import re

from lwt_python_lib.Paths import Paths

__author__ = 'VDTConstructor'

if __name__ == '__main__':
	f_path = r"""D:\lwtworker\DHII1\anatable\src\RenderPlatform"""
	files = Paths(f_path).files()

	pattern_set = re.compile(r'''variable_store\.(Set)\((.+),(.+)\);''')
	pattern_get = re.compile(r'''variable_store\.(Get)<(.+)>\((.+),(.+)\);''')

	for file_name in files:
		with open(file_name) as f:
			data = f.readlines()
			for line in data:
				line_match_set = re.findall(pattern_set, line)
				line_match_get = re.findall(pattern_get, line)
				if len(line_match_set) > 0:
					# print line_match_set
					print line_match_set[0][1].replace('"', '').replace('+', '').replace(' ', '')
				# if len(line_match_get) > 0:
				# 	print line_match_get
