
import warnings
import pandas as pd
from search.main import Search, Storage
from search.blocks import Block, EndData, Link
from search.options import SearchOptions
from search.page_loader import PageLoader
from search.selectors import Selector
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

pageNumber = 1
maxPages = 8
resultFileName = "output.xlsx"
storage = Storage()

while True:
   websiteUrl = f"https://www.goszakup.gov.kz/ru/registry/rqc?count_record=70&page={pageNumber}"
   searchOptions = SearchOptions(
      url=websiteUrl,
      blocks=[
         Block(Selector("#main-wrapper > div.content-block > div.panel.panel-info > div.panel-body > div > table"), "Table",
            [
               Block(Selector("tbody tr"), "Row",
                  [
                     EndData(Selector('td:nth-child(2) > a > strong'), "Название предприятия"),
                     EndData(Selector('td:nth-child(3)'), "БИН предприятия"),
                     Link(Selector('td:nth-child(2) > a'), "Детали", [
                           EndData(Selector("#main-wrapper > div.content-block > div:nth-child(4) > div:nth-child(5) > div.panel-body > table > tr:nth-child(1) > td"), "ИИН"),
                           EndData(Selector("#main-wrapper > div.content-block > div:nth-child(4) > div:nth-child(5) > div.panel-body > table > tr:nth-child(3) > td"), "ФИО"),
                           EndData(Selector("#main-wrapper > div.content-block > div:nth-child(4) > div:nth-child(6) > div.panel-body > table > tr:nth-child(2) > td:nth-child(3)"), "Полный Адрес"),
                     ])
                  ]
               )
            ]
         )
      ]
   )
   pageLoader = PageLoader(
      delay=0.7,
      threshold=1.3
   )
   search = Search(
      options=searchOptions,
      pageLoader=pageLoader,
      storage=storage
   )
   search.run()

   pageNumber += 1
   if pageNumber >= maxPages:
      break



def toExcel(data:dict):
   df = pd.DataFrame(data)
   df.drop_duplicates(inplace=True)
   df.to_excel(resultFileName, index=False)

toExcel(storage.get())







