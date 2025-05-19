# ask the user for the name of a file
name = input("File name: ").strip().lower()
first, last = name.split(".")
# if the name ends with .png,.jpg,.gif,.jpeg print image/name
match (last):
    case ".png" | ".jpg" | ".gif" | ".jpeg" :
        print(f"image/ {last}")    
# if the name endswith .txt,.pdf,.zip print application/name 
    case ".pdf" | ".txt" | ".zip" :
        print(f"application/ {last}")
# otherwise print application/octet-stream
    case _: 
        print("application/octet-stream")
