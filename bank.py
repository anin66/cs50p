greeting = input("Greeting: ").strip().lower()
x=greeting.startswith("hello")
y=greeting.startswith("h")
if x :
   print("0 rupee")
elif y:
   print("20 rupee")
else :
   print("100 rupee")