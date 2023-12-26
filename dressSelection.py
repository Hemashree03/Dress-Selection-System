'''
customer name
customer gender
customer height
customer size
customer color
customer fav color
customer dress model preference
customer age range
customer price range
'''


class customer:
    def __init__(self, cus_name, cus_age, cus_gender, cus_size, cus_color, cus_favclr, cus_priceRange):
        self.cus_name = cus_name
        self.cus_age = cus_age
        self.cus_gender = cus_gender
#        self.cus_height = cus_height
        self.cus_size = cus_size
        self.cus_color = cus_color
        self.cus_favclr = cus_favclr
        self.cus_priceRange = cus_priceRange

    def __str__(self):
        return "Name: " + str(self.cus_name) + "\nAge: " + str(self.cus_age) + "\nGender: " + str(self.cus_gender) + "\nSize: " + str(self.cus_size) + "\nColor: " + str(self.cus_color) + "\nFavorite color: " + str(self.cus_favclr) + "\nPrice Range: " + str(self.cus_priceRange)+"\n"


'''
class Customer_Color_Selection:
    def skinny(self,):
        print("Select the color:")
        skinny_selection = ["1.deep red", "2.olive green", "3.mustard yellow", "4.blue", "5.purple",
                            "6.cool pastels", "7.royal blue", "8.baby blue", "9.soft pink", "10.mint green", "11.lilac"]
        print(*skinny_selection)
        selection = int(input("Select the dress color with number: "))
        selection = selection-1
        print("selected color:", skinny_selection[selection])

    def dark(self):
        print("Select the color: ")
        dark_selection = [
            "1.Baby pink", "2.power blue", "3.navy purple", "4.emerald green", "5.deep purple", "6.ruby red", " 7.amethyst purple"]
        print(*dark_selection)
        selection = int(input("Select the dress color with number: "))
        selection = selection-1
        print("Selected color:", dark_selection[0])

    def white(self):
        print("Select the color: ")
        white_selection = [
            "1.Lavender", " 2.fiery red:", "3.vibrant orange", "4.electric blue", "5.sapphire blue", "6.soft grey", "7.taupe", "8.pale red"]
        print(*white_selection)
        selection = int(input("Select the dress color with number: "))
        selection = selection-1
        print("Selected color:", white_selection[selection])
'''


class Dress_model:
    def model_Selection(self):

        pass


class report:
    pass


def price_range(priceRange):
    if priceRange == "1":
        return "10000-5000"
    elif priceRange == "2":
        return "5000=3000"
    elif priceRange == "3":
        return "3000-1000"
    elif priceRange == "4":
        return "1000-500"
    elif priceRange == "5":
        return "500-200"
    else:
        return "None"


def crt_size(size):
    if int(size) % 2 != 0:
        return str(int(size)+1)


name = input("Enter your name: ")
age = input("Enter your age: ")
gender = input("Enter your gender: ")
# height = input("Enter your height: ")
size = input("Select your size: 24 26 28 30 32 34 36 38 40 42 44 46 48 \nSize:")
color_Type = int(
    input("Enter your color in number: \n1.Skinny 2.dark  3.White\nnumber:"))
favcolor = input("Enter your Favorite Color: ")
priceRange = input(
    "Select price range:\n1.10000-5000 2.5000-3000 3.3000-1000 4.1000-500 5.500-200\n")

priceRange = price_range(priceRange)
size = crt_size(size)
obj = customer(name, age, gender, size,
               color_Type, favcolor, priceRange)
print()
gender_model = []
print(obj)
if 'f' in gender[0]:
    gender = "f_gender"
    gender_model = ["1.Chudidhar", "2.Kurthi",
                    "3.Tops", "4.Shirts", "5.T-Shirts", "6.Salwar", "7.lehanga"]
elif "m" in gender[0]:
    gender = "m_gender"
    gender_model = ["1.Kurtha", "2.T-Shirts", "3.Formal-Shirt",
                    "4.Casual-Shirts", "5.Hoodie", "6.Jurgins"]
color = ""
if color_Type == 1:
    color = "Skinny"
elif color_Type == 2:
    color = "Dark"
elif color_Type == 3:
    color = "White"
color_lst = []
print("Select the color: ")
dress_color_model_dict = {"white": [
    "1.Lavender", " 2.fiery red:", "3.vibrant orange", "4.electric blue", "5.sapphire blue", "6.soft grey", "7.taupe", "8.pale red"], "Dark": [
    "1.Baby pink", "2.power blue", "3.navy purple", "4.emerald green", "5.deep purple", "6.ruby red", " 7.amethyst purple"], "skinny_selection": ["1.deep red", "2.olive green", "3.mustard yellow", "4.blue", "5.purple",
                                                                                                                                                  "6.cool pastels", "7.royal blue", "8.baby blue", "9.soft pink", "10.mint green", "11.lilac"]}
for i, j in dress_color_model_dict.items():
    if color == i:
        color_lst = j
        print(*j)
selection = int(input("Select the color with number here mentioned:"))
print()
print("Selected color: ", color_lst[selection-1])
print(*gender_model)
model_selection = int(input("select the model with the given number:"))
print()
print(gender_model[model_selection-1])
