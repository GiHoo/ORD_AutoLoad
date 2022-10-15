import re
import os  
import clipboard


folder_path = os.path.realpath(os.path.dirname("__file__")) #exe 파일이 있는 폴더의 절대경로 저장

each_file_path_and_gen_time = []
for each_file_name in os.listdir(folder_path):
     if each_file_name.endswith(".txt"):  #텍스트 파일만 추출
        each_file_path = folder_path + "\\" +  each_file_name # 절대경로 + 텍스트 파일의 경로
        each_file_gen_time = os.path.getctime(each_file_path) # 텍스트 파일의 최근 수정일 저장
        each_file_path_and_gen_time.append(
             (each_file_path, each_file_gen_time) #리스트에 파일명과 파일 수정일 저장
         )  # each_file_path_and_gen_time[] 에 디렉토리 안에 있는 txt문서들 저장

most_recent_file = max(each_file_path_and_gen_time, key=lambda x: x[1])[0] #가장 최근에 수정된(마지막) 파일 선택

with open(most_recent_file,"r", encoding="UTF8") as file_in:
    lines = file_in.read().splitlines() # 최근 파일을 lines[] 배열에 저장

regex = re.compile('{}(.*){}'.format(re.escape('"'), re.escape('"'))) #정규식으로 "" 사이의 값 추출 -load ~~
text = regex.findall(lines[5]) # 5번째 / load 있는 라인

clipboard.copy(text[0]) # 클립보드에 load 저장 