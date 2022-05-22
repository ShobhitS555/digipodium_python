# # with open('example.py') as content:
# #     print(content.read())

# with open('myfile.txt','w') as content:
#     print(content.write("here is some text \n this should be in next line"))

with open ('example.py','a') as content:
    content.write("/nprint ('using file handling')")