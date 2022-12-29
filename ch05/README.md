# noise.py

사진 1천 장, 한 번에 만들기

해당 파일이 있는 폴더에 random_image 폴더를 생성하고, 임의의 사이즈와 색상으로 이루어진 png 파일 1000개를 생성합니다.

실행 코드

$ python noise.py

numpy, PIL 모듈 설치 필요

$ pip install numpy

$ pip install pillow

# resize.py

사진 1천 장, 사이즈 한 번에 변경하기

실행 코드

$ python resize.py <DIRECTORY> <FACTOR>

<DIRECTORY> : 사진 저장 폴더명
<FACTOR> : 변경할 비율
예를 들어 30을 입력하면 30%, 150를 입력하면 150% 사이즈가 됩니다.
