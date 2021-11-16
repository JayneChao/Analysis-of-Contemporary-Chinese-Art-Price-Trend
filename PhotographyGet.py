# filter: Medium(Photography),Artist Nationality(Chinese),Time Period(2020s,2010s,2000s,1990s,1980s)
# url: https://www.artsy.net/collect?major_periods%5B0%5D=2020&major_periods%5B1%5D=2010&major_periods%5B2%5D=2000&major_periods%5B3%5D=1990&major_periods%5B4%5D=1980&additional_gene_ids%5B0%5D=photography&artist_nationalities%5B0%5D=Chinese&acquireable=false&offerable=false&at_auction=false&inquireable_only=false


import requests
import parsel
import csv

for page in range (1, 101):
    print(f'------page{page}data------')

    url = f'https://www.artsy.net/collect?major_periods%5B0%5D=2020&major_periods%5B1%5D=2010&major_periods%5B2%5D=2000&major_periods%5B3%5D=1990&major_periods%5B4%5D=1980&page={page}&additional_gene_ids%5B0%5D=photography&artist_nationalities%5B0%5D=Chinese&acquireable=false&offerable=false&at_auction=false&inquireable_only=false'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'}

    response = requests.get(url=url, headers=headers)
    html_data = response.text

    selector = parsel.Selector(html_data)
    aLabels = selector.css('.RouterLink__RouterAwareLink-sc-9hegtb-0.fNoXYF')
    for a in aLabels:
        artist = a.css('.Box-sc-15se88d-0.Text-sc-18gcpao-0.dmqYKK::text').get()
        title = a.css('.Box-sc-15se88d-0.Text-sc-18gcpao-0.caIGcn.kySEpG i::text').get()
        artworkYear = a.css('.Box-sc-15se88d-0.Text-sc-18gcpao-0.caIGcn.kySEpG::text').get()
        institute = a.css('.Box-sc-15se88d-0.Text-sc-18gcpao-0.caIGcn.hENCPo::text').get()
        price = a.css('.Box-sc-15se88d-0.Text-sc-18gcpao-0.eXbAnU.jkuGdd::text').get()
        print(artist,title,artworkYear,institute,price, sep='---')

        with open('PhotographyGet.csv', mode='a', encoding='utf_8_sig', newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerow([artist, title, artworkYear, institute, price])