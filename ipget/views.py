from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import pygeoip
import ipaddress
from collections import defaultdict
from pytz import country_timezones

def index(request):
      return render(request, 'ipget/index.html')

def results(request):
            ipaddr = request.POST.get('ip')
            if ipaddr is '':
                loc=[]
                myfile = request.FILES['ipfile']
                ipaddr = myfile.read()
                ipa =ipaddr.decode("utf-8").split('\n')
                for row in ipa:
                      a=row.strip('\r')
                      if a == "":
                            location= {'dma_code': "-",
                                              'area_code': "Invalid IP",
                                              'metro_code': "Invalid IP",
                                              'postal_code': "Invalid IP",
                                              'country_code': "Invalid IP",
                                              'country_code3': "Invalid IP",
                                              'country_name': "Invalid IP",
                                              'continent': "Invalid IP",
                                              'region_code': "Invalid IP",
                                              'city': "Invalid IP",
                                              'latitude': "Invalid IP",
                                              'longitude': "Invalid IP",
                                              'time_zone': "Invalid IP"}
                            location['ipad']=row.strip('\r')
                            loc.append(location)
                      else:            
                            try: ipaddress.IPv4Address(row.strip('\r'))
                            except (ipaddress.AddressValueError) :
                               try: ipaddress.IPv6Address(row.strip('\r'))
                               except (ipaddress.AddressValueError):
                                     location= {'dma_code': "-",
                                              'area_code': "Invalid IP",
                                              'metro_code': "Invalid IP",
                                              'postal_code': "Invalid IP",
                                              'country_code': "Invalid IP",
                                              'country_code3': "Invalid IP",
                                              'country_name': "Invalid IP",
                                              'continent': "Invalid IP",
                                              'region_code': "Invalid IP",
                                              'city': "Invalid IP",
                                              'latitude': "Invalid IP",
                                              'longitude': "Invalid IP",
                                              'time_zone': "Invalid IP"}
                                     location['ipad']=row.strip('\r')
                                     loc.append(location)
                                     
                               else:
                                     Geoip=pygeoip.GeoIP("ipget\Database\GeoLiteCityv6.dat")
                                     location=Geoip.record_by_addr(row.strip('\r')) 
                                     if location is None:  
                                              location= {'dma_code': "Not Found",
                                                          'area_code': "Not Found",
                                                          'metro_code': "Not Found",
                                                          'postal_code': "Not Found",
                                                          'country_code': "Not Found",
                                                          'country_code3': "Not Found",
                                                          'country_name': "Not Found",
                                                          'continent': "Not Found",
                                                          'region_code': "Not Found",
                                                          'city': "Not Found",
                                                          'latitude': "Not Found",
                                                          'longitude': "Not Found",
                                                          'time_zone': "Not Found"}
                                              location['ipad']=row.strip('\r')
                                              loc.append(location)
                                     else:      
                                              location['ipad']=row.strip('\r')
                                              if location['city'] is None: location['city'] = "Unknown"
                                              if location['time_zone'] is None:
                                                    l = country_timezones(location['country_code'])
                                                    location['time_zone'] = l[0]
                                              loc.append(location)

                            else:
                                  Geoip=pygeoip.GeoIP("ipget\Database\GeoLiteCity.dat")
                                  location=Geoip.record_by_addr(row.strip('\r'))
                                  if location is None:
                                        location= {'dma_code': "Not Found",
                                                    'area_code': "Not Found",
                                                    'metro_code': "Not Found",
                                                    'postal_code': "Not Found",
                                                    'country_code': "Not Found",
                                                    'country_code3': "Not Found",
                                                    'country_name': "Not Found",
                                                    'continent': "Not Found",
                                                    'region_code': "Not Found",
                                                    'city': "Not Found",
                                                    'latitude': "Not Found",
                                                    'longitude': "Not Found",
                                                    'time_zone': "Not Found"}
                                        location['ipad']=row.strip('\r')
                                        loc.append(location)
                                  else:      
                                        location['ipad']=row.strip('\r')
                                        if location['city'] is None: location['city'] = "Unknown"
                                        if location['time_zone'] is None:
                                              l = country_timezones(location['country_code'])
                                              location['time_zone'] = l[0]
                                        loc.append(location)
                                        
                return render(request, 'ipget/fresults.html', {
                                                'loc': loc,
                                            })

            
            else:
                      ipaddr = request.POST.get('ip')
                      try: ipaddress.IPv4Address(ipaddr)
                      except (ipaddress.AddressValueError) :
                                    try: ipaddress.IPv6Address(ipaddr)
                                    except (ipaddress.AddressValueError):
                                           location= {'dma_code': "-",
                                                    'area_code': "Invalid IP",
                                                    'metro_code': "Invalid IP",
                                                    'postal_code': "Invalid IP",
                                                    'country_code': "Invalid IP",
                                                    'country_code3': "Invalid IP",
                                                    'country_name': "Invalid IP",
                                                    'continent': "Invalid IP",
                                                    'region_code': "Invalid IP",
                                                    'city': "Invalid IP",
                                                    'latitude': "Invalid IP",
                                                    'longitude': "Invalid IP",
                                                    'time_zone': "Invalid IP"}
                                           location['ipad']=ipaddr
                                           return render(request, 'ipget/results.html' ,{ 'location': location }) 
                                    else:
                                         Geoip=pygeoip.GeoIP("ipget\Database\GeoLiteCityv6.dat")
                                         location=Geoip.record_by_addr(ipaddr)
                                         if location is None:
                                                  location = {'dma_code': "Not Found",
                                                              'area_code': "Not Found",
                                                              'metro_code': "Not Found",
                                                              'postal_code': "Not Found",
                                                              'country_code': "Not Found",
                                                              'country_code3': "Not Found",
                                                              'country_name': "Not Found",
                                                              'continent': "Not Found",
                                                              'region_code': "Not Found",
                                                              'city': "Not Found",
                                                              'latitude': "Not Found",
                                                              'longitude': "Not Found",
                                                              'time_zone': "Not Found"}
                                                  return render(request, 'ipget/results.html' ,{ 'location': location }) 
                                         else:      
                                                  location['ipad']=ipaddr
                                                  if location['city'] is None: location['city'] = "Unknown"
                                                  if location['time_zone'] is None:
                                                        l = country_timezones(location['country_code'])
                                                        location['time_zone'] = l[0]
                                                  return render(request, 'ipget/results.html', {
                                                          'location': location,
                                                      })

                      else:
                          Geoip=pygeoip.GeoIP("ipget\Database\GeoLiteCity.dat")   
                          location=Geoip.record_by_addr(ipaddr)
                          if location is None:
                                location = {'dma_code': "Not Found",
                                            'area_code': "Not Found",
                                            'metro_code': "Not Found",
                                            'postal_code': "Not Found",
                                            'country_code': "Not Found",
                                            'country_code3': "Not Found",
                                            'country_name': "Not Found",
                                            'continent': "Not Found",
                                            'region_code': "Not Found",
                                            'city': "Not Found",
                                            'latitude': "Not Found",
                                            'longitude': "Not Found",
                                            'time_zone': "Not Found"}
                                return render(request, 'ipget/results.html' ,{ 'location': location }) 
                          else:      
                                location['ipad']=ipaddr
                                if location['city'] is None: location['city'] = "Unknown"
                                if location['time_zone'] is None:
                                      l = country_timezones(location['country_code'])
                                      location['time_zone'] = l[0]
                                return render(request, 'ipget/results.html', {
                                        'location': location,
                                    })


def reset(request):
      return render(request, 'ipget/index.html')
