class program_start:
    
    def __init__(program, code):
        program.code = Read_code(code)
        program.numberOfLines = program.code.line_counter()
        
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
            
            
    def def_confirm(program, Line):
        s = program.code.remove_space(Line)
        if 'def' in s:
            return True
        else:
            return False
        
    def extract_def(program, Line):
        
        def_depth = program.code.depth_finder(Line)
        start_line = Line
        for counter in range(start_line+1, program.numberOfLines):
            if(program.code.depth_finder(counter) == def_depth):
                end_line = counter
                break
                
        s = program.code.remove_space(Line)
        line = s.replace("(", " ( ").replace(")", " ) ")
        line = line.split(" ")
        
        Type = line[1]
        name = line[2]
        input_type = []
        input_name = []
        parameter_type = []
        parameter_name = []
        
        p_index = line.index(')')
        
        for i in range(4, p_index):
            if(i %2 == 0):
                input_type,input_type.append(line[i])
            else:
                input_name.append(line[i])
                
        
        for counter in range(start_line+1, end_line):
            print(counter, program.code.body[counter])
                
        
        
        
        return(def_depth, start_line, end_line, Type, name, input_type, input_name)
        
        
    def ha(program):
        Line = 0
        for line in program.code.body:
            if(program.def_confirm(Line)):
                print("yup")
            else:
                print("NO")
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
                    
                    header = "    class: ", class_name, "/ class parents: ", parents, " {"
                    footer = "    }"
                    print("    class: ", class_name, "/ class parents: ", parents, " {",sep='')
                    print("")
                    '''================
                    Functions Adn Body!
                    ================'''
                    print("    }")
            Line += 1
