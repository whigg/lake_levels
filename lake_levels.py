from lxml import html
import requests


def GetRawData(date):
    page = requests.get('http://data.hydrometdataservice.info/dwr/report.aspx?dt={0}'.format(date))
    tree = html.fromstring(page.content)
    return tree
    
def GetTemperatures(weather):
    temperatures = weather[0].split(' ')[2]
    temp_high = temperatures.strip().split('/')[0]
    temp_low = temperatures.split('/')[1]
    return temp_high, temp_low

def GetHumidity(weather):
    humidity = weather[1].strip().split(' ')[1]
    humidity_high = humidity.strip().split('/')[0]
    humidity_low = humidity.split('/')[1]
    return humidity_high, humidity_low

def GetAverages(weather):
    averages = weather[2].strip().split(' ')[2]
    average_high = averages.strip().split('/')[0]
    average_low = averages.split('/')[1]
    return average_high, average_low

tree = GetRawData('2/28/2017')
weather = tree.xpath('//p[@class="temperatureValue"]/text()')
reservoirs = tree.xpath('//td[@class="siteLabel"]/text()')
reservoirs_shaded = tree.xpath('//td[@class="values values-shaded"]/text()')
reservoirs_unshaded = tree.xpath('//td[@class="values"]/text()')
temps = GetTemperatures(weather)
humidity = GetHumidity(weather)
averages = GetAverages(weather)
#print temps[0] + " F"
#print temps[1] + " F"
#print averages[0] + " F"
#print averages[1] + " F"
#print humidity[0] + " %"
#print humidity[1] + " %"
print reservoirs[0] + ": " + reservoirs_shaded[0] + " : " + reservoirs_shaded[1] + " : " + reservoirs_unshaded[0] + " : " + reservoirs_shaded[2] + " : " + reservoirs_shaded[3] + " : " + reservoirs_unshaded[1] + " : " + reservoirs_shaded[4]
