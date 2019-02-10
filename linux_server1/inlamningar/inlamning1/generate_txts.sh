#/bin/bash

# generates random texts to num of files as argument
set -e

if [ $# -ne 1 ] 
then
	echo "Only one argument needed"
	exit 1
fi

NUMBER_FILES=$1
COUNTER=0

echo "Kommer nu skapa $NUMBER_FILES filer som heter fil1-$NUMBER_FILES.txt" 

while [ $COUNTER -le $NUMBER_FILES ]
do
	echo "Lite text till olika filer, låt oss ha lite från och till och lite mer från och till. Varför inte ha mer från" >> fil${COUNTER}.txt
	((COUNTER++))
done

echo "All done!"
