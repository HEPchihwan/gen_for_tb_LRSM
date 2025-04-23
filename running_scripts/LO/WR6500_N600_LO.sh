#!/bin/bash
echo "[INFO] Working in: $PWD"
git clone https://github.com/HEPchihwan/gen_for_tb_LRSM.git
cd gen_for_tb_LRSM/bin/MadGraph5_aMCatNLO/
ls
./gridpack_generation.sh WRtoNLtoLLJJtb_WR6500_N600 cards/0tb_channel/LO/WRtoNLtoLLJJtb_WR6500_N600 pdmv
ls
mkdir result_WR6500_N600
ls
mv *.tar.xz result_WR6500_N600
mv *.log result_WR6500_N600
cd result_WR6500_N600
tar -xavf *.tar.xz
FILE="runcmsgrid.sh"
sed -i 's/5000\*9/20000*9/g' "$FILE"
sed -i 's/: 5000 )/: 20000 )/g' "$FILE"

sed -i 's/10000\*9/20000*9/g' "$FILE"
sed -i 's/: 10000 )/: 20000 )/g' "$FILE"
./runcmsgrid.sh 20000 234567
