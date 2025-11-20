s=input("File name: ")
s=s.strip().lower()

def split_period(filename):
    if "." in filename:
        after=filename[filename.index(".")+1:]
        return after
    else:
        return "1"

def main():
    re=split_period(s)
    if (re=="1"):
        print("application/octet-stream")
    else:
        final(re)

def final(m):
    match m:
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf" | "txt.pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")


main()
