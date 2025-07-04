
# task 01 == Розділіть змінну Alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну Alice_in_wonderland на друк

#task 01
Alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."')


#task 02
single_quotes = [char for char in Alice_in_wonderland if char == "'"]
print ("Знайдені символи одинарної лапки:")
print(single_quotes)
print(f"Кількість: {len(single_quotes)}")

#task 03
print(Alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436402
azov_sea = 37800
zagalna_ploshya = black_sea + azov_sea
print(zagalna_ploshya, "км²")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
vsyogo_tovariv = 375291
pershiy_ta_drygiy = 250449
drygiy_ta_tretyi = 222950
tretyi = vsyogo_tovariv - pershiy_ta_drygiy
pershyi = vsyogo_tovariv - drygiy_ta_tretyi
drygiy = vsyogo_tovariv - (tretyi + pershyi)
print ("pershyi", pershyi ,"tov.")
print ("drygiy", drygiy ,"tov.")
print("tretyi", tretyi ,"tov.")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
misyachnyi_platij = 1179
pivtora_roky = 18
vartist_kompa = misyachnyi_platij * pivtora_roky
print(vartist_kompa, "grn")


# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 890 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print("a)",a)
print("b)",b)
print("c)",c)
print("d)",d)
print("e)",e)
print("f)",f)

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
velyka_pizza = 4 * 274
serednya_pizza = 2 * 218
sik = 4 * 35
tort = 1 * 350
voda = 3 * 21
zamovlennya = velyka_pizza + serednya_pizza +sik + tort + voda
print(zamovlennya, "grn")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
vsyogo_foto = 232
odna_storynka = 8
vsyogo_storinok = vsyogo_foto / odna_storynka
print(vsyogo_storinok)

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distancia = 1600
rozhid_na_100km = 9
obem_baky = 48
neobhidno_benzyny_na_podoroj = distancia / rozhid_na_100km
kilkist_zapravok = neobhidno_benzyny_na_podoroj / obem_baky
print(kilkist_zapravok)
print(neobhidno_benzyny_na_podoroj, "litriv")