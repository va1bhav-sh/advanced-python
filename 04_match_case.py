#match-case is a feature in Python (introduced in Python 3.10) used for pattern matching
def http_status(status):
    match status:
        case 200:
            return "Ok"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status"

            
print(http_status(500))