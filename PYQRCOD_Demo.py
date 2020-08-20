import pyqrcode
name  = " parth Shukla\n"
email_ID = "parth.shukla@9ledgepro.com\n"
mobile_No = "9599587014"
LinkedIn = "https://www.linkedin.com/in/parth-shukla-09205239/\n"
GitHubLink = "https://github.com/ParthShuklaa\n"

myQRCode = pyqrcode.create( name + email_ID+mobile_No+LinkedIn+GitHubLink)
myQRCode.svg("myqrcode.svg")
print("Check your QR Code, it has been created inside your project")