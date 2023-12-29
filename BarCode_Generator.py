import barcode
from barcode.writer import ImageWriter

# Generate a barcode
def generate_barcode(data, barcode_type='code39'):
    # Create a barcode object
    barcode_class = barcode.get_barcode_class(barcode_type)
    barcode_instance = barcode_class(data, writer=ImageWriter())
    
    # Save the barcode as an image
    filename = f"my_barcode_{barcode_type}"
    barcode_instance.save(filename)
    print(f"Barcode saved as '{filename}.png'")

# Usage
data_to_encode = "123456789"  # Your data here
generate_barcode(data_to_encode)