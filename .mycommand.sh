#!/bin/bash 

#For new projects
function newproject(){
    cd
    echo 'Creating new project: ' $1
    python3 create.py $1 
    cd <project-path>$1
    echo '# README'>README.md
    git init
    git remote add origin https://github.com/<You're github username>/$1.git 
    git add .
    git commit -m "Initial commit"
    git push -u origin master 
    echo 'Created new project in <project-path>'
}
