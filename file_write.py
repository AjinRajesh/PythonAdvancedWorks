f=open('k.txt','w')#if exists, it will erase the file contents and return its reference to f

#else it will create a new empty file and return its reference to f

# f.write("Hello\n")
# f.write("Welcome to python\n")# to write in file
# f.write('''\nMuhammad Kutty Panaparambil Ismail (born 7 September 1951),
# known professionally as Mammootty, is an Indian actor
# and film producer who works predominantly in Malayalam-language films.
# With a career spanning over five decades, he has appeared in over 400 films,
# predominantly in lead roles, across Malayalam, Tamil, Telugu, Kannada, Hindi,
# and English languages. He is the recipient of several accolades, including four
# National Film Awards, eleven Kerala State Film Awards, eleven Kerala Film
# Critics Awards and fifteen Filmfare Awards South. He received the
# Padma Bhushan, the third-highest civilian award, in 2026 for his
# contributions to cinema, and earlier the Padma Shri, the fourth-highest
# civilian award, from the Government of India in 1998. ''')

#writelines(list)
f.writelines(['hello\n','world\n','hi\n','python\n','ready\n','to\n','study\n'])
f.close()#always close after file operations