#!/bin/bash
ls | while read line
do
		sr=$(soxi -r "$line")
		if [[ $(bc <<< "$sr!=44100") == 1 ]]
		then
				echo "$line    $sr"
		fi
done
