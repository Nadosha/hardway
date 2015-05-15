# coding: utf-8

# Это упражнение для того чтоб вспомнить и использовать все что 
# я выучил до этого. 

# Это примитивная програма для печати товарного чека 
# в отдельный текстовый файл

from sys import argv

script, out_file = argv

print "=" * 11 + script + "=" * 11 
print "-" * 30 + "\n" "\tЭкспресс касса\n" + "-" * 30

print """
Добрый день! Как вас зовут?
"""
user_name = raw_input("> ")

print "Очень приятно %s" % user_name
print "Сделайте ваш заказ: "

name = raw_input("Именование > ")
price = 12
print  "-" * 30 + "\n" + user_name + " вы заказали " + name + ", по \nцене %d грн за штуку, хороший выбор!" % price
print  "Какое количество?"
count = int(raw_input("> "))

print "Спасибо за заказ"
print "Печать чека ..."
 
def to_check(name, count, price):
	check = open(out_file, "w")
	price = price * count
	check.write("-" * 30 + "\n" + "\tЭкспресс касса\n" + "-" * 30 + "\n")
	check.write(("Товар: %s" % name) + (" (x%d)" % count))
	check.write("\n\tЦЕНА: %d грн." % price)
	check.write("\n" + "-" * 30 + "\n" + user_name + "\tСпасибо за покупку\n" + "-" * 30 + "\n")

choice = to_check(name, count, price) 

check = open(out_file)
print check.read()