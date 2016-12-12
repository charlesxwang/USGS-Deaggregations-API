'''
    This function is used to download data from USGS 2008 deaggint tool
    home = 'http://geohazards.usgs.gov/deaggint/2008/'
    Author: Charles Wang
    Clemson University
    Date:12-27-2015
'''


from bs4 import BeautifulSoup as bs
import requests
import wget
import os


def worker(pars_string):

    '''
        pars_string: a string contains the following pars in the order:
        name,latitude,longitude,percent,vs30,years,sa,gmpe,geo
        files will be put in the download folder
    '''
    
    headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    s = requests.session()

    home = 'http://geohazards.usgs.gov/deaggint/2008/'


    name,latitude,longitude,percent,vs30,years,sa,gmpe,geo = pars_string.strip().split()
    '''
    # set paras
    name='mysite'
    latitude = 37.771882
    longitude = -122.263711
    percent = 2
    vs30 = 500
        
    years = 50
    sa = 1
    gmpe = 1
    geo = 1
    '''

    # cook url
    url = 'http://geohazards.usgs.gov/deaggint/2008/application.php?'
    url += 'name=' + name
    url += '&latitude=' + latitude
    url += '&longitude=' + longitude
    url += '&percent=' + percent
    url += '&years=' + years
    url += '&sa=' + sa
    url += '&gmpe=' + gmpe
    url += '&geo=' + geo
    url += '&vs30=' + vs30
    print(url)

    # load website
    result = requests.get(url)
    print(result.status_code)
    c = result.content

    # parse
    soup = bs(c, "html.parser")
    txtLinks = soup.find_all("link")
    txtFile = txtLinks[0]['url']
    print(txtFile)

    # download
    if not os.path.exists('download'):
        os.makedirs('download')
    wget.download(txtFile,'download/'+name+'.txt')

