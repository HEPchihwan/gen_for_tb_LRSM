#!/bin/bash
echo "[INFO] Working in: $PWD"
git clone https://github.com/HEPchihwan/gen_for_tb_LRSM.git
cd gen_for_tb_LRSM/bin/MadGraph5_aMCatNLO/
ls
./gridpack_generation.sh WRtoNLtoLLJJtb_WR3000_N2900 cards/0tb_channel/LO/WRtoNLtoLLJJtb_WR3000_N2900 pdmv
ls
mkdir result_WR3000_N2900
ls
mv *.tar.xz result_WR3000_N2900
mv *.log result_WR3000_N2900
cd result_WR3000_N2900

