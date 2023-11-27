

#%%

try:
    with open("sometext.txt") as file:
        for line in file:
            print(line)
except:
    print('the file doesn\'t exist')



# %%
