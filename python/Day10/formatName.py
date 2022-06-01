

def format_name(fname, lname):
    if fname == "" or lname == "":
        return "Please Enter Valid Input!"
    formated_fname = fname.title()
    formated_lname = lname.title()

    return f"{formated_fname} {formated_lname}"

 
print(format_name(input("Enter your first name: "), input("Enter your last name: ")))