def allowed_file(filename):
    ALLOWED_EXTENSIONS = ['png', 'jpeg', 'jpg']
    extension = filename.split('.')[-1]
    return extension in ALLOWED_EXTENSIONS
