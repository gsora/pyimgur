import pyimgur

testImage = open('./test.png', 'rb')
secret = "YOUR SECRET"
clientID = "YOUR CLIENT ID"

print("Go to {}, paste here your PIN and press enter.".format(pyimgur.craftAuthURL(clientID)))
PIN = input("PIN >> ")
acc, rec = pyimgur.imgurAuth(clientID, secret, PIN)
print("Access token: {}\nRefresh token: {}".format(acc, rec))
print("Uploading image...")
print(pyimgur.imgurUpload(acc, pyimgur.doB64Conv(testImage)))
