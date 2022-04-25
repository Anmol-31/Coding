'''
1. close() open file ko close krta hai

2. it has no effect if file is already closed

3. closed file cannot be read or written anymore.

4.* koi bhi file tumko koi bhi operation krna hai lekin vo file already close hai tho, (value error) raise krega.

5.* python automatically closes a file when the reference obj. of file is resigned to another file

6. input output ke process ke time pe data jo hai vo buffer(this means data jo hai vo temp. location pr hold hota hai write krne se phle.) hota hai.
   python doesnt flush the buffer(write data to a file) jab tak ki vo sure ni hai ki you have done writing.python ko sure krane ka tarika hota hai file ko
   close karana.
   if uh dont close the file data wont make it to target file.
   but interesting thing about python is python automatically closes a file when the reference obj.of file is resigned to another file.

7. return value of close method is None.
'''
