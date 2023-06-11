import os

number=7

for i in range(40):
    try:
        os.system('python upworkOneRegister.py profile'+str(i%number)+'.json')
    except Exception as e:
        print(f'Error occurred during execution: {e}')
        continue
