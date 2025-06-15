wr_start = 1000
wr_end = 6500
wr_step = 500

for wr in range(wr_start, wr_end + 1, wr_step):
    for n in range(100, wr, 100):
        tag = f"WR{wr}_N{n}"
        filename = f"{tag}_LO.sh"
        content = f"""#!/bin/bash
echo "[INFO] Working in: $PWD"
git clone https://github.com/HEPchihwan/gen_for_tb_LRSM.git
cd gen_for_tb_LRSM/bin/MadGraph5_aMCatNLO/
ls
./gridpack_generation.sh WRtoNLtoLLJJtb_{tag} cards/top_decay_to_only_wr/WRtoNLtoLLJJtb_{tag} pdmv
ls
mkdir result_{tag}
ls
mv *.tar.xz result_{tag}
mv *.log result_{tag}
cd result_{tag}
tar -xavf *.tar.xz
FILE="runcmsgrid.sh"
sed -i 's/5000\*9/20000*9/g' "$FILE"
sed -i 's/: 5000 )/: 20000 )/g' "$FILE"

sed -i 's/10000\*9/20000*9/g' "$FILE"
sed -i 's/: 10000 )/: 20000 )/g' "$FILE"
./runcmsgrid.sh 20000 234567
"""

        with open(filename, 'w') as f:
            f.write(content)

        print(f"✅ Generated: {filename}")
