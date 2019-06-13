#!/bin/bash

read -s -p "Username: " user
read -s -p "Password: " password
echo $user
credentials="${user}:${password}"

declare -a repositoryNames=("slingware-root-project"
				"structured-resource-models"
				"ui-libraries"
				"kestros-cms-foundation"
				"kestros-site-admin-ui"
				"kestros-forms-foundation"
				"kestros-login"
				"kestros-site-administration"
				"kestros-user-management-core"
				"kestros-build-helper"
				)

## now loop through the above array
for name in "${repositoryNames[@]}"
do
	cd ~/Documents/Kestros/$(echo $name)/
	pwd
	git pull https://${credentials}@github.com:slingware/${name}.git >/dev/null 2>&1
	mvn clean install
   # or do whatever with individual element of the array
done