import qrcode
#generate qr
my_port = qrcode.make("Desktop/New folder/data_science_in_git/Python_datascience_cheatsheet.pdf")
my_port.save("my_portfolio.png",scale=8)
