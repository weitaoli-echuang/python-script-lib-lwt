# coding=utf-8

from lwt_python_lib.Paths import Paths

if __name__ == '__main__':
	print 'here'
	path_name = r'''D:\lwtworker\DHII1\anatable\src\TestGPUProgram'''
	path = Paths(path_name)

	# child_directory = path.directory()
	# child_file = path.files()
	#
	# print 'directories '
	# for d in child_directory:
	# 	print d
	#
	# print 'files '
	# for f in child_file:
	# 	print f

	first_file = r"""D:\lwtworker\DHII1\anatable\src\TestGPUProgram\TestCases\TestCaseFactory.h"""
	second_file = r"""D:\lwtworker\DHII1\anatable\src\TestGPUProgram\RenderingAlgorithms\RenderWithTimeSlice\Raycasting_CT\GPURaycastingCTBrick.cpp"""
	print path.relative_path(first_file, second_file)
