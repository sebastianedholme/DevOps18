# Lists only files and not directories
for F in * ; do
	if [ -f "$F" ] ; then
		echo "$F"
	fi
done
