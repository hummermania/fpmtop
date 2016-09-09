#!/bin/sh

# Make zip with sources
tar cvfz ~/buildroot/SOURCES/fpmtop-0.0.1.tar.gz --exclude=.git --exclude=.gitignore .

rpmbuild -bs specs/fpmtop.spec

mock -r epel-7-x86_64 ~/buildroot/SRPMS/fpmtop-0.0.1-1.el6.src.rpm 
