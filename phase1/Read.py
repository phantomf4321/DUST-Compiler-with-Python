class Read_code:
    def __init__(code, body):
        #print("constructor is called!")
        code.body = body 
    def __str__(code):
        return f"{code.body}"
    def get_line(code, line_no):
        return code.body[line_no]
    #Removes spaces at the beginning of strings:
    def remove_space(code, line_no):
        space_counter = 0
        index = 0
        new_str = code.body[line_no].lstrip()
        #print("Line ", line_no, " is: ", code.body[line_no])
        return new_str
    #numer of lines in code:
    def line_counter(code):
        counter = 0
        for line in code.body:
            counter += 1
        return counter
    #The depth is determined according to the condition of the brackets:
    def depth_finder(code, line_no):
        space_counter = 0
        index = 0
        #print("Line ", line_no, " is: ", code.body[line_no])
        for survey in code.body[line_no]:
            #print(code.body[line_no][index])
            if(code.body[line_no][index] == " "):
                space_counter += 1
                index += 1
            else:
                return space_counter/4
    #In each part of the code, it is determined in which line we reach the bracket:
    def next_braket(code, line_no): 
        current_line = line_no
        last_line = code.line_counter()
        open_braket_counter = 0
        for counter in range(current_line+1, last_line):
            if '{' in code.body[counter]:
                open_braket_counter += 1
            if '}' in code.body[counter]:
                if(open_braket_counter == 0):
                    return counter
                else:
                    open_braket_counter = open_braket_counter-1 
    #It puts the imports in an array and returns:        
    def find_imports(code):
        Line = 0
        imports = []
        for line in code.body:
            if(code.depth_finder(Line) == 0):
                s = code.remove_space(Line)
                if 'import' in s:
                    index = s.find('import')
                    s = code.body[Line][7:]
                    s = s.strip('\n')
                    imports.append(s)
                Line += 1       
        return(imports)
    #is field?
    def field_confirm(code, line_no):
        keywords = ['int', 'bool', 'float', 'string', 'double']
        s = code.body[line_no]
        s = code.remove_space(line_no)
        s = s.split(" ")
        confirm = any(word in keywords for word in s)
        if(confirm):#is there char?
            if "=" not in s:#There is no assignment command
                if "def" not in s:#it is not function
                    return True
        else:
            if(s[0][0].isupper()):#start with capital letter
                if "=" not in s:
                    if "def" not in s:
                        return True
            else:
                return False    
    #Creates two arrays of type and name. returns it:        
    def get_field(code, line_no):
        s = code.body[line_no]
        s = code.remove_space(line_no).strip('\n').split(" ")
        field_type = s[0]
        field_name = s[1]
        if "[" in field_type:
            open_parantes_index = field_type.index("[")
            close_parantes_index = field_type.index("]")
            field_type = field_type[:open_parantes_index] + field_type[close_parantes_index+1:]
        return(field_type, field_name)     
    #is function?
    def def_confirm(code, line_no):
        s = code.body[line_no]
        if 'def' in s:
            return True
        else:
            return False
    #is class?   
    def class_confirm(code, line_no):
        s = code.body[line_no]
        if 'class' in s:
            return True
        else:
            return False
    def extract_def(code, line_no, class_name):
        def_depth = code.depth_finder(line_no)#find depth
        start_line = line_no#initail line of function
        end_line = code.next_braket(line_no)#final line of function
        #The initial spaces of the string are removed for better calculations.      
        s = code.remove_space(line_no)#a space is created between the parentheses so that they are recognized as an independent element in the list
        line = s.replace("(", " ( ").replace(")", " ) ")#elements separated by space become independent Example: eat(Food food, int c) -> eat ( Food food, int c )
        line = line.split(" ")
        if(line[1] == class_name):
            Type = "constructor"
            name = line[1]
            input_type = []
            input_name = []
            p_index = line.index(')')
            for i in range(3, p_index):
                if(i %2 == 0):
                    input_name.append(line[i])
                else:
                    input_type.append(line[i])          
        else:
            Type = line[1]
            name = line[2]
            input_type = []
            input_name = []
            p_index = line.index(')')
            for i in range(4, p_index):
                if(i %2 == 0):
                    input_type.append(line[i])
                else:
                    input_name.append(line[i])
        field_type = []
        field_name = []
        for counter in range(start_line+1, end_line):      
            if(code.field_confirm(counter)):
                field = code.get_field(counter)
                field_type.append(field[0])
                field_name.append(field[1])
        return(def_depth, start_line, end_line, Type, name, input_type, input_name, field_type, field_name)    
    def extract_global_def(code, line_no, class_name):
        print(class_name)
        def_depth = code.depth_finder(line_no)#find depth
        start_line = line_no#initail line of function
        end_line = code.next_braket(line_no)#final line of function
        #The initial spaces of the string are removed for better calculations.      
        s = code.remove_space(line_no)#a space is created between the parentheses so that they are recognized as an independent element in the list
        line = s.replace("(", " ( ").replace(")", " ) ")#elements separated by space become independent Example: eat(Food food, int c) -> eat ( Food food, int c )
        line = line.split(" ")
        Type = line[1]
        name = line[2]
        input_type = []
        input_name = []
        p_index = line.index(')')
        for i in range(4, p_index):
            if(i %2 == 0):
                input_type.append(line[i])
            else:
                input_name.append(line[i])
                    
        field_type = []
        field_name = []
        for counter in range(start_line+1, end_line):      
            if(code.field_confirm(counter)):
                field = code.get_field(counter)
                field_type.append(field[0])
                field_name.append(field[1])
            
        return(def_depth, start_line, end_line, Type, name, input_type, input_name, field_type, field_name)
    
    
    
    def extract_calss(code, line_no):
        def_depth = code.depth_finder(line_no)#find depth
        start_line = line_no#initail line of function
        end_line = code.next_braket(line_no)#final line of function
        
        s = code.remove_space(line_no)#a space is created between the parentheses so that they are recognized as an independent element in the list
        line = s.replace("(", " ( ").replace(")", " ) ")#elements separated by space become independent Example: eat(Food food, int c) -> eat ( Food food, int c )
        line = line.split(" ")
        
        name = line[1]
        parents =[]
        fields = []
        functions = []
        open_arantes_index = line.index("(")
        close_arantes_index = line.index(")")
        
        for counter in range(open_arantes_index+1, close_arantes_index):
            parents.append(line[counter])
            
        for counter in range(start_line+1, end_line):  
            if(code.field_confirm(counter)):
                fields.append(code.get_field(counter))
                
            if(code.def_confirm(counter)):
                functions.append(code.extract_def(counter, name))
                
        return(def_depth, start_line, end_line, name, parents, fields, functions)
