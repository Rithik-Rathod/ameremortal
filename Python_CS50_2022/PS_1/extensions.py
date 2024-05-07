def main():
    ext=input("Yo, send me some mediaaaa ")
    e=extension(ext)
    print(e)

def extension(x):
    x=x.lower().strip()
    x=x.split(".")

    match x[1]:
        case "gif":
            return "GIF"
        case "jpg"|"jpeg":
            return "JPEG"
        case "png":
            return "PNG"
        case "pdf":
            return "PDF"
        case "txt":
            return "TEXT"
        case "zip":
            return "ZIP"
        case _:
            return "application/octet-stream"

if __name__=="__main__":
    main()
    