import sys
import unittest
import cStringIO as StringIO
from contextlib import contextmanager

from sampler.command_line import main


@contextmanager
def stdout_redirected(new_stdout):
	save_stdout = sys.stdout
	sys.stdout = new_stdout
	try:
		yield None
	finally:
		sys.stdout = save_stdout


class CLITestCase(unittest.TestCase):
	def setUp(self):
		pass

	def test_help(self):
		args = r"-h".split()
		with self.assertRaises(SystemExit) as cm:
			main(args)

		the_exception = cm.exception
		self.assertEqual(the_exception.code, 0)

	def test_command(self):
		myOut = StringIO.StringIO()
		with stdout_redirected(myOut):
			args = r"-k 10 words.txt".split()
			main(args)
			output = myOut.getvalue().strip()

			self.assertTrue(output)
			self.assertEqual(len(output.splitlines()), 10)

	def test_preserve_order(self):
		myOut = StringIO.StringIO()
		with stdout_redirected(myOut):
			args = r"-k 10 words.txt --preserve-order".split()
			main(args)
			output = myOut.getvalue().strip()

			self.assertTrue(output)
			self.assertEqual(len(output.splitlines()), 10)


if __name__ == '__main__':
	unittest.main()
