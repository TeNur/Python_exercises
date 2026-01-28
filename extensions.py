def main():

    name = input("File name: ").strip().lower()
    dot = "."

    if dot not in name:
        print("application/octet-stream")

    else:
        cleaned = name.rsplit(".", 1)[1]

        print(type_checker(cleaned))

def type_checker(file):
   match file:
        case "gif" | "png":
            return "image/" + file
        case "jpg" | "jpeg":
            return "image/jpeg"
        case "pdf" | "zip":
            return "application/" + file
        case "txt":
            return "text/plain"
        case _:
            return "application/octet-stream"


main()