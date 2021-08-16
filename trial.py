import os 

dicti = {'1-blackshirt' : 'https://www.myntra.com/shirts/marks--spencer/marks--spencer-men-navy-blue-regular-fit-solid-casual-shirt/8594849/buy',
        '1-stripshirt': 'https://www.myntra.com/shirts/marks--spencer/marks--spencer-men-pink--off-white-regular-fit-striped-casual-shirt/13510610/buy',
        '1-plainshirt' : 'https://www.myntra.com/shirts/marks--spencer/marks--spencer-men-pink--off-white-regular-fit-striped-casual-shirt/13510610/buy',
        '2-bluejacket' : 'https://www.myntra.com/jackets/perfkt-u/perfkt-u-men-navy-blue-solid-insulator-padded-jacket/12681772/buy',
        '2-blackjacket' : 'https://www.myntra.com/jackets/perfkt-u/perfkt-u-men-black-solid-insulator-padded-jacket/12681770/buy',
        '3-blazer1' : 'https://www.myntra.com/blazers/favoroski/favoroski-men-sea-green-solid-slim-fit-single-breasted-blazer/8983669/buy',
        '3-blazer2' : 'https://www.myntra.com/blazers/favoroski/favoroski-purple-slim-fit-single-breasted-formal-blazer/2090924/buy',
        '3-blazer3': 'https://www.myntra.com/blazers/favoroski/favoroski-blue-wool-slim-fit-single-breasted-formal-blazer/2379222/buy',
        '3-blazer4' : 'https://www.myntra.com/blazers/favoroski/favoroski-navy-wool-slim-fit-single-breasted-formal-blazer/2379229/buy',
        '3-blazer5' : 'https://www.myntra.com/blazers/favoroski/favoroski-red-slim-fit-woollen-single-breasted-formal-blazer/2090926/buy',
        '4-jeans1' : 'https://www.myntra.com/jeans/american-archer/american-archer-men-blue-skinny-fit-low-rise-clean-look-stretchable-jeans/11528616/buy',
        '4-jeans3' : 'https://www.myntra.com/jeans/american-archer/american-archer-men-blue-slim-fit-low-rise-low-distress-stretchable-jeans/12942758/buy',
       '4-jeans2' : 'https://www.myntra.com/jeans/american-archer/american-archer-men-blue-skinny-fit-low-rise-clean-look-stretchable-jeans/12942730/buy',
    }

for i in os.listdir(r'Y:\Pro1\Creatin-Pro1'):
    for j in os.listdir(os.path.join(r'Y:\Pro1\Creatin-Pro1', i)):
        f = open(os.path.join(r'Y:\Pro1\Creatin-Pro1', i, j, j+'-link.txt'), 'w+')
        f.writelines(dicti[j])
        f.close()
        
print('Done')