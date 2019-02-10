#!/bin/bash

ATTEND_LIST=()
COUNT=0
NAME=""

while true;
do
	echo .................................................
	echo Enter name or :q to quit or ls to list attendance
	echo Name: 
	read NAME
	if [ "$NAME" == ":q" ] ; then
		break
	elif [ "$NAME" == "ls" ] ; then
		echo
		for el in "${ATTEND_LIST[@]}"
		do
			echo "$el"
		done
	else
		ATTEND_LIST+=("$NAME")
	fi
done

echo
echo Good Bye!
