from Read import Read_code
import re

class program_start:
    
    def __init__(program, code):
        program.code = Read_code(code)
        
    def __str__(program):
        return f"{program.code.body}"
    
    def find_imports(program):
        Line = 0
        for line in program.code.body:
            if(program.code.depth_finder(Line) == 0):
                s = program.code.remove_space(Line)
                if 'import' in s:
                    index = s.find('import')
                    print("    import class: ", program.code.body[Line][7:], end = "")
            Line += 1
            
    def find_class(program):
        Line = 0
        for line in program.code.body:
            if(program.code.depth_finder(Line) == 0):
                s = program.code.remove_space(Line)
                if 'class' in s:
                    index = s.find('class')
                    spareted_string = program.code.body[Line][6:].partition('(')
                    class_name = spareted_string[0].lstrip()
                    
                    parets = str(program.code.body[Line][6:])
                    parents = re.findall(r'\(.*?\)', parets)
                    parents = ''.join(map(str, parents))
                    parents = parents.replace('(','').replace(')','').replace(' ','') 
                    
                    print("    class: ", class_name, "/ class parents: ", parents, " {",sep='')
            Line += 1
