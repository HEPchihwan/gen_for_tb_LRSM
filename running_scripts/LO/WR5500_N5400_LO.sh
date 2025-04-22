#!/bin/bash
echo "[INFO] Working in: $PWD"
git clone https://github.com/HEPchihwan/gen_for_tb_LRSM.git
cd gen_for_tb_LRSM/bin/MadGraph5_aMCatNLO/
ls
./gridpack_generation.sh WRtoNLtoLLJJtb_WR5500_N5400 cards/0tb_channel/LO/WRtoNLtoLLJJtb_WR5500_N5400 pdmv
ls
mkdir result_WR5500_N5400
ls
mv *.tar.xz result_WR5500_N5400
mv *.log result_WR5500_N5400
cd result_WR5500_N5400

