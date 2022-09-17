import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)  
        file = open(file_from, 'rb')
        dbx.files_upload(file.read(), file_to)

    

def main():
    access_token = 'sl.BPbLwwl5ccBaa773KGjdfWpnf57_5OwUAfgSVveCfLD9FeBQ2FsJ9U0GALJNgqRuwCiyFaZDPa4sWf0lhHjr_YLej2VzpLKfD4XlwI6odBI0510zTyqpRSt3KoRaLcrTh9CZd_8'
    transfer_data = TransferData(access_token)
    
    file_from = "C:/Users/Sreekanth Murugan/Documents/101/hello.txt"
    
    file_to = "/Projects/hello.txt"
    
    transfer_data.upload_file(file_from, file_to)
    print("Files has been moved")

main()