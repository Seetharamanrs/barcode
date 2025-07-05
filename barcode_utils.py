import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from IPython.display import Image, display
def barcode_gen(data:str):
    c='0123456789QWERTYUIOPASDFGHJKLZXCVBNM-. $/+%'
    for i in data:
        if i not in c:
            raise ValueError("Invalid Character for code 39. Use A-Z 0-9 and -.$/+% space ")
    b=barcode.get_barcode('code39')   
    b_i=b(data.upper(),writer=ImageWriter(),add_checksum=False)
    buffer = BytesIO()
    b_i.write(buffer)
    buffer.seek(0)
    return buffer