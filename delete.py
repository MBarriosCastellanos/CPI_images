#%%
import os
import glob

#%%
files = glob.glob('*.*'); print('len files = %s'%len(files))
for j in ['.py', '.tex', 
  '.pdf'
  ]:
  files = [i for i in files if i[-len(j):]!=j]
  print('len files = %s without %s'%(len(files), j))

#%%
print('len files = %s to delete'%(len(files)))
for f in files:
  os.remove(f)

# %%
