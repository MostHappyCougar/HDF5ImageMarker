from sys import exit
def iss_handler(issue_class, text, exit_code=0):
    print("#############################################################")
    print(issue_class+": " + text)
    print(f"EXECUTION IS INTERRUPTED with exit code {exit_code}")
    print("#############################################################")
    exit(exit_code)