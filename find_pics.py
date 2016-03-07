import os
import glob
import shutil
import sys

# find current directory and prepare for
current_path = os.getcwd()
des_path = current_path + "\photos"

# if directory \photos doesn't  exist create one
if not os.path.exists(des_path):
    os.makedirs(des_path)

# counts the files found
counter = 0

# search for .jpg .gif .png files in the current directory and print them
for x in glob.glob("*.jpg"):
    print x
    counter += 1
for y in glob.glob("*.gif"):
    print y
    counter += 1
for z in glob.glob("*.png"):
    print z
    counter += 1

answer = ""

# take a prompt from the user if files found
if counter > 0:
    answer = raw_input("Found the above file(s). PRESS y to proceed n to finish...")

# if files found move them to the destination
if answer.upper() == "Y":
    for x in glob.glob("*.jpg"):
        try:
            shutil.move(x, des_path)
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except ValueError:
            print "Could not convert data to an integer."
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
    for y in glob.glob("*.gif"):
        try:
            shutil.move(y, des_path)
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except ValueError:
            print "Could not convert data to an integer."
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise
    for z in glob.glob("*.png"):
        try:
            shutil.move(z, des_path)
        except IOError as e:
            print "I/O error({0}): {1}".format(e.errno, e.strerror)
        except ValueError:
            print "Could not convert data to an integer."
        except:
            print "Unexpected error:", sys.exc_info()[0]
            raise

    # successfully moved files
    raw_input("SUCCESS! Press enter...")

# if no files found terminate the program
if counter == 0:
    raw_input("No files found.Press enter...")