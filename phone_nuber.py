import phonenumbers

from phonenumbers import carrier , geocoder , timezone

moblieno = input(" \n  Enter the Phnoe Number you want to search with country code: ")
moblieno = phonenumbers.parse(moblieno)

print(" \n  This Phone No. follows the Time/Zone of: ",timezone.time_zones_for_number(moblieno))

print(" \n  The ISP of this Phone Number is: " , carrier.name_for_number(moblieno,"en"))

print(" \n  The country where this phone is situated is: " , geocoder.description_for_number(moblieno,"en"))

print(" \n  This is a Valid PhoneNumber" , phonenumbers.is_valid_number(moblieno), "\n")

# print("Checking Possibility of Number : " , phonenumbers.is_possible_number(moblieno))