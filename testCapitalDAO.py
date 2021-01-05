from CapitalDAO import capitalDAO

#create
capital1 = {
    'id': 7,
    'name': 'Dublin',
    'country': 'Ireland',
    'population': 554000,
}

capital2 = {
    'id': 7,
    'name': 'London',
    'country': 'United Kingdom',
    'population': 8900000,
}

#create
returnValue = capitalDAO.create(capital1)
print("-----create done-----")

#getall
returnValue = capitalDAO.getAll()
print(returnValue)
print("-----getAll done-----")

#update
returnValue = capitalDAO.update(capital2)
print(returnValue)
print("update done-----")

#find by id
returnValue = capitalDAO.findById(capital2['id'])
print(returnValue)
print("findById done-----")

#delete
capitalDAO.delete(capital2['id'])
print("-----delete done-----")

#getall
returnValue = capitalDAO.getAll()
print(returnValue)
print("-----getAll done-----")