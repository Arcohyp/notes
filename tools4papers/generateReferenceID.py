import re  
  
def extract_cite_keys(bib_file_path):  
    with open(bib_file_path, 'r', encoding='utf-8') as file:  
        content = file.read()  
      
    # 正则表达式匹配每个条目的类型和键  
    pattern = r'@(\w+)\{(.*?),'  
    matches = re.findall(pattern, content, re.DOTALL)  
      
    # 提取键并构建\cite{}字符串  
    cite_strings = [r'\cite{' + match[1] + '}' for match in matches]  
      
    return cite_strings  
  
def write_to_txt(cite_strings, output_file_path):  
    with open(output_file_path, 'w', encoding='utf-8') as file:  
        for cite in cite_strings:  
            file.write(cite + '\n')  
  
# 使用函数  
bib_file = 'path_to_your_bib_file.bib'  # 替换为你的.bib文件路径  
output_txt = 'output_citations.txt'  # 输出文件的名称  
  
cite_strings = extract_cite_keys(bib_file)  
write_to_txt(cite_strings, output_txt)  
  
print(f'Extracted citations have been written to {output_txt}')
