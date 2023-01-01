#-*- coding: utf-8 -*-
from time import sleep
from rpi_lcd import LCD
import barcode_scanner as scanner

import db_handler as db
import motor_handler as motor
lcd = LCD()
lcd.text ("WELCOME TO NEC", 1)
lcd.text ("Scan Your Card", 2)

while True:
   sleep(0.1)
   if db.checkdRecords(scanner.waitForBarCode()):
      lcd.text('Roll is in the database')
      count = db.getCount()
      print('Count is : ',count)
      lcd.text ("Availabe pad",count)
      if count >25:
         print('Run from one')
         motor.stepper1()
         db.setCount(count-1)
      
      elif count<=25:
         print('Run from two')
         motor.stepper2()
         db.setCount(count-1)


      lcd.text('Roll is in the database',1)

   else:
      print('Roll not in database')
      lcd.text('Roll is not in database',1)
