import os

# WR 값별로 사용할 N 리스트를 딕셔너리로 정의
WR_TO_N = {
    5100: [1020, 2550, 4700],
    5500: [1100, 2750, 5100],
}

for WRMASS in WR_TO_N:
    for NMASS in WR_TO_N[WRMASS]:
        DIRNAME = f"WRtoNLtoLLJJtb_WR{WRMASS}_N{NMASS}"
        os.makedirs(DIRNAME, exist_ok=True)

        # run_card / extramodels 복사
        os.system(f"cp skeleton_for_LO/run_card.dat {DIRNAME}/{DIRNAME}_run_card.dat")
        os.system(f"cp skeleton_for_LO/extramodels.dat {DIRNAME}/{DIRNAME}_extramodels.dat")

        # proc_card 처리
        proclines_path = "skeleton_for_LO/proc_card.dat"
        with open(proclines_path, "r") as f_in, open(f"{DIRNAME}/{DIRNAME}_proc_card.dat", "w") as f_out:
            for line in f_in:
                if "###OUTPUT" in line:
                    f_out.write(f"output {DIRNAME} --hel_recycling=False\n")
                else:
                    f_out.write(line)

        # customizecards 처리
        custolines_path = "skeleton_for_LO/customizecards.dat"
        with open(custolines_path, "r") as f_in, open(f"{DIRNAME}/{DIRNAME}_customizecards.dat", "w") as f_out:
            for line in f_in:
                if "###SETMASS9900012" in line:
                    f_out.write(f"set param_card mass 9900012 999999\n")
                elif "###SETMASS9900014" in line:
                    f_out.write(f"set param_card mass 9900014 {NMASS}\n")
                elif "###SETMASS9900016" in line:
                    f_out.write(f"set param_card mass 9900016 999999\n")
                elif "###SETMASS34" in line:
                    f_out.write(f"set param_card mass 34 {WRMASS}\n")
                else:
                    f_out.write(line)

        print(f"Generated directory and cards for WR={WRMASS}, N={NMASS}")