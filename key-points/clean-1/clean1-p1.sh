#!/usr/bin/zsh
cat ../../../../capstone/dataste-generation/cappy-definitive-edition/step2/z_output/input_nodes_copy_deployment_000.csv | awk -F ";" '{print $1";"$3}' > clean1-part1.csv
