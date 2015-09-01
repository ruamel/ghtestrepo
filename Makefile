
UTILNAME:=ghtestrepo
PKGNAME:=ruamel.ghtestrepo
VERSION:=$(shell python setup.py --version)
REGEN:=/home/venv/dev/bin/ruamel_util_new util ruamel.ghtestrepo test repo for github to test PR automation --skip-hg

include ~/.config/ruamel_util_new/Makefile.inc

clean:	clean_common
#	rm -rf build .tox $(PKGNAME).egg-info/ README.pdf
#	find . -name "*.pyc" -exec rm {} +
