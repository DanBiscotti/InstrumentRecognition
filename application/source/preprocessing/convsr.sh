#!/bin/bash
ls | while read line
do
		sr=$(soxi -r "$line")
		if [[ $(bc <<< "$sr!=44100") == 1 ]]
		then
				sox "$line" -r 44100 new"$line"
				rm "$line"
		fi
done
