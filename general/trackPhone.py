import phonenumbers
from phonenumbers import geocoder
number="+919082229626"
num_obj=phonenumbers.parse(number,"IN")
print(geocoder.description_for_number(num_obj,"en"))