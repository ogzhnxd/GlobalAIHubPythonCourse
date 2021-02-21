###############################################################
## Global AI Hub Introduction to Python Programming Course
## Final Project
## Recipe Maker
###############################################################
## Author: Oğuzhan GÜVERCİN
## Author Email: ogzhngvrcn00@gmail.com
###############################################################

# Importing needed module
import time


# A function to prettify strings
def prettifyStrings(string):
    # If sent variable isn't string turning it into string
    string = str(string)
    # Deleting special characters from string
    string = string.translate({ord(i): None for i in '{}[](),\''})
    # Returning prettified string
    return string.replace(" ", ", ").capitalize()


# A parent class for dishes
class Dishes:
    # Initializing needed parameters
    def __init__(self, liquidIngredients, solidIngredients, spices):
        self.liquidIngredients = liquidIngredients
        self.solidIngredients = solidIngredients
        self.spices = spices
        self.allIngredients = self.solidIngredients + self.liquidIngredients
        self.pan = []
        self.containers = {"1.Kase": [], "2.Kase": [], "3.Kase": []}

    # A method to add new ingredients to ingredient lists
    def addNewIngredient(self):
        # Infinite loop
        while True:
            # Asking user for ingredient
            ingredient = input("Hangi malzemeyi eklemek istersiniz ?")
            # Asking the form of ingredient (solid or liquid)
            ingredientForm = input("Bu malzeme sıvı mı yoksa katı bir malzeme mi ? (katı/sıvı)")
            # If ingredient is liquid
            if ingredientForm == "sıvı":
                # Add it to liquid ingredients list
                self.liquidIngredients.append(ingredient)
                # And return ingredient
                return ingredient
            # If ingredient is solid
            elif ingredientForm == "katı":
                # Add it to solid ingredients list
                self.solidIngredients.append(ingredient)
                # And return ingredient
                return ingredient
            # Else ask for an ingredient again
            else:
                print("Lütfen cevabınızı katı veya sıvı olarak veriniz!")
                continue

    # A method to wash solid ingredients
    def washing(self):
        print("{} yıkanıyor...".format(', '.join(self.solidIngredients)).capitalize())

    # I'm not including this part of the code cause it makes it insane long and
    # it is already a pretty long code on it's own
    # But i wanted to include it in comment form anyway
    # def measuring(self, ingredient):
    #
    #    if ingredient in self.solidIngredients:
    #        measure = input("Ne kadar kullanmak istersiniz ?")
    #        print("{} malzemesinden {} kadar ölçülüyor...".format(ingredient, measure))
    #
    #    elif ingredient in self.liquidIngredients:
    #        while True:
    #            try:
    #                measure = input("Ne kadar kullanmak istersiniz ? (Cevabınızı mililitre olacak şekilde giriniz.)")
    #                measure = int(measure.strip("ml"))
    #            except ValueError:
    #                print("Cevabınızı mililetre olacak şekilde giriniz (1000ml gibi)")
    #                continue
    #            break
    #
    #        print("{} malzemesinden {}ml kadar ölçülüyor...".format(ingredient, measure))

    # A static method to mix ingredients in the or in bowls
    @staticmethod
    def mixing(ingredients):
        # Mixing ingredients
        print("{} karıştırlıyor".format(prettifyStrings(ingredients)))

    # A method to peel ingredients
    def peeling(self, solidIngredient):
        # If ingredient is in solid ingredients
        if solidIngredient in self.solidIngredients:
            # Peel
            print("{} soyuluyor...".format(solidIngredient).capitalize())
        # Else
        else:
            # Add the forgotten ingredient and then peel
            print("{} malzemesini eklemediniz!".format(solidIngredient).capitalize())
            self.peeling(self.addNewIngredient())

    # A method to slice ingredients
    def slicing(self, solidIngredient):
        # If ingredient is in solid ingredients
        if solidIngredient in self.solidIngredients:
            # Slice
            print("{} doğranıyor...".format(solidIngredient).capitalize())
        # Else
        else:
            # Add the forgotten ingredient and then slice
            print("{} malzemesini eklemediniz!".format(solidIngredient).capitalize())
            self.slicing(self.addNewIngredient())

    # A method to dice ingredients
    def dicing(self, solidIngredient):
        # If ingredient is in solid ingredients
        if solidIngredient in self.solidIngredients:
            # Dice
            print("{} küp küp doğranıyor...".format(solidIngredient).capitalize())
        # Else
        else:
            # Add the forgotten ingredient and then dice
            print("{} malzemesini eklemediniz!".format(solidIngredient).capitalize())
            self.dicing(self.addNewIngredient())

    # A method to cook the ingredients that are in pan
    def cooking(self):
        print("{} pişiriliyor...".format(prettifyStrings(self.pan)).capitalize())

    # A method to season the dish
    def seasoning(self):
        print("Yemeğe {} ekleniyor...".format(self.spices).capitalize())

    # A method to add ingredients to pan
    def addIngredientsToPan(self, *args):
        check = True
        # Iterate over arguments
        for i in args:
            # If argument is in ingredients
            if i in self.allIngredients:
                # Continue to loop
                continue
            # Else
            else:
                # Add the unknown ingredient to ingredients list
                print("{} malzemesini eklemediniz!".format(i).capitalize())
                self.addNewIngredient()
                # Change chect to False
                check = False
                # And break
                break
        # If check is true
        if check:
            # Add ingredients to pan
            self.pan.append(args)
            print("{} tavaya  ekleniyor...".format(prettifyStrings(args)))
        # Else try again
        else:
            self.addIngredientsToPan(args)

    # A method to add ingredients to bowls
    def addIngredientsToBowls(self, *args):
        # If bowl 1 is empty
        if not self.containers["1.Kase"]:
            # Add arguments to bowl1
            print("{} ilk kaseye ekleniyor...".format(prettifyStrings(args)))
            self.containers["1.Kase"] = args
        # If bowl 2 is empty
        elif not self.containers["2.Kase"]:
            # Add arguments to bowl2
            print("İlk kase dolu,{} ikinci kaseye ekleniyor...".format(prettifyStrings(args)))
            self.containers["2.Kase"] = args
        # If bowl 3 is empty
        elif not self.containers["3.Kase"]:
            # Add arguments to bowl3
            print("ilk iki kase dolu,{} ikinci kaseye ekleniyor...".format(prettifyStrings(args)))
            self.containers["3.Kase"] = args
        # Else tell user to empty bowls
        else:
            print("Boş kasen yok önce kaselerini boşalt!")

    # A method to empty the contents of bowl to pan
    def emptyBowlToPan(self):
        # Infinite loop
        while True:
            # Ask user to choose a bowl
            kase = input("Hangi kaseyi tavaya aktarmak istiyorsunuz ? (1/2/3)")
            # If bowl 1 is chosen
            if kase == "1":
                # Empty the contents of bowl 1 to pan
                print("{} tavaya ekleniyor...".format(prettifyStrings(self.containers["1.Kase"])))
                self.pan = self.containers["1.Kase"]
                self.containers["1.Kase"] = []
                break
            # If bowl 2 is chosen
            elif kase == "1":
                # Empty the contents of bowl 2 to pan
                print("{} tavaya ekleniyor...".format(prettifyStrings(self.containers["2.Kase"])))
                self.pan = self.containers["2.Kase"]
                self.containers["2.Kase"] = []
                break
            # If bowl 3 is chosen
            elif kase == "1":
                # Empty the contents of bowl 3 to pan
                print("{} tavaya ekleniyor...".format(prettifyStrings(self.containers["3.Kase"])))
                self.pan = self.containers["3.Kase"]
                self.containers["3.Kase"] = []
                break
            # Else ask user for a bowl number again
            else:
                print("Sadece 3 adet kaseniz var lütfen 1,2 veya 3 numaralı kaseyi seçiniz!")
                continue

    # A static method to heating pan
    @staticmethod
    def heatPan():
        print("Tavanın altı açılıyor...")

    # A method to empty the contents of pan
    def emptyPan(self):
        # Infinite loop
        while True:
            # Ask for a bowl for dumping the ingredients
            bowl = input("Tavayı hangi kaseye aktarmak istiyorsunuz ? (1/2/3) ")
            # If bowl 1 is chosen
            if bowl == "1" and not self.containers["1.Kase"]:
                # Empty the contents of pan to bowl 1
                self.containers["1.Kase"] = self.pan
                self.pan = []
                break
            # If bowl 2 is chosen
            elif bowl == "2" and not self.containers["2.Kase"]:
                # Empty the contents of pan to bowl 2
                self.containers["2.Kase"] = self.pan
                self.pan = []
                break
            # If bowl 3 is chosen
            elif bowl == "3" and not self.containers["3.Kase"]:
                # Empty the contents of pan to bowl 3
                self.containers["3.Kase"] = self.pan
                self.pan = []
                break
            # Ask for a bowl number again
            else:
                print("Sadece 3 adet kaseniz var lütfen 1,2 veya 3 numaralı kaseyi seçiniz!")
                continue


# A child class to Dishes class
class karniYarik(Dishes):
    # Inheriting all parameters and methods from Dishes
    def __init__(self, liquidIngredients, solidIngredients, spices, name):
        super().__init__(liquidIngredients, solidIngredients, spices)
        # Adding a new "name" parameter
        self.name = name

    # A method to fry ingredients
    def frying(self, solidIngredient):
        # If ingredient is in the solid ingredients list
        if solidIngredient in self.solidIngredients:
            # Fry
            print("{} kızartılıyor...".format(solidIngredient).capitalize())
        # If ingredient is in the liquid ingredients list
        elif solidIngredient in self.liquidIngredients:
            # Inform user
            print("Bir sıvı malzemeyi kızartamazsınız!")
        # Else inform user, add the unknown ingredient and try again
        else:
            print("Bu malzemeyi eklemediniz!")
            self.addNewIngredient()
            self.frying(solidIngredient)

    # A method to scar eggplant
    def scarEggplant(self):
        if "patlıcan" in self.solidIngredients:
            print("Patlıcanlar yarılıyor...")
        else:
            print("Patlıcanlarını nasıl unuttun karnıyarık yapıyoruz! Neyse ben ekliyorum")
            self.addNewIngredient()

    # A method to fill eggplant with the fillings
    def dumpIngredientsToEggplant(self):
        ingredients = str(self.containers["1.Kase"])
        ingredients.replace("[", "")
        print("1. kasedeki pişmiş {} patlıcanın içine konuluyor...".format(prettifyStrings(self.containers["1.Kase"])))

    # A method to serv dish
    def service(self):
        print("Pişmesi için biraz bekleyiniz...")
        print("{} tabağa konuluyor...".format(self.name.capitalize()))

    # A static method to inform user that dish is ready
    @staticmethod
    def dishReady():
        print("Karnıyarığınız hazır afiyet olsun :)")

    # A static method put dish into oven
    @staticmethod
    def putItIntoOven():
        print("Karnıyarık fırına veriliyor...")


# A child class to dish 1
class pilav(karniYarik):
    # Inheriting all parameters and methods from dish 1
    def __init__(self, liquidIngredients, solidIngredients, spices, name):
        super().__init__(liquidIngredients, solidIngredients, spices, name)

    # A method to soak ingredients
    def soakIngredient(self, ingredient):
        # If ingredient is in solid ingredients list
        if ingredient in self.solidIngredients:
            # Soak in water
            print("{} ıslatılıyor...".format(ingredient).capitalize())
        # Else add the ingredient to list and try again
        else:
            print("{}i nasıl unuttun Neyse ben ekliyorum".format(ingredient).capitalize())
            self.soakIngredient(self.addNewIngredient())

    # A static method to inform user that dish is ready
    @staticmethod
    def dishReady():
        print("Pilavınız hazır afiyet olsun :)")


# A child class to dish 2
class patatesKizartmasi(pilav):
    # Inheriting all the parameters and methods from dish 2
    def __init__(self, liquidIngredients, solidIngredients, spices, name):
        super().__init__(liquidIngredients, solidIngredients, spices, name)

    def dishReady(self):
        print("{} tabağa konuluyor...".format(self.name.capitalize()))
        print("Patates kızartmanız hazır afiyet olsun :)")

    # A static method to inform user that dish is ready
    @staticmethod
    def straining(ingredient):
        print("{} süzülüyor...".format(ingredient).capitalize())

# Starting with a informing message
print("Bugün karnıyarık, pilav ve patates kızartması yapacağız. Vakit kaybetmeden başlayalım :).")
time.sleep(1)
# Cooking the dishes and waiting 1 second between every step
karniYarikYemegi = karniYarik(["ayçiçek yağı", "zeytinyağı"],
                              ["patlıcan", "kıyma", "kuru soğan", "sarımsak", "salça", "domates", "maydanoz", "biber"],
                              ["tuz", "karabiber", "pul biber"], "karnıyarık")
print("Önce karnıyarığı yapalım.")
time.sleep(1)
karniYarikYemegi.washing()
time.sleep(1)
karniYarikYemegi.addIngredientsToPan("zeytinyağı")
time.sleep(1)
karniYarikYemegi.heatPan()
time.sleep(1)
karniYarikYemegi.dicing("kuru soğan")
time.sleep(1)
karniYarikYemegi.dicing("domates")
time.sleep(1)
karniYarikYemegi.slicing("biber")
time.sleep(1)
karniYarikYemegi.slicing("sarımsak")
time.sleep(1)
karniYarikYemegi.addIngredientsToPan("kuru soğan", "domates", "biber", "sarımsak", "kıyma", "salça")
time.sleep(1)
karniYarikYemegi.mixing(karniYarikYemegi.pan)
time.sleep(1)
karniYarikYemegi.cooking()
time.sleep(1)
# In this step user has to input 1,2 or 3 or program will keep asking for it again and again
karniYarikYemegi.emptyPan()
# Showing contents of bowls to user
print("Kaseler ;")
print("1. Kase : ", end="")
print(prettifyStrings(karniYarikYemegi.containers["1.Kase"]))
print("2. Kase : ", end="")
print(prettifyStrings(karniYarikYemegi.containers["2.Kase"]))
print("3. Kase : ", end="")
print(prettifyStrings(karniYarikYemegi.containers["3.Kase"]))
time.sleep(1)
karniYarikYemegi.peeling("patlıcan")
time.sleep(1)
karniYarikYemegi.frying("patlıcan")
time.sleep(1)
karniYarikYemegi.addIngredientsToBowls("patlıcan")
# Showing contents of bowls to user
print("Kaseler ;")
print("1. Kase : ", end="")
print(prettifyStrings(karniYarikYemegi.containers["1.Kase"]))
print("2. Kase : ", end="")
print(prettifyStrings(karniYarikYemegi.containers["2.Kase"]))
print("3. Kase : ", end="")
print(prettifyStrings(karniYarikYemegi.containers["3.Kase"]))
time.sleep(1)
karniYarikYemegi.scarEggplant()
time.sleep(1)
karniYarikYemegi.dumpIngredientsToEggplant()
time.sleep(1)
karniYarikYemegi.putItIntoOven()
time.sleep(1)
karniYarikYemegi.service()
time.sleep(1)
karniYarikYemegi.dishReady()
time.sleep(1)
print("\n")
time.sleep(1)
# Cooking next dish
pilavYemegi = pilav(["su", "sıvı yağ"], ["pirinç", "tereyağı"], ["tuz"], "pilav")
print("Şimdi pilavı yapalım.")
time.sleep(1)
pilavYemegi.soakIngredient("pirinç")
time.sleep(1)
pilavYemegi.heatPan()
time.sleep(1)
pilavYemegi.addIngredientsToPan("pirinç", "tereyağı")
time.sleep(1)
pilavYemegi.mixing(pilavYemegi.pan)
time.sleep(1)
pilavYemegi.cooking()
time.sleep(1)
pilavYemegi.addIngredientsToPan("su")
time.sleep(1)
pilavYemegi.mixing(pilavYemegi.pan)
time.sleep(1)
pilavYemegi.cooking()
time.sleep(1)
pilavYemegi.service()
time.sleep(1)
pilavYemegi.dishReady()
time.sleep(1)
print("\n")
# Cooking the last dish
patatesKizartmasiYemegi = patatesKizartmasi(["sıvıyağ"], ["patates"], ["tuz"], "patates kızartması")
print("Son olarak patates kızartmasını hazırlayalım")
time.sleep(1)
patatesKizartmasiYemegi.slicing("patates")
time.sleep(1)
patatesKizartmasiYemegi.soakIngredient("patates")
time.sleep(1)
patatesKizartmasiYemegi.heatPan()
time.sleep(1)
patatesKizartmasiYemegi.addIngredientsToPan("sıvıyağ", "patates")
time.sleep(1)
patatesKizartmasiYemegi.cooking()
time.sleep(1)
patatesKizartmasiYemegi.straining("patates")
time.sleep(1)
patatesKizartmasiYemegi.dishReady()
time.sleep(1)
