#Here, we are adding "..." between words
mol=input("What's the meaning of life?")
#Default of .split() is spacing so we dont need to do shit there
mol=mol.split()
# we are using .join(mol) to join the mol which we split above
y= "...".join(mol)
print(y)
