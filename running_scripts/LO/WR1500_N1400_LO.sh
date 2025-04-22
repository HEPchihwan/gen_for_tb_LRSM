#!/bin/bash
echo "[INFO] Working in: $PWD"
git clone https://github.com/HEPchihwan/gen_for_tb_LRSM.git
cd genproductions/bin/MadGraph5_aMCatNLO/
ls
./gridpack_generation.sh WRtoNLtoLLJJtb_WR1500_N1400 cards/0tb_channel/LO/WRtoNLtoLLJJtb_WR1500_N1400 pdmv
ls
mkdir result_WR1500_N1400
ls
mv *.tar.xz result_WR1500_N1400
mv *.log result_WR1500_N1400
cd result_WR1500_N1400

