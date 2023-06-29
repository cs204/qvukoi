x = input("File name: ")
words = x.split(".")
last = words[1]

match last:
    case "gif" | "jpeg" | "png":
        print("image/" + last)
    case "pdf" | "zip":
        print("application/" + last)
    case "txt":
        print("text/plain")
    case "jpg":
        print("image/jpeg")
    case _:
        print("application/octet-stream")