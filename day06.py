try:
    input_file=input("File name: ")
    fp=open(input_file,'r')
    readme_list=fp.readlines()
    rls = readme_list[0].split('_') #읽어서 _를 기준으로 나눔
    print(readme_list)
    print(rls)
    fp.close()
except FileNotFoundError as err:
    print(f"{input_file} is not exist. {err}")