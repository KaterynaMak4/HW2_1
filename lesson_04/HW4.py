adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace ("\n", " ")
print (adwentures_of_tom_sawer)


# task 02 ==
""" Замініть .... на пробіл
"""

adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")
print (adwentures_of_tom_sawer)


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
adwentures_of_tom_sawer = " ".join(adwentures_of_tom_sawer.split())
print(adwentures_of_tom_sawer)


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_h = adwentures_of_tom_sawer.count("h")
print(f'Літера "h" зустрічається {count_h} разів.')


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
words = adwentures_of_tom_sawer.split()
capital_words = [w for w in words if w[0].isupper()]
print(f'Кількість слів, що починаються з великої літери: {len(capital_words)}')

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
first_index = adwentures_of_tom_sawer.find("Tom")
second_index = adwentures_of_tom_sawer.find("Tom", first_index + 1)
print(f'Слово "Tom" вдруге зустрічається на позиції {second_index}')

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_no_end_dot = adwentures_of_tom_sawer.strip(".")
adwentures_of_tom_sawer_sentences = adwentures_no_end_dot.split(".")
adwentures_of_tom_sawer_sentences = [s.strip() for s in adwentures_of_tom_sawer_sentences if s.strip()]
print(adwentures_of_tom_sawer)

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
fourth_sentence = adwentures_of_tom_sawer_sentences[3].strip().lower()
print(f"Четверте речення:\n{fourth_sentence}")

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
starts_with_by_the_time = any(s.strip().startswith("By the time") for s in adwentures_of_tom_sawer_sentences)
print(f'Чи є речення, що починається з "By the time"? {starts_with_by_the_time}')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""

last_sentence = adwentures_of_tom_sawer_sentences[-1].strip()
last_sentence_words = last_sentence.split()
count_words_last = len(last_sentence_words)
print(f'Кількість слів у останньому реченні: {count_words_last}')