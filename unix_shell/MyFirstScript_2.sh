
#
#usage: ./MyFistScript.sh

input=Data/gapminder.txt

$ cut -f1,3,4 $input | grep 2002 | sort -n -k3 | tail -n 1 > CountryHighestLifeExp_2.txt