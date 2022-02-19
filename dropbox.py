import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,"rb")
        dbx.files_upload(f.read(),file_to)
    
def main():
    access_token="sl.BCUzfcZEovtUmOgIu4ohJsk90MCMEn3gx6hO2imJkL8EOEUDg7h8Yl9o6wMtyR4Jt-f7P5lhtZkEm1VsIoE0Wq7CDalG0ud7rT3YWvRLc2Mt3_iIBYDJVyedXitBpoT2eaD_XvQ"
    transferData=TransferData(access_token)

    file_from=input("Enter the file path to transfer: ")
    file_to=input("Enter the full path to upload to dropbox: ")

    transferData.upload_file(file_from,file_to)
    print("File has been moved!")

main()