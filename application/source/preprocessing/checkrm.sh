#!/bin/bash
lim=$1
ls | while read line
do
		num=$(soxi -D "$line")
		if [[ $(bc <<< "$num>$lim") == 1 ]]
		then
				rm "$line"
		fi
done
