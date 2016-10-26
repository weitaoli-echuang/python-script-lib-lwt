# coding=utf-8
import os

__author__ = 'VDTConstructor'


class Paths:
	"""support relative path methods"""

	def __init__(self, path):
		"""Constructor for Paths"""
		self.__path = path
		self.__walk()

	def __walk(self):
		self.__directory = list()
		self.__file = list()
		for dirpath, dirnames, filenames in os.walk(self.__path):
			if len(dirnames) > 0:
				path_dir = [os.path.join(dirpath, d) for d in dirnames]
				self.__directory.extend(path_dir)
			if len(filenames) > 0:
				path_file = [os.path.join(dirpath, f) for f in filenames]
				self.__file.extend(path_file)

	def directory(self, ):
		"""return the child directory of"""
		return self.__directory

	def files(self, ):
		"""return files list contained in this """
		return self.__file

	@classmethod
	def relative_path(self, first_file, second_file):
		"""return relative path of two files"""
		return os.path.relpath(first_file, second_file)
