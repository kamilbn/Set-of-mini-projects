

def calc_expr():
    off=False
    print("Expression Calculator")
    while not off:

       expr=input("Type your expression (Type 'off' if you want exit): ").lower()
       if expr == "off":
           off = True
       else:

            try:
               result = eval(expr)
               print(f"{expr}={result}")
            except:
                print(f"Your enter wrong value. Try again." )




