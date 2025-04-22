#!/bin/bash
echo "[INFO] Working in: $PWD"
git clone https://github.com/HEPchihwan/gen_for_tb_LRSM.git
cd genproductions/bin/MadGraph5_aMCatNLO/
ls
./gridpack_generation.sh WRtoNLtoLLJJtb_WR2000_N1900 cards/0tb_channel/LO/WRtoNLtoLLJJtb_WR2000_N1900 pdmv
ls
mkdir result_WR2000_N1900
ls
mv *.tar.xz result_WR2000_N1900
mv *.log result_WR2000_N1900
cd result_WR2000_N1900

