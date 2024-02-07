

from company import Company
from dev import Dev
from freebie import Freebie


__all__ = [ 'Company', 'Dev', 'Freebie' ]

ibm = Company("IBM", 1980)
facebook = Company("Facebook", 2006)

rooj = Dev("Rooj")
isaiah = Dev("isaiah")

freebie1 = Freebie(rooj, ibm, "Hat", 5)
freebie2 = Freebie(isaiah, facebook, "Mug", 3)


# print(freebie1.print_details())

# facebook.give_freebie(rooj, "shirt", 10)
# print(rooj.freebies())

# rooj.give_away(isaiah, freebie1)

print(Company.oldest_company())
