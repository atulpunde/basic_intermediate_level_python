from PIL import Image 

img = Image.open("C://Users//Lenovo//Desktop//Atharv1.jpg") 
img.show() 

print(img.mode)
print(img.size)
print(img.format)

# angle = -30
# r_img = img.rotate(angle)



# size = (1000,600)
# r_img = img.resize(size)
# print(r_img.show())

# from PIL import Image 

# size = (400, 140) 
# img = Image.open(r"C://Users//Lenovo//Desktop//signscan.jpg") 
# r_img = img.resize(size) 

# # resized_test.png => Destination_path 
# r_img.save("C://Users//Lenovo//Desktop//signscan2.png") 

# # Opening the new image 
# img = Image.open(r"C://Users//Lenovo//Desktop//signscan2.png") 
# print(img.size) 
