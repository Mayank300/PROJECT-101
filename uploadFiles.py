import dropbox
import os

class TransferData(object):
    def __init__(self, acces_token):
        self.acces_token = acces_token

    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.acces_token)
        for root, dirs, files in os.walk(file_from):
            for file_name in files:
                local_path = os.path.join(root, file_name)
                relPath = os.path.relpath(local_path, file_from)
                os.path.join(file_to, relPath)
 
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode('overwrite'))
        


def main():
    acces_token = "sl.Av01tiybi9hTqGp10npmnwCCkR9cuDlhkksK55dzYCzvxgJ_zZujxoRk9bk9DaKj90N0mCIbUjkwFrGhs5Etd-0naEP29C6NTI7R_til1rd2Rw-UVtpQhokMKKCnPZT2byZCwz8"
    transferData = TransferData((acces_token))

    file_from = input("name of the file path : ")
    file_to = input("enter the full path of the file to upload to dropbox : ")

    transferData.upload_files(file_from, file_to)

    print("file uploaded successfully =)")


# if __name__ == "__main__":
main()
