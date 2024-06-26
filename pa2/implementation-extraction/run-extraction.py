from regex_extraction import *
from xpath_extraction import *

if __name__ == '__main__':
    # Overstock jewelry 1 page
    #jewelry_01_file = '../input-extraction/WebPages/overstock.com/jewelry01.html'
    #extractor = OverstockRegularExpressionExtractor(file_path=jewelry_01_file, save_dir='./results/jewelry1/')
    #extractor = OverstockXPathExtractor(file_path=jewelry_01_file, save_dir='./results/jewelry1/')
    #json_data = extractor.to_json()
    #print(json.dumps(json_data, indent=4))

    # Overstock jewelry 2 page
    #jewelry_02_file = '../input-extraction/WebPages/overstock.com/jewelry02.html'
    #extractor2 = OverstockRegularExpressionExtractor(file_path=jewelry_02_file, save_dir='./results/jewelry2/')
    #extractor2 = OverstockXPathExtractor(file_path=jewelry_02_file, save_dir='./results/jewelry2/')
    #json_data2 = extractor2.to_json()
    # print(json.dumps(json_data2, indent=4))

    # Rtvslo Audi page
    #audi_file = '../input-extraction/WebPages/rtvslo.si/audi.html'
    #extractor3 = RtvsloRegularExpressionExtractor(file_path=audi_file, save_dir='./results/audi/')
    #extractor3 = RtvsloXPathExtractor(file_path=audi_file, save_dir='./results/audi/')
    #json_item = extractor3.to_json()
    # print(json_item)

    # Rtvslo Volvo
    #volvo_file = '../input-extraction/WebPages/rtvslo.si/volvo.html'
    #extractor4 = RtvsloRegularExpressionExtractor(file_path=volvo_file, save_dir='./results/volvo/')
    #json_item2 = extractor4.to_json()
    #print(json_item2)
	
    # BigBang
    #bigbang_file = '../input-extraction/CustomPages/bigbang.si/bigbang.html'
    #extractor4 = BigBangRegularExpressionExtractor(file_path=bigbang_file, save_dir='./results/bigbang/')
    #extractor4 = BigBangXPathExtractor(file_path=bigbang_file, save_dir='./results/bigbang/')
    #json_item = extractor4.to_json()
    #print(json_item)
	
	#Craiglist
    craiglist_file = '../input-extraction/CustomPages/craigslist.com/birmingham, AL video gaming - craigslist.html'
    extractor5 = CraigsListRegularExpressionExtractor(file_path=craiglist_file, save_dir='./results/craiglist/')
    #extractor5 = CraigsListXPathExtractor(file_path=craiglist_file, save_dir='./results/craiglist/')
    json_item = extractor5.to_json()
    #print(json_item)