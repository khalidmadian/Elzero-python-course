websites=[]

counter=5

while counter>0:
    in_website=input('Enter your website with https://').strip().lower()
    websites.append(f'https://{in_website}')
    counter-=1
    print(websites)
    print(f'you can add {counter} websites to the list')

print('full list of websites')
