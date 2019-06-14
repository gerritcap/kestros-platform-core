#!/bin/bash

read -s -p "Username: " user
read -s -p "Password: " password
echo $user
credentials="${user}:${password}"

declare -a repositoryNames=("kestros-build-helper"
							"slingware-root-project"
							"structured-resource-models"
							"ui-libraries"
							"kestros-cms-foundation"
							"kestros-site-admin-ui"
							"kestros-forms-foundation"
							"kestros-login"
							"kestros-site-administration"
 							"kestros-user-management-core"
							)


for name in "${repositoryNames[@]}"
do
		## Add If Logic to check if folder exists, Create it if not.
		cd ../$(echo $name)/
		pwd
		git pull https://${credentials}@github.com/slingware/${name}.git #>/dev/null 2>&1
		if [ name != "kestros-build-helper" ]; then
			mvn clean install -PinstallPackage;
		fi
done
