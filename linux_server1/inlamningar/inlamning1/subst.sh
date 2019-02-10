#!/bin/bash

set -e

# Subst är ordet vi vill ersätta, with är ordet vi vill ha kvar i filen
SUBST=$1
WITH=$2

# Hantera om för få argument med -lt (less then)
# $# == hur många argument som man skickat in
if [ $# -lt 3 ]
then
	echo "Måste vara minst 3 argument! Avbryter scriptet"
	sleep 1
	exit 1
fi

# Loopa igenom resten av argumenten som är filer där ord ska sökas och ersättas
# $@ är alla argument
# ${@:num} Där num är en slice av alla argument liknande som i python
for arg in "${@:3}"
do
	if [ ! -e "$arg" ] 
	then
		echo "Filen $arg finns inte, avbryter scriptet"
		sleep 1
		exit 1
	else
		sed -i "s/${SUBST}/${WITH}/g" "$arg"
	fi
done
