# Writing Data into a file

import os.path
fn = input("File: ")

if os.path.isfile(fn):
	data = input("Enter data to write and press q to quit ")
	f = open(fn, "a")
	while data != 'q':      # Writes data until we type "q"
		f.write(data + "\n")
		data = input(":")
	f.close()
else:
	print(fn, "does not exists ")
