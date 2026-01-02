try:
    print(a)
except NameError as e:
    print(e)
    
except TypeError as e:
    print(e)

except:
    print("something went wrong")