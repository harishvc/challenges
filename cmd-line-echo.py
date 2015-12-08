def Read():
    try:
        print("welcome to echo ... press ENTER to exit")
        while True:
            x = input()
            if (len(x) > 0):
                print(x)
            else:
                break   
    except Exception as e:
        print("error:", str(e))
    finally:
        print("shutting down echo")
    
    
Read()