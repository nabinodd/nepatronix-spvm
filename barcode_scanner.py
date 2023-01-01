import keyboard

def utfToAscii(bar_code):
   new_arr = []
   bar_cod_enc = bytearray(bar_code,'utf-8')

   for c in bar_cod_enc:
      new_arr.append(c)

   new_arr[4] = 45
   del new_arr[5]
   del new_arr[5]
   read_arr = ''

   for c in new_arr:
      read_arr = read_arr + chr(c)

   return str(read_arr)


def waitForBarCode():
   print('[INFO]\tWaiting for Barcode')
   recorded = keyboard.record(until = 'enter')
   string = keyboard.get_typed_strings(recorded)
   bar_code = next(string)
   bar_code = utfToAscii(bar_code)
   return bar_code
