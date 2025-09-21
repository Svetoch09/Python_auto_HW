from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 17 Pro", "+7999 999 99 99"),
    Smartphone("Google", "Pixel 10 Pro", "+7988 888 88 88"),
    Smartphone("Sony", "X Peria 10", "+7977 777 77 77"),
    Smartphone("Samsung", "Galaxy 25", "+7966 666 66 66"),
    Smartphone("Xiaomi", "Note", "+7955 555 55 55")
]

for phone in catalog:
    print(f"{phone.phone_brand} - {phone.phone_model}. {phone.mobile_number}")
