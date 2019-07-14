##dictionaries

##provinces and capital cities and significant cities if significant is not capital

provinces = {
    'Mpumalanga': 'Nelspruit',
    'Limpopo': 'Polokwane',
    'Gauteng': ['Pretoria, Johannesburg'],
    'Kwa-Zulu Natal': ['Ulundi', 'Durban'],
    'North West': 'Mafikeng',
    'Eastern Cape': ['Bisho', 'Port Elizabeth'],
    'Northen Cape': 'Kimberly',
    'Free State': 'Bloemfontein',
    'Western Cape': 'Cape Town',
    'South Africa': ['Pretoria', 'Cape Town']
}


print('provinces with a significant city that is not the capital')
for province in provinces:
    if isinstance(provinces[province], list):
        print(province)
