#!/bin/bash
echo "[INFO] Working in: $PWD"
git clone https://github.com/HEPchihwan/gen_for_tb_LRSM.git
cd gen_for_tb_LRSM/bin/MadGraph5_aMCatNLO/
ls
./gridpack_generation.sh WRtoNLtoLLJJtb_WR3500_N1700 cards/0tb_channel/LO/WRtoNLtoLLJJtb_WR3500_N1700 pdmv
ls
mkdir result_WR3500_N1700
ls
mv *.tar.xz result_WR3500_N1700
mv *.log result_WR3500_N1700
cd result_WR3500_N1700
tar -xavf *.tar.xz
FILE="runcmsgrid.sh"
sed -i 's/5000\*9/20000*9/g' "$FILE"
sed -i 's/: 5000 )/: 20000 )/g' "$FILE"

sed -i 's/10000\*9/20000*9/g' "$FILE"
sed -i 's/: 10000 )/: 20000 )/g' "$FILE"
./runcmsgrid.sh 20000 234567
