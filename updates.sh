#!/usr/bin/env bash

cd ~/Documents/Python3/tutorial

## declare an array variable
declare -a arr=("artemisu" "daphneu" "fleuru" "morganau" "riasu" "artemis" "daphne" "diana" "fleur" "favorites" "morgana" "rias")

## now loop through the above array
for i in "${arr[@]}"
do
   rm "$i.json"
   scrapy crawl $i -o "$i.json"
   # or do whatever with individual element of the array
done

#rm artemisu.json
#
#rm daphneu.json
#
#rm dianu.json
#
#rm fleuru.json
#
#rm morganau.json
#
#rm riasu.json
#
#scrapy crawl artemisu -o artemisu.json
#
#scrapy crawl daphneu -o daphneu.json
#
#scrapy crawl dianu -o dianu.json
#
#scrapy crawl fleuru -o fleuru.json
#
#scrapy crawl morganau -o morganau.json
#
#scrapy crawl riasu -o riasu.json