#!/bin/bash

for F in * ; do
if [ -d "$F" ] ; then
	echo "$F" is a directory
else
	echo "$F" is a file
fi
done
