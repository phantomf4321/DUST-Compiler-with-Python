class Read_code:
    def __init__(code, body):
        print("constructor is called!")
        code.body = body
        
    def __str__(code):
        return f"{code.body}"
    
    def get_line(code, line_no):
        return code.body[line_no]
    
    def remove_space(code, line_no):
        space_counter = 0
        index = 0
        new_str = code.body[line_no].lstrip()
        #print("Line ", line_no, " is: ", code.body[line_no])
        return new_str
        
    def line_counter(code):
        counter = 0
        for line in code.body:
            counter += 1
        return counter
    
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
                
