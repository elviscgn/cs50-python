filename = input("Filename: ")
output = "application/octet-stream"
if "gif" in filename.lower().strip():
    output = "image/gif"
elif "jp" in filename.lower().strip():
    output = "image/jpeg"
elif "png" in filename.lower().strip():
    output = "image/png"
elif "png" in filename.lower().strip():
    output = "image/png"
elif "pdf" in filename.lower().strip():
    output = "application/pdf"
elif "txt" in filename.lower().strip():
    output = "text/plain"
elif "zip" in filename.lower().strip():
    output = "application/zip"
print(output)