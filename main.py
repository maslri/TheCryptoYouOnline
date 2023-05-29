import bs4
import requests
import json
import pyodbc
from sklearn import tree


def insert_baby(dic_baby):
    connection_db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL '
                                   'Server};SERVER=MOHAMMADALI-PC;DATABASE=TheCryptoYouFindBaby;UID=babyadmin;PWD'
                                   '=baby123')
    cursor = connection_db.cursor()
    param = (
        dic_baby['name'], dic_baby['nft_id'], str(dic_baby['level']), str(dic_baby['total_score']),

        dic_baby['dpm_type'],

        dic_baby['role_name'], str(dic_baby['rarity']), str(dic_baby['strength']), str(dic_baby['dexterity']),

        str(dic_baby['vitality']),

        str(dic_baby['mentality']), str(dic_baby['grit']), str(dic_baby['stamina']), dic_baby['main_stat'],

        dic_baby['sub_stat'],

        str(round(float(dic_baby['sale_price_usd']), 2)), str(round(float(dic_baby['sale_price_normalized']), 2)),

        str(round(float(dic_baby['milk_per_day']), 2)),

        str(dic_baby['payback_days']), str(round(float(dic_baby['annualized_roi_percentage']), 2))
    )
    print(param)

    count = list(cursor.execute("select count(*) from BABY where HASH_ID = ?", dic_baby['nft_id']))

    if count[0][0] == 0:

        cursor.execute('''
                       insert into BABY(NAME, HASH_ID, LEVEL_NUMBER, TOTAL_SCORE, DAMAGE_TYPE, ROLE, RARITY, STRENGHT, 
                       DEXTERITY, VITALITY, MENTALITY, GRIT, STAMINA, MAIN_STAT, SUB_STAT, PRICE_DOLLAR, PRICE_BABY, 
                       ESTIMATED_PROFIT_BABY, PAYBACK, ROI) values 
                       (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                       ''', param)
    else:
        print(
            "-------------------------------------------------  The kid is in the database  -------------------------------------------------")
    
    connection_db.commit()
    
    connection_db.close()


def load_baby_page(response):
    soup_response = bs4.BeautifulSoup(response.text, "html.parser")
    baby_sale = soup_response.find('div', attrs={'id': 'app'})
    scripts = baby_sale.get('data-page')
    dic_baby = json.loads(scripts)
    props = dic_baby['props']
    results = props['results']
    data = results['data']
    if not data:
        return False
    for x in data:
        insert_baby(x)
    return True


def start_insert_baby_market():
    page = 1
    while True:
        print("page : " + str(page))
        response = requests.get("https://thecryptoyou.online/baby-finder?per_page=75&page=" + str(page))
        if response.ok:
            if not load_baby_page(response):
                return print("All children were included!")
        else:
            return print(response.status_code)
        page += 1


def fetch_babies():
    connection_db = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL '
                                   'Server};SERVER=MOHAMMADALI-PC;DATABASE=TheCryptoYouFindBaby;UID=babyadmin;PWD'
                                   '=baby123')
    cursor = connection_db.cursor()
    cursor.execute("select * from BABY")
    babies = cursor.fetchall()
    connection_db.commit()
    connection_db.close()
    return babies


def start_machine_learning():
    x = []
    y = []
    babies = fetch_babies()
    for baby in babies:
        input_param_baby = [baby.TOTAL_SCORE, baby.LEVEL_NUMBER, baby.STRENGHT, baby.DEXTERITY, baby.VITALITY, baby.MENTALITY, baby.GRIT, baby.STAMINA]
        output_param_baby = baby.PRICE_BABY
        x.append(input_param_baby)
        y.append(output_param_baby)
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(x, y)
    return clf


def calculate_the_price_baby(total_score, level, strength, dexterity, vitality, mentality, grit, stamina):
    clf = start_machine_learning()
    input_values = [(total_score, level, strength, dexterity, vitality, mentality, grit, stamina)]
    price = clf.predict(input_values)
    return str(price)


if __name__ == '__main__':
    while True:
        start_command_project = int(input("[ start fetch baby market : 1, calculate the price : 2 ]  "))
        if start_command_project == 1:
            start_insert_baby_market()
        elif start_command_project == 2:
            total_score = input("total_score : ")
            level = input("level : ")
            strength = input("strength : ")
            dexterity = input("dexterity : ")
            vitality = input("vitality : ")
            mentality = input("mentality : ")
            grit = input("grit : ")
            stamina = input("stamina : ")
            print("My prediction of your baby price : " + calculate_the_price_baby(total_score, level, strength, dexterity, vitality, mentality, grit, stamina))
