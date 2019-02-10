#!/bin/bash

DEST="$1"


if [ -e "$DEST" ] ; then
	echo "$DEST finns redan"
	exit 1
fi

mkdir "$DEST"
cp /etc/hostname "$DEST"
echo "Kopierat hostname till $DEST"
