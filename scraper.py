import requests
from bs4 import BeautifulSoup
import smtplib

# The below URL points to 'Lenovo Legion 7i Core i7 10th Gen' laptop on flipkart
# You may change the URL as you please
URL = 'https://www.flipkart.com/lenovo-legion-7i-core-i7-10th-gen-16-gb-1-tb-ssd-windows-10-home-8-gb-graphics-nvidia-geforce-rtx-2080-super-max-q-144-hz-15imhg05-gaming-laptop/p/itm23265f2e8bfe9?pid=COMFU7ANQZYJGA9N&lid=LSTCOMFU7ANQZYJGA9N7UKB0I&marketplace=FLIPKART&q=Lenovo+Legion+&store=6bo&srno=s_1_2&otracker=search&fm=Search&iid=e90298a7-a030-4811-af51-74024b8440dd.COMFU7ANQZYJGA9N.SEARCH&ppt=browse&ppn=browse&ssid=zd1njxijts0000001645161975959&qH=aec8cc6f34a63bdd'

# Instead of the '#' charcater below, enter your User Agent
# You can find out your User Agent by searching 'my user agent' on google 
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # The class below represents the html <div> block containing the price of the priduct to be tracked 
    # It can be changed as per requirement  
    price = soup.find(class_ ="_30jeq3 _16Jk6d").get_text()
    price = price.replace(',', '')
    
    try:
        # Remove the first character if it is not numeric
        if ord(price[0]) < 48 or ord(price[0]) > 57:
            price = price.replace(price[0], "")
        price = int(price)

    except ValueError as error:
        # Throw an exception if the given string cannot be converted to integer type
        print("Error !",error,"\nThe given value is of String type and it cannot be converted to an integer.")

    if(price < 100000):
        # Function send_mail() call
        send_mail()

    # display the Rs. symbol along with the price  
    print(u'\u20B9','{:,}'.format(price))

def send_mail():
    # SMPT port 587 is used by most email providers
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    # Enter your email id and password respectively below
    server.login('mayank.n.motwani@gmail.com', 'pdurifrboksmbnzv')

    # The email sent will have the following format
    subject = 'Price Fell Down !'
    body = 'Check the flipkart link https://www.flipkart.com/lenovo-legion-7i-core-i7-10th-gen-16-gb-1-tb-ssd-windows-10-home-8-gb-graphics-nvidia-geforce-rtx-2080-super-max-q-144-hz-15imhg05-gaming-laptop/p/itm23265f2e8bfe9?pid=COMFU7ANQZYJGA9N&lid=LSTCOMFU7ANQZYJGA9N7UKB0I&marketplace=FLIPKART&q=Lenovo+Legion+&store=6bo&srno=s_1_2&otracker=search&fm=Search&iid=e90298a7-a030-4811-af51-74024b8440dd.COMFU7ANQZYJGA9N.SEARCH&ppt=browse&ppn=browse&ssid=zd1njxijts0000001645161975959&qH=aec8cc6f34a63bdd'

    msg = f"Subject: {subject}\n\n{body}"

    sender = 'mayank.n.motwani@gmail.com'
    recipients = ['mayank.n.motwani@gmail.com', '2018.mayank.motwani@ves.ac.in']

    server.sendmail(
        sender,
        recipients,
        msg
    )
    print('HEY EMAIL HAS BEEN SENT !')

    server.quit()

# Function check_price() call
check_price()