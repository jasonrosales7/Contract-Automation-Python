from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url="webhook", username="Bot name")


embed = DiscordEmbed(title="X", color=242424)

webhook.add_embed(embed)

Path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(Path)

nameCheckForNew = ""
addressCheckForNew = ""


for x in range(1000000):
    driver.get("https://etherscan.io/contractsVerified")


    x = driver.find_element_by_css_selector("#transfers > div.table-responsive.mb-2.mb-md-0 > table > tbody > tr:nth-child(1) > td:nth-child(2)").text

    y = driver.find_element_by_css_selector("#transfers > div.table-responsive.mb-2.mb-md-0 > table > tbody > tr:nth-child(1) > td:nth-child(1) > a").text

    if (nameCheckForNew != x) & (addressCheckForNew != y):

        nameCheckForNew = x
        addressCheckForNew = y


        embed.set_footer(text="Contract: " + x + " " + y)
        embed.set_timestamp()

        a = "[Click here](https://etherscan.io/address/"
        b = y + "#code)"
        c = a + b
        embed.add_embed_field(name='Link:', value=c)
        response = webhook.execute()
        embed.del_embed_field(0)


    time.sleep(15)
