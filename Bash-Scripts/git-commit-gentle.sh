#!/usr/bin/env bash

git status

echo "Which file?"

read plik

git add $plik

echo "What is your commit message?"

read commit

git commit -m "$commit"

git push
