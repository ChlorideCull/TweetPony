#!/usr/bin/env python
# Copyright (C) 2013 Julian Metzler
# See the LICENSE file for the full license.

from setuptools import setup, find_packages

setup(
	name = "TweetPony",
	version = "1.2.8-py3fork",
	description = "A Twitter library for Python",
	license = "AGPLv3",
	author = "Julian Metzler",
	author_email = "contact@mezgrman.de",
	url = "https://github.com/Mezgrman/TweetPony",
	keywords = "twitter library api wrapper pony",
	requires = ["requests (<=1.2.0)"],
	packages = find_packages()
)
