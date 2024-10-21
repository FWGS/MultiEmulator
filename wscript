#! /usr/bin/env python
# encoding: utf-8
# mittorn, 2018

from waflib import Logs
import os

top = '.'

def options(opt):
	return

def configure(conf):
	return

def build(bld):
	bld.stlib(
		source   = bld.path.ant_glob(['src/*.cpp']),
		target   = 'MultiEmulator',
		features = 'cxx',
		includes = ['include/', 'src/'],
		export_includes = ['include/'],
		subsystem = bld.env.MSVC_SUBSYSTEM
	)

	if bld.env.TESTS:
		tests = {
			'sha256': 'tests/test_sha256.cpp',
		}

		for i in tests:
			bld.program(features = 'test',
				source = tests[i],
				target = 'test_%s' % i,
				includes = 'src/',
				use = 'MultiEmulator',
				subsystem = bld.env.CONSOLE_SUBSYSTEM,
				install_path = None)