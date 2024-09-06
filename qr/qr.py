import qrcode
#generate qr
my_port = qrcode.make("https://sites.google.com/view/yeshwantgn/home")
my_port.save("my_portfolio.png",scale=8)
