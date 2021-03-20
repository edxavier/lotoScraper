from flask import Flask
import requests
from selenium import webdriver

app = Flask(__name__)

"""opt = webdriver.ChromeOptions()
opt.add_argument('headless')
opt.add_argument('-disable-dev-shm-usage')
opt.add_argument('--no-sandbox')
browser = webdriver.Chrome(options=opt)
"""

@app.route("/")
def loto_results():
    res = requests.get("https://www.loto.com.ni/")
    return res.text, res.status_code


"""@app.route("/previous")
def loto_previous_results():
    try:
        browser.get('https://www.loto.com.ni/resultados-anteriores/')
        table = browser.find_element_by_xpath("//*[@id='resultados']")
        html = table.get_attribute('innerHTML')
        # html = browser.page_source
        #browser.close()
        return html, 200
    except:
        return "", 500
"""

if __name__ == "__main__":

    app.run(debug=False, host="0.0.0.0", port=7000)
