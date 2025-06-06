import os
import re
import pandas as pd

# 1) 상위 경로
base_path = "/data6/Users/snuintern1/tbchannel/gen_for_tb_LRSM/condorfiles/LO_up_to_tb/"

# 2) 폴더 이름 패턴: result_WR{숫자}_N{숫자}
dir_pattern = re.compile(r"^result_WR(\d+)_N(\d+)$")

# 3) gridlock 파일 안에서 Cross-section 파싱용 정규식
xsec_pattern = re.compile(r"Cross-section\s*:\s*([0-9eE.+-]+)")

# 4) 결과 저장용 딕셔너리: {(WR, N): crosssection 값}
results = {}

# 5) base_path 아래를 순회하면서 하위 디렉터리 확인
for entry in os.listdir(base_path):
    entry_path = os.path.join(base_path, entry)
    if not os.path.isdir(entry_path):
        continue

    # 디렉터리 이름이 패턴에 맞는지 확인
    m = dir_pattern.match(entry)
    if not m:
        continue

    WR = int(m.group(1))
    N  = int(m.group(2))
    key = (WR, N)

    # 해당 폴더 안의 파일들을 훑어보면서 "gridlock"으로 시작하는 파일 찾기
    for fname in os.listdir(entry_path):
        if not fname.startswith("gridpack"):
            continue

        file_path = os.path.join(entry_path, fname)
        try:
            with open(file_path, "r") as f:
                content = f.read()
        except UnicodeDecodeError:
            # 텍스트 인코딩 문제로 파일을 읽을 수 없을 때(바이너리 파일 등) 무시
            continue

        # "Cross-section :" 뒤 숫자 추출
        xm = xsec_pattern.search(content)
        if xm:
            xsec_val = float(xm.group(1))
            # 동일 (WR, N) 쌍에 여러 개의 gridlock 파일이 있으면, 마지막으로 찾은 값을 덮어씀
            results[key] = xsec_val
            # (원한다면) 첫 번째 매치를 찾고 멈추려면 break 사용
            # break

# 6) DataFrame 생성 및 정렬
rows = []
for (WR, N) in sorted(results.keys(), key=lambda x: (x[0], x[1])):
    rows.append({
        "WR": WR,
        "N": N,
        "CrossSection": results[(WR, N)]
    })

df = pd.DataFrame(rows)
df = df.sort_values(by=["WR", "N"]).reset_index(drop=True)

# 7) CSV로 저장
output_path = "/data6/Users/snuintern1/tbchannel/gen_for_tb_LRSM/analysis/result/20000event/tbchannel_crosssections.csv"
df.to_csv(output_path, index=False, float_format="%.6g")

print(f"Saved to {output_path}")