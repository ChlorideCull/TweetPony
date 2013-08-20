#!/usr/bin/env python
# Copyright (C) 2013 Julian Metzler
# See the LICENSE file for the full license.

from setuptools import setup, find_packages

setup(
	name = "TweetPony",
	version = "1.2.8-py3fork",
	description = "A Twitter library for Python 3, ported and maintained by Chloride Cull.",
	license = "AGPLv3",
	author = "Julian Metzler, Chloride Cull",
	author_email = "chloride@devurandom.net",
	url = "https://github.com/ChlorideCull/TweetPony-Python3",
	keywords = "twitter library api wrapper pony port",
	requires = ["requests (<=1.2.0)"],
	packages = find_packages()
)
