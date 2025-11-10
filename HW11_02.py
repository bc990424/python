import zipfile
import sys
file_name = input()

if file_name.endswith(".zip"):
    with zipfile.ZipFile(file_name,'r') as zf:
        try:
            zf.extractall()
            print("suceeee")
        except Exception as a:
            print(a)



else:
    print("zip을 끝나지 않음")
