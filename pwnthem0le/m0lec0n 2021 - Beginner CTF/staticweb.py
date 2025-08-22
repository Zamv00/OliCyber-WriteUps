import requests

site = "http://staticwebfoundation.challs.olicyber.it/"

r = requests.get(site).headers
#/o1SfuSXpptIk1p8U0qISobkrYwXSILflr6ZxTsmF?p=banana

r1 = requests.get(f"{site}/o1SfuSXpptIk1p8U0qISobkrYwXSILflr6ZxTsmF?p=banana").text
print(r1)

#ptm{l00k_at_Th3_he4d3rs!}