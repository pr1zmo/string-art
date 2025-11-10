# Source - https://stackoverflow.com/a/145649
# Posted by Florian Bösch, modified by community. See post 'Timeline' for change history
# Retrieved 2025-11-09, License - CC BY-SA 4.0

from ctypes import cdll
lib = cdll.LoadLibrary('./libfoo.so')

class Foo(object):
	def __init__(self):
		self.obj = lib.Foo_new()

	def bar(self):
		lib.Foo_bar(self.obj)

	def heavy_calculation(self, i):
		lib.Foo_heavy_calculation(self.obj, i)

f = Foo()
f.bar() #and you will see "Hello" on the screen
f.heavy_calculation(10000)