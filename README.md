reservoir-sampling-cli
======================

[![Build Status](https://travis-ci.org/RyanBalfanz/reservoir-sampling-cli.png)](https://travis-ci.org/RyanBalfanz/reservoir-sampling-cli)

A command line tool to randomly sample k items from an input S containing n items.

> Reservoir sampling is a family of randomized algorithms for randomly choosing a sample of k items from a list S containing n items, where n is either a very large or unknown number.
> --<cite><http://en.wikipedia.org/wiki/Reservoir_sampling></cite>

Installation
------------

	# From PyPI
	pip install reservoir-sampling-cli # From PyPI
	# From Github
	pip install -e git+ssh://git@github.com/RyanBalfanz/preservoir-sampling-cli.git#egg=resamp

Usage
-----

Show help message

	$ resamp -h
	usage: Randomly sample k items from an input S containing n items.
	       [-h] [-k NUM_ITEMS] [--preserve-order]
	       [infile] [outfile]

	positional arguments:
	  infile
	  outfile

	optional arguments:
	  -h, --help            show this help message and exit
	  -k NUM_ITEMS, --num-items NUM_ITEMS
	                        An integer number giving the size of the reservoir
	  --preserve-order      Preserve input ordering

Sample 10 words from /usr/share/dict/words preserving the original order

	$ cat /usr/share/dict/words | resamp -k10 --preserve-order
	Paralipomenon
	frankalmoign
	hauntingly
	hellion
	laniiform
	lithify
	semicollapsible
	sniveled
	stolkjaerre
	unaloud
