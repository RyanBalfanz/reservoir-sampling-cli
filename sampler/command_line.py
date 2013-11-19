#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import operator
import random
import sys


def get_parser():
	parser = argparse.ArgumentParser("Randomly sample k items from an input S containing n items.")
	parser.add_argument("infile", nargs='?', type=argparse.FileType('r'), default=sys.stdin)
	parser.add_argument("outfile", nargs='?', type=argparse.FileType('w'), default=sys.stdout)
	parser.add_argument("-k", "--num-items", type=int, help="An integer number giving the size of the reservoir")
	parser.add_argument("--preserve-order", action="store_true", help="Preserve input ordering")

	return parser

def main(argv=None):
	parser = get_parser()
	args = parser.parse_args(argv)
	N = args.num_items

	reservoir = []
	reservoir_ordered = []

	for l, line in enumerate(args.infile):
		if l < N:
			reservoir.append(line)
			reservoir_ordered.append((l, line))
		elif l >= N and random.random() < N/float(l+1):
			replace = random.randint(0, len(reservoir)-1)
			reservoir[replace] = line
			reservoir_ordered[replace] = (l, line)

	if args.preserve_order:
		for item in sorted(reservoir_ordered, key=operator.itemgetter(1)):
			args.outfile.write(item[1])
	else:
		for item in reservoir:
			args.outfile.write(item)


if __name__ == "__main__":
	sys.exit(main(sys.argv[1:]))
