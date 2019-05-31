def arti_ret(topic):
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import re
    import os, codecs
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    # options.add_argument("--headless")
    driver = webdriver.Chrome('utilities/chromedriver.exe', options= options)
    driver.get("https://en.wikipedia.org/wiki/Main_Page")
    elem = driver.find_element_by_id("searchInput")
    query = topic
    elem.send_keys(query)
    elem.send_keys(Keys.RETURN)
    ps = driver.find_elements_by_tag_name('p')
    art = []
    cit = r'\[[0-9]+\]'
    for p in ps:
        art.append(p.text)
    art_corrected = []
    for sent in art:
        art_corrected.append(re.sub(cit, " ", sent))
    f = codecs.open("utilities/article.txt", "w", encoding="utf8")
    for w in art_corrected:
        f.write(w)
        f.write('\n')
    f.close()
    os.system("notepad.exe utilities/article.txt")

if __name__ == '__main__':
	arti_ret("quantum computing")