# Import for the Web Bot
from botcity.web import WebBot, Browser, By

# Importar as bibliotecas do excel
from botcity.plugins.excel import BotExcelPlugin




def main():
    # Instancia o Web Bot
    bot = WebBot()

    # Configure whether or not to run on headless mode
    bot.headless = False

    # Uncomment to change the default Browser to Firefox
    bot.browser = Browser.EDGE

    # Uncomment to set the WebDriver path
    bot.driver_path = r"D:\webdriver\msedgedriver.exe"



    # Instantiate the plugin
    bot_excel = BotExcelPlugin()

    # Read from an Excel File
    dados = bot_excel.read(r'D:\Botcity\RPAChallenge\resources\challenge.xlsx').as_list()[1:]



    # Abre o site do desafio.
    bot.browse(r"https://rpachallenge.com/")

    # Maximize the window.
    bot.maximize_window()



    # Achar os botões Start e Submit
    btnStart = bot.find_element(selector="/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button", by=By.XPATH)
    btnSubmit = bot.find_element(selector="/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input", by=By.XPATH)

    # Clicar no botão Start.
    # Inicia o Desafio.
    btnStart.click()


    # Criando o loop principal do robô.
    for linha in dados:
        # Cria a variável First Name
        strFisrtName = linha[0]

        # Cria a variável Last Name
        strLastName = linha[1]

        # Cria a variável Company Name
        strCompanyName = linha[2]

        # Cria a variável Role in Company
        strRole = linha[3]

        # Cria a variável Adress
        strAdress = linha[4]

        # Cria a variável Email
        strEmail = linha[5]

        # Cria a variável Phone Number
        intPhone = linha[6]

        # Achar os campos e preencher o formulário
        campoFirstName = bot.find_element(selector="//input[@ng-reflect-name='labelFirstName']", by=By.XPATH)
        campoFirstName.send_keys(strFisrtName)

        campoLastName = bot.find_element(selector="//input[@ng-reflect-name='labelLastName']", by=By.XPATH)
        campoLastName.send_keys(strLastName)
        
        campoCompanyName = bot.find_element(selector="//input[@ng-reflect-name='labelCompanyName']", by=By.XPATH)
        campoCompanyName.send_keys(strCompanyName)
        
        campoRoleCompany = bot.find_element(selector="//input[@ng-reflect-name='labelRole']", by=By.XPATH)
        campoRoleCompany.send_keys(strRole)
        
        campoAdress = bot.find_element(selector="//input[@ng-reflect-name='labelAddress']", by=By.XPATH)
        campoAdress.send_keys(strAdress)

        campoEmail = bot.find_element(selector="//input[@ng-reflect-name='labelEmail']", by=By.XPATH)      
        campoEmail.send_keys(strEmail)
        
        campoPhoneNumber = bot.find_element(selector="//input[@ng-reflect-name='labelPhone']", by=By.XPATH)
        campoPhoneNumber.send_keys(intPhone)

        # Clicar no Botão Submit
        btnSubmit.click()


    # Wait 3 seconds before closing
    bot.wait(3000)

    bot.print_pdf(path=r"D:\Botcity\RPAChallenge\resources\finish.pdf")

    # Finish and clean up the Web Browser
    # You MUST invoke the stop_browser to avoid
    # leaving instances of the webdriver open
    bot.stop_browser()

    

def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()

