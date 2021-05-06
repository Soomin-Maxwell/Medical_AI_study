def complicate_function(a) :
    a += 1000
    a *= 0.5 
    a = "string"
    a *= -.1

    return a 

if __name__ == "__main__" :
    a = 40 
    print(complicate_function(a))  