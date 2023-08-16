#!/bin/bash
FOLDER=${PWD}
echo -e "\nThe following files will be deleted:\n"
find "$FOLDER" -name ".DS_Store"
echo -e "\nDelete these files? (y/n): "
read -p "" DECISION
while true
do
    case $DECISION in
        [yY]* ) find "$FOLDER" -name ".DS_Store" -delete
        echo -e "\nThe files were deleted.\n"
        break;;
        [nN]* ) echo -e "\nAborting without file deletion.\n"
        exit;;
        * ) echo -e "\nAborting without file deletion.\n"
        exit;;
    esac
done