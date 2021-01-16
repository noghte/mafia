import random
p = ['Abbas','Mehdi','Sanaz Haghani', 'Sanaz Sattar', 'Arash', 'Leila', 'Saed', 'Mona','Saba','Maryam','Elham']
r = ['Neogotiator', 'Terrorist', 'God Father', 'Karagah', 'Doctor', 'Tak Tirandaz', 'Zereh Poush', 'Ravanshenas','Khabarnegar','Shahrvand'] 

shahrvands_len = (len(p) - len(r))
r+= ['Shahrvand'] * shahrvands_len

print("sharvands:", shahrvands_len)
if len(p) == len(r):
    sel_p = random.sample(p, len(p))
    sel_r = random.sample(r, len(r))
    final = list(zip(sel_p, sel_r))
    print(final)
else:
    print('lists had different length')

print("Asking order: \r\n1. tak tariandaz  \r\n2. terrorist  \r\n3. karagah \r\n4. ravanshanas \r\n5. khabarnegar (if negotiated)")