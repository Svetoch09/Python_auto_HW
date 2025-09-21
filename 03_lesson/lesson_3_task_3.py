from address import Address
from mailing import Mailing

to_address = Address("123 456", "NY", "White street", 3, 78)
from_address = Address("456 123", "London", "Black street", 8, 24)
cost = 48.56
track = "12fsdghjtkj6568hj"

my_mailing = Mailing(to_address, from_address, cost, track)

print(my_mailing)
