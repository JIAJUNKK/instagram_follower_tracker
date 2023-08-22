# Checking who don't follow back you on Instagram
Install selenium on terminal if not installed. 

    pip install selenium

\

If encounters error such as **_This version of ChromeDriver only supports Chrome version xx_**.
### Try running either two of the below:
#### 1. Installing webdriver-manager
        1. pip install webdriver-manager
        2. from webdriver_manager.chrome import ChromeDriverManager
        3. driver = webdriver.Chrome(ChromeDriverManager().install())

#### 2. Upgrading the chrome driver on terminal
        brew upgrade chromedriver --cask


