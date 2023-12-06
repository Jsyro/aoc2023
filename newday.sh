#/bin/bash 
if [ -z $1 ];
then
    echo "missing 1 parameter"
    exit 1
fi
mkdir $1
cp template.py $1/sol.py
cd $1
touch input.txt
echo https://adventofcode.com/2023/day/$1/input
cd ..
