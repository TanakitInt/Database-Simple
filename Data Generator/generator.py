#Data Generator
#Last Updated: 28/04/2018
#Coded by: TIVOLI
#KMITL

#Current code state: Customer Data Generator

import random

def main():
#Name lists for customers
    malename = ['Adirake','Akkarat','Chaowalit','Chayond','Chuan','Jettrin','Kiettisuk','Kittikorn','Krit','Ned','Niwat','Nontawat','Pairote','Paradorn','Petch','Pongrit','Pracha','Prakorb','Pramod','Prasopchai','Sakchai','Sarawut','Songpole','Sunya','Surat','Suttipong','Thongchai','Tuksin','Udom','Vit','Winai','Worrawut']
    femalename = ['Amporn','Areya','Budsaba','Chompoo','Chompunut','Duangrat','Intira','Jutharat','Korrakoj','Krittiga','Nattaporn','Nuntida','Orapan','Ornanong','Patsaporn','Pim','Porntip','Pradtana','Premwadee','Preyanutch','Promporn','Sangrawee','Sinee','Sirirat','Sunisa','Suttida','Suwattanee','Tidarat','Utumporn','Vipada','Yada']

#Name list for staffs
#    staff = ['Abhisit','Adisak','Akara','Alisara','Amorn','Amornrat','Anan','Anantachai','Anat','Anchalee','Anchaleephorn','Anucha','Apasara','Aphichat','Aphichat','Aphirak','Aphisak','Apinya','Aree','Ariphong','Arong','Arthit','Arunsri','Asara','Asda','Athasit','Banthita','Banyat','Boonsri','Bunrat','Bunyiam','Bunyong','Busarakham','Busawan','Chaiyanan','Chaiyaporn','Chakrii','Chalerm','Chaluay','Chana','Chanchai','Chanin','Chaniporn','Chanthasiri','Chaow','Chatchai','Chati','Chatuphon','Chid','Chomkate','Choom','Chuan','Chunphat','Chuwit','Danai','Daeng','Danupol','Duangjai','Duangkamol','Duanphen','Dusit','Ekamai','Ekaphong','Fungfaa','Gaan-daa','Gaewgaow','Gamon','Ganokpon;','Grasin','Hathai','Janthana','Jaruwan','Jintara','Jinthana','Juaa','Kanchana','Kasem','Khajee','Khanittha','Khlang','Khwanchit','Klaharn','Krist','Kumchok','Kunchanita','Kunlapan','Kwanchai','Kwanjai','Malee','Mali','Manee','Manee','Manit','Mano','Manoo','Manu','Marnit','Maruai','Mongkhon','Montri','Mukda','Naak','Naiyana','Nak','Naowarat','Napasorn','Naree','Narinsak','Narisa','Narongsak','Naruemol','Nattasit','Nawawan','Nee','Niew','Niracha','Nittaya','Nongluck','Nongnut','Nopadol','Nopakhoon','Nopparat','Nuttha','Nuttima','Pairat','Paithoon','Pakorn','Panchai','Panit','Panit','Pannee','Panom','Panthep','Panupat','Parichat','Parinya','Pasura','Patcharabhorn','Pathi','Pathom','Patipaan','Pattana','Pavena','Pensukporn','Perati','Perm','Phadet','Phaibun','Phaisak','Phaisan','Phanit','Phayon','Phichit','Phichit','Phimchai','Phinit','Phiphop','Phiriya','Phirom','Phondet','Phongphen','Phonphan','Phornrampha','Phuchong','Phumin','Phumphat','Phunsak','Pikun','Pimwasee','Pirawan','Piti','Piti','Piyabut','Piyakom','Piyawan','Pong','Pornchai','Pracha','Pradit','Pramon','Pramuk','Pranee','Praphan','Praphat','Prasan','Prasert','Prasit','Prasong','Prathana','Prathip','Prathum','Pratya','Prawet','Prawet','Prawit','Prawit','Preechaa','Preeda','Prem','Punyaa','Ram','Rangrong','Rinrada','Rong','Rudee','Rune','Runerudee','Rungsit','Rut','Ruthai','Saengdow','Saiphin','Saisamorn','Sakada','Sakon','Sakthip','Sakun','Saliltorn','Samak','Samat','Samorn','[Thai','Sanan','Sangwaan','Sangwal','Sanit','Santi','Sarita','Sasithorn','Sathit','Sathittayang','Sawang','Sawat','Sawit','Seri','Setiawan','Setiyang','Singh','Siri','Sirichok','Sirikit','Sirini','Siriphan','Siriphon','Siriphong','Siriporn','Sirirak','Sirirat','Siriwan','Sisak','Sisak','Sitthi','Sobhak','Sombat','Somboon','Sombun','Somchai','Somchok','Somjai','Somjit','Somkhit','Somkhuan','Somlaksa','Sommai','Somphian','Somphop','Sompong','Somporn','Somrat','Somsak','Somsong','Somsri','Somyot','Sonthi','Soontharee','Suchada','Suchadacha','Suchai','Suchart','Suchinda','Suda','Sugunya','Suhat','Sujit','Sumate','Sunai','Sunee','Suni','Supa','Supachai','Supaporn','Supawit','Suphan','Suphap','Suphawut','Supicha','Supit','Suppaphon','Supparat','Suprapha','Surat','Suree','Suriya','Suriya','Sutham','Suthep','Sutthiphon','Sutthiphong','Suwan','Suwicha','Suwit','Tanet','Tanuphon','Teerasak','Thaksin','Thanakorn','Thanaporn','Thanat','Thanatcha','Thawichat','Thawin','Thawip','Thawisak','Thawiwong','Thiraphat','Thitawan','Thitiporn','Thongchai','Tussanee','Ubol','Ubonwan','Udom','Ukit','Ukrit','Unyanee','Veera','Viroj','Vorapat','Wanee','Wanlapa','Wanlop','Wann','Wanna','Wanpol','Waraporn','Watcharaporn','Wattana','Wichai','Wichan','Wichian','Wichit','Wilat','Winai','Winyut','Wipa','Wipaporn','Wira','Wirachai','Wirachat','Wiraphan','Wiraphon','Wirasak','Wirasak','Wirat','Wiriya','Wisa','Wiset','Wisit','Witya','Woraporn','Yanin','Yaowapha','Yingyot','Yupin','Yuth','Yuwarat']

#Surnames list
    surname = ['Aromdee','Atitarn','Bunyasarn','Chaiprasit','Chaisurivirat','Jetatikarn','Jetjirawat','Juntasa','Kadesadayurat','Kaewburesai','Kaouthai','Kasamsun','Kitjakarn','Kongkatitum','Kongpaisarn','Kongsangchai','Kraiputra','Kunakorn','Kunchai','Kurusarttra','Leekpai','Leelapun','Lertkunakorn','Maleenon','Maneerattana','Meesang','Narkbunnum','Narkhirunkanok','Nimitwanitch','Ornlamai','Paowsong','Parnpradub','Parnthong','Pornpipatpong','Prasongsanti','Puntasrima','Punyawong','Rojjanasukchai','Rojumanong','Saenamuang','Sakda','Sangsorn','Shinawatra','Sirisopa','Somwan','Songprawati','Sripituksakul','Srisati','Sriwarunyu','Sukbunsung','Suntornnitikul','Suppamongkon','Suttirat','Tawisuwan','Thumying','Tuntayakul','Udomprecha','Vipavakit','Visalyaputra','Wattanapanit','Wattanasin','Yongjaiyut','Yuvaves']

#Starting 'ID' variable
    cusid = 1

#'for' loop to set the number of IDs to generate
    for i in range(0,30):

#One of the next 2 sets of codes will be used and the other will be commented.
#Customer name and sex randomizer
        num = random.randint(0,1)
        if num == 0:
            num = random.randint(0,len(malename)-1)
            fname = malename[num]
            sex = 'Male'
        elif num == 1:
            num = random.randint(0,len(femalename)-1)
            fname = femalename[num]
            sex = 'Female'
        num = random.randint(0,len(surname)-1)
        lname = surname[num]
        name = '{} {}'.format(fname,lname)

#Staff name and sex randomizer
#        num = random.randint(0,len(staff)-1)
#        fname = staff[num]
#        num = random.randint(0,len(surname)-1)
#        lname = surname[num]
#        name = '{} {}'.format(fname,lname)
#        sexformat = ['Male', 'Female']
#        sex = sexformat[random.randint(0,1)]

#Age randomizer
#        age = random.randint(18,59)

#Civilian ID generator
        civid = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        civid[0] = random.randint(1,8)
        for i in range(1,11):
            civid[i] = random.randint(0,9)
        last = (civid[0]*13) + (civid[1]*12) + (civid[2]*11) + (civid[3]*10) + (civid[4]*9) + (civid[5]*8) + (civid[6]*7)\
        + (civid[7]*6) + (civid[8]*5) + (civid[9]*4) + (civid[10]*3) + (civid[11]*2)
        last = last % 11
        civid[12] = 11 - last
        last = ''
        for i in civid:
            last = last + str(i)
        civid = last

#Phone Number Generator
        phone = [0,0,0,0,0,0,0,0,0,0]
        phone[1] = random.randint(8,9)
        for i in range(2,9):
            phone[i] = random.randint(0,9)
        last = ''
        for i in phone:
            last = last + str(i)
        phone = last

#Salary Generator for staffs
#        salary = random.randint(15000,30000) // 100 * 100

#Role Randomizer for staffs
#        roleset = ['Clerk', 'Janitor', 'IT Support', 'Security', 'Cook', 'Waiter']
#        role = roleset[random.randint(0,len(roleset)-1)]

#All variables arranged for SQL uses
#For customers
        print("(%0.10d, '{}', '{}', '{}', '{}'),".format(name,sex,phone,civid)%cusid)
#For staffs
#        print("(%0.5d, '{}', '{}', '{}', '{}', '{}', '{}'),".format(name,age,phone,sex,role,salary)%cusid)

#This line will add the ID number
        cusid += 1

main()