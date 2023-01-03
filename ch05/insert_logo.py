import time
import os
from PIL import Image
import sys

# 작업 시작 메시지를 출력합니다.
print("Process Start.")

# 시작 시점의 시간을 기록합니다.
start_time = time.time()

# 사진이 저장된 폴더명을 입력 받습니다.
directory = sys.argv[1]

# 사진에 삽입될 로고 파일을 입력 받습니다.
logo_filename = sys.argv[2]

# 결과물을 저장할 폴더를 생성합니다.
out_dir = "images_with_logo"
if out_dir not in os.listdir():
    os.mkdir(out_dir)

# 폴더의 내용물을 열람해 목록을 생성합니다.
input_files = os.listdir(directory)

# 로고 파일을 불러옵니다.
logo = Image.open(logo_filename)
logo_x, logo_y = logo.size

# input_files에 저장된 파일 이름을 한 번에 하나씩 불러옵니다.
for file_name in input_files:
    # 이미지 파일이 아닐 경우 걸러냄
    exp = file_name.strip().split(".")[-1]
    if exp not in "JPG jpg JPEG jpeg PNG png BMP bmp":
        continue

    # 이미지를 불러옵니다.
    image = Image.open(directory + "/" + file_name)

    # 이미지의 크기를 알아냅니다.
    Xdim, Ydim = image.size

    # 로고의 X축 길이가 이미지보다 클 경우
    if logo_x / Xdim > logo_y / Ydim:
        # 로고의 x축 길이를 이미지의 x축 길이의 1/5로 조절합니다.
        new_logo_x = int(Xdim / 5)
        # 로고의 y축 길이는 비례
        new_logo_y = int(logo_y * (new_logo_x / logo_x))

    else:
        new_logo_y = int(Ydim / 5)
        new_logo_x = int(logo_x * (new_logo_y / logo_y))

    # 이미지 크기에 맞게 축소/확대된 로고 만듭니다.
    resized_logo = logo.resize((new_logo_x, new_logo_y))

    # 사진에 로고를 적당한 위치( 여백의 2% )에 삽입합니다.
    image.paste(resized_logo, (int(Xdim / 50), int(Ydim / 50)), resized_logo)

    # 변경된 이미지를 저장합니다.
    image.save(out_dir + "/" + file_name)

    # 이미지를 닫아줍니다.
    image.close()

# 작업 종료 메시지를 출력합니다.
print("Process Done.")

# 작업에 총 몇 초가 걸렸는지 출력합니다.
end_time = time.time()
print("The Job Took : " + str(end_time - start_time) + " seconds.")
