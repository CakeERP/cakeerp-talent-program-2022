def inputAdapter(inp_type, inp_msg, err_msg):
    st_time = True
    while True:
        i = input(inp_msg)
        try:
            if (inp_type == bool):
                if (
                    i == "1" or
                    i.lower() == "true" or
                    i.lower() == "t" or
                    i.lower() == "v" or
                    i.lower() == "s" or
                    i.lower() == "y"
                ): return True

                if (
                    i == "0" or
                    i.lower() == "false" or
                    i.lower() == "f" or
                    i.lower() == "n"
                ): return False

                raise

            return inp_type(i)
        except:
            if not(st_time):
                print("\033[A                             \033[A")
            print("\033[A" + err_msg)

        st_time = False