
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from WebScraperForAllMusic import parserForInformation

def getDiscography(artist):
    # This parameter is a string that contains the name of the artist
    try:
        browser = webdriver.Chrome()
        browser.get("https://www.allmusic.com")
        browser.maximize_window()
        time.sleep(2)
        searchInput = browser.find_element_by_class_name("site-search-input")
        searchInput.send_keys(artist)
        searchInput.send_keys(u'\ue007')
        time.sleep(2)
        artistsLink = browser.find_element_by_partial_link_text("Artists")
        artistsLink.click()
        results = browser.find_element_by_class_name("results")
        #We get the first element in that list and click on it
        firstResult = results.find_element_by_xpath("//li[1]/div[2]/div[1]/a")
        firstResult.click()
        time.sleep(2)
        
        # x.click()
        time.sleep(2)
        #change to tab discrography 
        tabDisc = browser.find_element_by_css_selector("li.tab.discography")
        action = ActionChains(browser)
        action.move_to_element(tabDisc)
        action.perform()
        time.sleep(2)
        action.click(tabDisc)
        action.perform()
        #print(browser.page_source)
        print(browser.title)
        # print("Yash")
        parserForInformation(browser.page_source)
    except Exception as e:
        print(e)
    finally:
        browser.quit()


def main():
    try:
        artist = input("Give me the name of an artist:\n")
        getDiscography(artist)
    except Exception as e:
        print("Something went wrong, check the error")
        print(e)
        
if __name__== "__main__":
    main()