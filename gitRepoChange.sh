#!/bin/bash
#Changes the repository when adding files 

echo "The current repository is $(git config --get remote.origin.url)"
echo "Change repository?(y/n)"
read $change
if [ "$change" = "y" ]; then 
	echo "Enter repository to redirect: "
	read ${newRepo}.git
	git remote add origin git@github.com:ma3lstrom/$newRepo
fi