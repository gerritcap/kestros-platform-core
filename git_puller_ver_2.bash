#!/bin/bash

read -s -p "Username: " user
read -s -p "Password: " password
read -s -p "Verify Password: " password1

while [ $password != $password1 ]; do
echo Password Mismatch, Try again
read -s -p "Password: " password
read -s -p "Verify Password: " password1
done

echo $user
credentials="${user}:${password}"

path=$(pwd)

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
                                                        "kestros-guides-core"
                                                        )


for name in "${repositoryNames[@]}"
do
        ## Add If Logic to check if folder exists, Create it if not.
        if [[ ! -d $path/$(echo $name)/ ]]; then
                sudo mkdir -p $path/$(echo $name)/
                echo Directory Missing
                #path_true=False
        fi
        cd $path/$(echo $name)/
        echo Directory Changed
        pwd
        git pull https://${credentials}@github.com/slingware/${name}.git #>/dev/null 2>&1
        if [ name != "kestros-build-helper" ];  then
                mvn clean install -PinstallPackage;
        fi
done
