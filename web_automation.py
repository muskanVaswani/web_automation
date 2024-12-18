from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
import logging  
logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.DEBUG)

#Load data from the CSV
data_file = 'C:\\Users\\Muskan\\Desktop\\cactus\\web_automation\\product_data.csv'
product_data = pd.read_csv(data_file,encoding='ISO-8859-1')
#print(product_data.columns)

def searchProduct():
    try:
        # Loop through the data file and add data
        for index, row in product_data.iterrows():
            try:
                product_name = row['Material']  # Ensure this matches the CSV column
                time.sleep(8)
                search_box = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[2]/div/div[1]/div/input")
                search_box.send_keys(product_name+ Keys.ENTER)
                #print(f"Searched for product: {product_name}")
                time.sleep(2)  # Adjust sleep as needed
            except KeyError:
                print(f"Row is missing the 'Material' column.")
            except Exception as e:
                print(f"Error processing row")

            
            #clicking product box
            product_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[1]/div')
            product_box.click()
            time.sleep(5)

            #specification button
            specification = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/div[1]/div[2]/div[4]/div[1]/ul/li[3]/a')
            specification.click()

            time.sleep(3)
 
            specsTextDiv = driver.find_element(By.XPATH, '//*[@id="product_specifications_0"]')#//*[@id="product_specifications_0"]/p'
            specsTextDiv.click()
            # specsTextDiv.clear()
            # time.sleep(2)
            specsTextDiv.send_keys("/2" + Keys.ENTER)
            time.sleep(2)
            
    
            #adding text in column 1
            find_col1 = driver.find_element(By.XPATH, '//*[@id="product_specifications_0"]/div/div/div[1]/p')
            #//*[@id="product_specifications_0"]/div/div/div/p'
            find_col1.click()
            time.sleep(2)
            
            #adding specification heading
            find_col1.send_keys("Specifications")
            time.sleep(1)
            
            time.sleep(8)
           
            
            
            #adding specification
            productSpecs = row['Specifications']
            find_col1.send_keys(Keys.ENTER)
            find_col1.send_keys(productSpecs)
        
            time.sleep(5)
            
            dimensions = driver.find_element(By.XPATH, '//*[@id="product_specifications_0"]/div/div/div[1]/p')
            time.sleep(2)
            find_col1.send_keys(Keys.ENTER)
            find_col1.send_keys(Keys.ENTER)
            find_col1.send_keys(Keys.ENTER)
            find_col1.send_keys(Keys.ENTER)
            
            
            dimensions.send_keys('Dimensions' + Keys.ENTER)
            time.sleep(3)
            
            
            #adding dimensions
            #widths
            widths = row['Width (in.)']
            dimensions.send_keys('Width(in.) - '+ widths + Keys.ENTER)
            #dimensions.send_keys(Keys.ENTER)
            time.sleep(5)
            
            #depth
            depths = row['Depth (in.)']
            dimensions.send_keys('Depth(in.) - '+ depths)
            dimensions.send_keys(Keys.ENTER)
            time.sleep(5)
            
            #length
            lengths = row['Length (in.)']
            dimensions.send_keys('Length(in.) - '+ lengths + Keys.ENTER)
            #dimensions.send_keys(Keys.ENTER)
            time.sleep(5)
            
            #Thickness
            thicknesses = row['Thickness (in.)']
            dimensions.send_keys('Thickness(in.) - '+ str(thicknesses))
            dimensions.send_keys(Keys.ENTER)
            time.sleep(5)
            
            #gauge
            gauge = row['Gauge']
            dimensions.send_keys('Gauge - ' + str(gauge))
            dimensions.send_keys(Keys.ENTER)
            time.sleep(5)
            
            #Weight lb/ft
            weight = row['Weight lb/ft']
            dimensions.send_keys('Weight lb/ft - ' + str(weight))
            dimensions.send_keys(Keys.ENTER)
            time.sleep(5)
        
        
            #adding benefits
            productdesc = row['Descriptions']
            descText = driver.find_element(By.XPATH , '//*[@id="product_specifications_0"]/div/div/div[2]/p')
            descText.click()
            descText.send_keys("Benefits")
            descText.send_keys(Keys.ENTER + productdesc)
            time.sleep(2)
            
            #country of origin
            descText.send_keys(Keys.ENTER)
            descText.send_keys(Keys.ENTER)
            descText.send_keys(Keys.ENTER)
            
            
            descText.send_keys('Country of Origin'+ Keys.ENTER)
            origin = row['Country of Origin']
            time.sleep(8)
            
            origin = row.get('Country of Origin', '')  # Use .get() to avoid KeyError
            if pd.isna(origin) or origin.strip() == "":
                logging.info(f"Country of Origin not found for product {product_name}, using default: Canada")
                origin = "Canada"
            descText.send_keys(str(origin))
            #descText.send_keys(Keys.ENTER + origin)
            
            
            
            #saving data
            save = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[1]/div[3]/div/button[1]')
            save.click()
            time.sleep(2)
            
            #going back to products
            product = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div[1]/div[2]/ol/li/a')
            product.click()
            time.sleep(2)
            
            #cancelling existing product
            cross_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[2]/div/div[1]/div/div[2]/div[3]/button')
            cross_button.click()
            time.sleep(2)
            
            
            
    finally:       
        pass     

#headless
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
# chrome_options.add_argument('--ignore-certificate-errors')  # Ignore SSL errors
# chrome_options.add_argument('--disable-web-security')       # Disable web security
chrome_options.add_argument('--allow-insecure-localhost')


# Set up the chrome WebDriver with the Service class
service = Service(executable_path="web_automation\\chromedriver.exe")
driver = webdriver.Chrome(service = service, options = chrome_options)
print({})
try:
    # Open the specified URL
    driver.get("http://89.233.104.212:8080//web//login")

    # Wait for 5 seconds
    time.sleep(5)

    # Find the username input field using XPath and enter the username
    username_field = driver.find_element(By.XPATH, '//*[@id="login"]')
    username_field.send_keys("admin")

    # Find the Password input field using XPath and enter the username
    username_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    username_field.send_keys("admin123")

    # Wait for 5 seconds
    time.sleep(5)

    # Find the login button using XPath and click it
    login_button = driver.find_element(By.XPATH, '//html/body/div[1]/main/div[1]/form/div[3]/button')  # Update with the correct XPath
    login_button.click()

    # Wait for 10 seconds
    time.sleep(5)

    # Find the inventory and click it
    inventory_button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[13]/a/img')
    inventory_button.click()

    # Wait for 10 seconds
    time.sleep(5)

    # driver.get("http://89.233.104.212:8080/web#action=486&model=product.template&view_type=kanban&cids=1&menu_id=325")

    WebDriverWait(driver,5).until(
    ec.presence_of_element_located((By.XPATH, '/html/body/header/nav/div[1]/div[2]'))
    )

    product_dropdown = driver.find_element(By.XPATH, '/html/body/header/nav/div[1]/div[2]')
    product_dropdown.click()


    WebDriverWait(driver,5).until(
    ec.presence_of_element_located((By.XPATH,"/html/body/header/nav/div[1]/div[2]/div/a[1]"))
    )
    product_button = driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[2]/div/a[1]")
    product_button.click()

    time.sleep(5)

    #function calling to search product and enter details
    searchProduct()
    time.sleep(5)


    # Wait for search results to appear
    time.sleep(1003)
    #time.sleep(5)
    
except Exception as e:
    print(f"Error: {e}")  # Print the error message
    time.sleep(100)
