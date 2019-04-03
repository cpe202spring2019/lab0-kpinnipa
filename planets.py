def weight_on_planets():
   user = int(input("What do you weigh on earth? "))
   mars = user*0.38
   jupiter = user*2.34 
   print("\nOn Mars you would weigh %s pounds.\nOn Jupiter you would weigh %s pounds." %(mars,jupiter))
if __name__ == '__main__':
   weight_on_planets()
