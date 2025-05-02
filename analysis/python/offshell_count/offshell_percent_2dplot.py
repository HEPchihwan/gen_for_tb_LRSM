import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# CSV 파일 불러오기
df = pd.read_csv("/data6/Users/snuintern1/tbchannel/gen_for_tb_LRSM/analysis/result/offshell_count/sorted_output_muon.csv")

# 비율 계산
df["ratio"] = df["offshell_below99_count"] / (df["on_shell_count"] + df["off_shell_count"])*100

# 500단위 binning
df["WR_bin"] = df["WR_mass"] 
df["N_bin"] = df["N_mass"] 

# 피벗 테이블 생성: index=N_bin, columns=WR_bin, values=ratio
pivot_table = df.pivot_table(index="N_bin", columns="WR_bin", values="ratio")

# 플롯
plt.figure(figsize=(10, 8))
sns.heatmap(pivot_table, annot=True, fmt=".2f", cmap="viridis", cbar_kws={"label": "Ratio"})
plt.title("Off-shell (<99% on-shell mass)/on+off-shell percentage of WR")
plt.xlabel("WR mass [GeV]")
plt.ylabel("N mass [GeV]")
plt.tight_layout()
plt.gca().invert_yaxis()
plt.show()
plt.savefig("offshell_percent_muon.png", dpi=500)

