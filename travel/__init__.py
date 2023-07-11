import os


folder =  "sample_dir"
if os.path.exists(folder):
    print("이미 폴더가 존재합니다")
else:
    os.makedirs(folder)
    print(folder, "폴더를 생성했습니다")