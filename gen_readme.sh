__dirname="`dirname \"$0\"`"
{ cat $__dirname/readme_stub.md \
&& printf "\nSameple 1: \n" \
&& python3 $__dirname/run.py \
&& printf "\nSameple 2: \n" \
&& python3 $__dirname/run.py; } > readme.md
