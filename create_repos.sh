#!/bin/bash

repos=("EternaFX-AGI" "EternaFX-Quantum" "EternaFX-Classical" "EternaFX-ML" "EternaFX-Collab" "EternaFX-Utils" "EternaFX-ChatAnalysis" "EternaFX-Millennium")

for repo in "${repos[@]}"
do
  echo "Creating $repo repository on GitHub..."
  gh repo create aiKC91/$repo --public --description "$repo for EternaFX Framework" --clone
  cd $repo

  echo "Generating basic folder structure for $repo..."
  mkdir -p config data docs src tests scripts notebooks
  touch config/config.yaml
  touch data/.gitkeep
  touch docs/README.md
  touch src/main.py
  touch tests/test_${repo,,}.py
  touch scripts/deploy.sh
  touch notebooks/${repo,,}_prototype.ipynb
  echo "# $repo" > README.md

  git add .
  git commit -m "Initial commit for $repo"
  git push origin main

  cd ..
done