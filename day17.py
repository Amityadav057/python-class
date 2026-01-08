# f = open('error.txt','r')
# a = 10
# f.write(r)
# f.close()
def handle_error(message,file="error.txt"):
    f = open(file,'a')
    f.write(message)
    f.close()
try:
    print(a)
except NameError as e:
    handle_error(str(e),'name.txt')
except TypeError as e:
    handle_error(str(e),'type.txt')

except:
    print("something went wrong")
    