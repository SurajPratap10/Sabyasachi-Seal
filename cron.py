import requests
import random
import yaml
import os

cronjobraw = "https://raw.githubusercontent.com/Sabyasachi-Seal/Sabyasachi-Seal/main/.github/workflows/Profile3D.yml"
cron = requests.get(cronjobraw)
croncontent = cron.text
croncontent = croncontent.split("\n")
croncontent[3] =   f'  - cron: "0 */{str(random.randint(1, 8))} * * *"'

yamlfile =  open('.github/workflows/Profile3D.yml', 'w')

yamlfile.write("\n".join(croncontent))

yamlfile.close()

print("Updated Cron Job")

# os.system('git add .')
# os.system('git commit -m "Cron Job Update"')
# os.system('git push')