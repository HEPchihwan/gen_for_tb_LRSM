import os
import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class MassRecoFromLHE:
    def __init__(self, lhe_path, WR_mass):
        self.lhe_path = lhe_path
        self.WR_mass = WR_mass
        self.finalstate_masses = []
        self.finalstate_mass_count = 0
        self.offshell_count = 0

    def _get_four_vector(self, px, py, pz, E):
        return {"px": px, "py": py, "pz": pz, "E": E}

    def _invariant_mass(self, p):
        E = p["E"]
        px = p["px"]
        py = p["py"]
        pz = p["pz"]
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
            status = int(cols[1])
            px, py, pz, E = map(float, cols[6:10])
            particles.append({
                "status": status,
                "px": px,
                "py": py,
                "pz": pz,
                "E": E
            })

        final_particles = [p for p in particles if p["status"] == 1]
        if not final_particles:
            return

        px_tot = sum(p["px"] for p in final_particles)
        py_tot = sum(p["py"] for p in final_particles)
        pz_tot = sum(p["pz"] for p in final_particles)
        E_tot  = sum(p["E"]  for p in final_particles)

        mass2 = E_tot**2 - px_tot**2 - py_tot**2 - pz_tot**2
        mass = np.sqrt(mass2) if mass2 > 0 else 0

        self.finalstate_mass_count += 1
        self.finalstate_masses.append(mass)

        if mass < 0.5 * self.WR_mass:
            self.offshell_count += 1

# --- 작업 디렉토리 설정 ---
base_dir = "/data6/Users/snuintern1/tbchannel/gen_for_tb_LRSM/condorfiles/LO"
output_csv_path = "/data6/Users/snuintern1/tbchannel/gen_for_tb_LRSM/analysis/result/offshell_count/total_WR.csv"
output_plot_dir = "/data6/Users/snuintern1/tbchannel/gen_for_tb_LRSM/analysis/result/offshell_count/total_mass_reco_plots"

os.makedirs(output_plot_dir, exist_ok=True)

summary_records = []

# --- 전체 LHE 파일 탐색 ---
lhe_files = glob.glob(f"{base_dir}/result_WR*_N*/cmsgrid_final.lhe")
print(f"총 {len(lhe_files)}개 파일 발견됨.")

for lhe_path in lhe_files:
    try:
        folder_name = os.path.basename(os.path.dirname(lhe_path))
        parts = folder_name.replace("result_", "").split("_")
        WR_mass = int(parts[0].replace("WR", ""))
        N_mass = int(parts[1].replace("N", ""))
        label = f"WR{WR_mass}_N{N_mass}"

        print(f"🔍 처리 중: {label}")

        # --- mass reco 수행 ---
        reco = MassRecoFromLHE(lhe_path, WR_mass)
        reco.Run()

        summary_records.append({
            "WR_mass": WR_mass,
            "N_mass": N_mass,
            "total_count": reco.finalstate_mass_count,
            "offshell_count": reco.offshell_count
        })

        # --- 히스토그램 저장 ---
        plt.figure(figsize=(8, 6))
        if reco.finalstate_masses:
            plt.hist(reco.finalstate_masses, bins=50, histtype='step', label="Final-state sum", linewidth=1.5)
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
