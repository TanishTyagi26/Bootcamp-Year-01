#------------------TYPE INSPECTOR PROGRAM----------------------------
# type inspector that accepts any user input ,tries to detct if it's int,float ,str ,, displays type name ,shows all type properties
#handle comma-separated,, list of values show type for each .

def detect_type(value_str):
    try :
        int(value_str)
        return int,int(value_str)
    except ValueError :
        pass
    try :
        float(value_str)
        return float,float(value_str)
    except ValueError :
        pass
    return str,value_str

# main program 
user_input=input("enter a value : ")
detected , converted = detect_type(user_input)
print(f"Type:{ detected.__name__}")
print(f"Value :{converted}")
print(f"isinstance int ? {isinstance (converted , int)}")