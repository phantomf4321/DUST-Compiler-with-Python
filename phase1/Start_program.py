from Read import Read_code
import re


class program_start:
    
    def __init__(program, code):
        print("program start{")
        program.code = Read_code(code)
        program.numberOfLines = program.code.line_counter()
        
    def __str__(program):
        return f"{program.code.body}"
            
            
    def expand_class(program):
        import_counter = 0
        imports = program.code.find_imports()
        for Line in imports:
            print("    import class: ", imports[imports.index(Line)], sep='')
            
        #initial part of class:   
        for Line_counter in range(0, program.numberOfLines):
            #is it a class?
            if(program.code.class_confirm(Line_counter)):
                #extactin class:
                classes = program.code.extract_calss(Line_counter)
                
                #print name and parents:
                name = classes[3]
                parents = classes[4]
                print("    class: ", name, "/ class parents:", ' '.join(parents), "{", sep='')
                print("")#endline \n...
                
                #call fields of class:
                fields = classes[5]
                #print fields:
                for Line in fields:
                    print("        field: ", fields[fields.index(Line)][1], "/ type= ", fields[fields.index(Line)][0], sep='')
                    
                print() 
                #get all functions of class:
                functions = classes[6]
                for Line in functions:
                    
                    if(functions[functions.index(Line)][3] == 'constructor'):
                        print("        class constructor: ", functions[functions.index(Line)][4], "{", sep='')
                    else:
                        if(functions[functions.index(Line)][3] == 'void'):
                            print("        class method: ", functions[functions.index(Line)][4], "{", sep='')
                        else:
                            print("        class method: ", functions[functions.index(Line)][4],"/ return type: ", functions[functions.index(Line)][3], "{", sep='')
                        
                    
                    #call input parameters:
                    parameter_type = functions[functions.index(Line)][5]
                    parameter_name = functions[functions.index(Line)][6]
                    #checking empty fields:
                    if parameter_type[0] != '':
                        print("            parameter list: [", end='')
                        for INDEX in parameter_type:
                            counter = parameter_type.index(INDEX)
                            print( parameter_type[counter], " ", parameter_name[counter], sep='', end='')
                        print("]")
                     
                    #call fields of function:
                    def_fields_type = functions[functions.index(Line)][7]
                    def_fields_name = functions[functions.index(Line)][8]
                    #checking empty fields:
                    if def_fields_type:
                        for Line in def_fields_type:
                            counter = def_fields_type.index(Line)
                            print("            field: ", def_fields_name[counter], "/ type= ", def_fields_type[counter], sep='')
                            
                    print("        }")
                print("    }")
        print("}")
        
#Open the case test file        
f = open("testcase/test.txt", "r")
text = f.readlines()

#construct an object
c1 = program_start(text)

#starting program:
c1.expand_class()
