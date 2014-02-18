# -*- coding: latin-1 -*-

#
#  IS-105 LAB4
#
#  lab4.py - kildekode som inneholder studentenes løsning.
#         
#
#
import sys
import os
import subprocess
import re
import psutil # Kan installeres med "pip2.7 install psutil"

# Skriv inn fullt navn på gruppemedlemene (erstatte '-' med navn slikt 'Kari Trå')
gruppe = {  'Student 1': 'Erik Mikalsen', \
			'Student 2': 'Oddvar Tengesdal', \
            'Student 3': 'Tore Andre Halhjem', \
}

# Oppgave 1
# 	Funksjonen lager en strukturert utskrift av resultater fra
#   kallet psutil.cpu_times(). 
#	Modulen psutil må være installert.
#
#   Utskriften skal være følgende (verdiene skal selvsagt være forskjellige):
#		user = 3088.16
#		nice = 0.99
#		system = 897.37
#		idle = 72353.81
#		iowait = 19.29
#		irq = 6.82
#		softirq = 3.07
#		steal = 0.00
#		guest = 0.00
#
#def psutils_use():
#	"""
#	Henter lister med systeminformasjon fra /proc og bearbeider disse
#	"""
	# Impleementer funksjonen her
def psutils_use():
    """
    Henter lister med systeminformasjon fra /proc og bearbeider disse
    """
# Impleementer funksjonen her
    cputider=psutil.cpu_times()	# Lagrer resultat i cputider variabelen
    etiketter=cputider._fields	# Henter ut etikettene: user, nice osv.
    verdier=tuple(cputider)	# Henter ut verdiene: 3088.16, 0.99 osv.
    altsammen=zip (etiketter, verdier)	# Slår de sammen i en liste

    for element in altsammen:
       
        print "{} = {}".format(element[0], element[1])
 #index 0 inneholder etikett, index 1 er selve dataene.	
psutils_use()


# Oppgave 2
#	Gitt følgende liste (inn-data):
# 	proglangs = [('Python', '1989', 'Guido van Rossum'), ('C', '1969', 'Dennis Ritchie'), ('Java/Oak', '1991', 'James Gosling'), ('C++', '1979', 'Bjarne Stroustrup'), ('Ruby', '1991', 'Yukihiro "Matz" Matsumoto'), ('Perl', '1987' , 'Larry Wall'), ('Go/golang', '2007', 'Robert Griesemer, Rob Pike, and Ken Thompson')]
#
#	skal funksjonen produsere følgende ut-data:
#
#		C ble startet 1969 av Dennis Ritchie.
#		C++ ble startet 1979 av Bjarne Stroustrup.
#		Perl ble startet 1987 av Larry Wall.
#		Python ble startet 1989 av Guido van Rossum.
#		Java/Oak ble startet 1991 av James Gosling.
#		Ruby ble startet 1991 av Yukihiro "Matz" Matsumoto.
#		Go/golang ble startet 2007 av Robert Griesemer, Rob Pike, and Ken Thompson.
#			
#def print_history(proglangs):
	# Implementer funksjonen her

#proglangs = [('Python', '1989', 'Guido van Rossum'), ('C', '1969', 'Dennis Ritchie'), ('Java/Oak', '1991', 'James Gosling'), ('C++', '1979', 'Bjarne Stroustrup'), ('Ruby', '1991', 'Yukihiro "Matz" Matsumoto'), ('Perl', '1987' , 'Larry Wall'), ('Go/golang', '2007', 'Robert Griesemer, Rob Pike, and Ken Thompson')]
#print_history(proglangs)


# Standardkall for evalueringen
print 5*"-" + " Studenter: " + 5*"-"
for s in gruppe.values():
	if s is not "-":
		print s





