import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pyhepmc as hep

class MassRecoFromLHE:
    def __init__(self, lhe_path):
        self.lhe_path = lhe_path
        self.on_shell_masses = []
        self.off_shell_masses = []
        self.on_shell_count = 0
        self.off_shell_count = 0

    def _get_four_vector(self, px, py, pz, E):
        return {"px": px, "py": py, "pz": pz, "E": E}

    def _invariant_mass(self, p1, p2):
        E = p1["E"] + p2["E"]
        px = p1["px"] + p2["px"]
        py = p1["py"] + p2["py"]
        pz = p1["pz"] + p2["pz"]
        return np.sqrt(max(E**2 - px**2 - py**2 - pz**2, 0))

    def Run(self):
        with open(self.lhe_path, 'r') as f:
            lines = f.readlines()

        inside_event = False
        event_lines = []

        for line in lines:
            if '<event>' in line:
                inside_event = True
                event_lines = []
                continue
            elif '</event>' in line:
                inside_event = False
                self._process_event(event_lines)
                continue
            if inside_event:
                event_lines.append(line.strip())

    def _process_event(self, event_lines):
        if not event_lines:
            return
        try:
            n_particles = int(event_lines[0].split()[0])
        except:
            return

        particles = []
        for i in range(1, n_particles + 1):
            cols = event_lines[i].split()
            if len(cols) < 10:
                continue
            pid = int(cols[0])
            mother1 = int(cols[2])
            mother2 = int(cols[3])
            px, py, pz, E = map(float, cols[6:10])
            
            # 파티클 리스트 만들 때 status 추가
            status = int(cols[1])
            particles.append({
            "pid": pid,
            "status": status,
            "mother1": mother1,
            "mother2": mother2,
            "px": px,
            "py": py,
            "pz": pz,
            "E": E,
            "idx": i
        })

            for p in particles:
                if p["pid"] == 34:
                    m1, m2 = p["mother1"], p["mother2"]
                    parent_statuses = []
                    for mid in (m1, m2): 
                        parent = next((pp for pp in particles if pp["idx"] == mid), None)
                        if parent:
                            parent_statuses.append(parent["status"])
                    if any(s == -1 for s in parent_statuses): # onshell WR 중에서 first 꺼 골라내기 
                        mass2 = p["E"]**2 - (p["px"]**2 + p["py"]**2 + p["pz"]**2)
                        mass = np.sqrt(mass2) if mass2 > 0 else 0
                        self.on_shell_count += 1
                        self.on_shell_masses.append(mass)
                    return

        # off-shell N-뮤온 짝 찾기
        N_particles = [p for p in particles if p["pid"] == 9900012]
        electrons = [p for p in particles if abs(p["pid"]) == 11]

        for Np in N_particles:
            N_parents = {Np["mother1"], Np["mother2"]}
            for mp in electrons:
                electron_parents = {mp["mother1"], mp["mother2"]}
                if N_parents & electron_parents:
                    p1 = self._get_four_vector(Np["px"], Np["py"], Np["pz"], Np["E"])
                    p2 = self._get_four_vector(mp["px"], mp["py"], mp["pz"], mp["E"])
                    mass = self._invariant_mass(p1, p2)
                    self.off_shell_masses.append(mass)
                    self.off_shell_count += 1
                    return

# --- 작업 디렉토리 설정 ---
base_dir = "/data6/Users/snuintern1/tbchannel/gen_for_tb_LRSM/condorfiles/LO"
output_csv_path = "/data6/Users/snuintern1/tbchannel/gen_for_tb_LRSM/analysis/result/offshell_count/mass_reco_summary_counts_electron.csv"
output_plot_dir = "/data6/Users/snuintern1/tbchannel/gen_for_tb_LRSM/analysis/result/offshell_count/mass_reco_plots_electron"

os.makedirs(output_plot_dir, exist_ok=True)

# --- 전체 결과 저장용 리스트 ---
summary_records = []

# --- 전체 LHE 파일 탐색 ---
lhe_files = glob.glob(f"{base_dir}/result_WR*_N*/cmsgrid_final.lhe")
print(f"총 {len(lhe_files)}개 파일 발견됨.")

for lhe_path in lhe_files:
    try:
        # --- 폴더 이름 parsing ---
        folder_name = os.path.basename(os.path.dirname(lhe_path))
        parts = folder_name.replace("result_", "").split("_")
        WR_mass = int(parts[0].replace("WR", ""))
        N_mass = int(parts[1].replace("N", ""))

        label = f"WR{WR_mass}_N{N_mass}"

        print(f"🔍 처리 중: {label}")

        # --- mass reco 수행 ---
        reco = MassRecoFromLHE(lhe_path)
        reco.Run()

        # --- CSV용 summary 기록 ---
        if reco.on_shell_masses:
            percentile_99 = np.percentile(reco.on_shell_masses, 1)  
            offshell_below99 = sum(m < percentile_99 for m in reco.off_shell_masses)  
        else:
            percentile_99 = None
            offshell_below99 = 0

        summary_records.append({
        "WR_mass": WR_mass,
        "N_mass": N_mass,
        "on_shell_count": reco.on_shell_count,
        "off_shell_count": reco.off_shell_count,
        "offshell_below99_count": offshell_below99  
        })

        # --- 히스토그램 저장 ---
        plt.figure(figsize=(8,6))
        if reco.on_shell_masses:
            plt.hist(reco.on_shell_masses, bins=50, histtype='step', label="On-shell W'", linewidth=1.5)
        if reco.off_shell_masses:
            plt.hist(reco.off_shell_masses, bins=50, histtype='step', label="Off-shell reco mass", linewidth=1.5)
        plt.xlabel("Mass [GeV]")
        plt.ylabel("Events")
        plt.title(f"Mass Reconstruction: {label}")
        plt.grid(True)
        plt.legend()
        plot_path = os.path.join(output_plot_dir, f"{label}.png")
        plt.savefig(plot_path)
        plt.close()
        print(f"🖼️ 그림 저장 완료: {plot_path}")

    except Exception as e:
        print(f"❌ 에러 발생 ({lhe_path}): {e}")

# --- 최종 summary를 CSV로 저장 ---
df_summary = pd.DataFrame(summary_records)
df_summary.to_csv(output_csv_path, index=False)
print(f"\n✅ 최종 summary CSV 저장 완료: {output_csv_path}")