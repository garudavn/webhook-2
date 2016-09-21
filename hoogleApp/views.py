# -*- coding: utf-8 -*-

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
import requests
import json

class Test(APIView):
  def post(self, request):
    resp = GetEstimateData()
    Resp = Response(resp, content_type='application/json; charset=utf-8')
    return Resp
    
def GetEstimateData():
  url = 'https://valuation.homify.com.vn/RealEstatePriceService/landprice/'
  req = json.dumps({'cuoi':'','dau':'','diadiem':'HN','dientich':'80','duong':'Cầu Giấy','loaiBDS':'D','loaiduong':'D','mattien':'','nam':'2016','phuong':'Quan Hoa','quan':'Cầu Giấy'})
  response = requests.post(url,data=req)
  resp = response.json()
  gia = resp.get('Gia')
  speech = {"speech": "Homify gia nha cua ban la:" + gia}
  return {
       "speech": speech,
       "displayText": speech,
       #"data": {},
       # "contextOut": [],
       "source": "apiai-dinh-gia"
   }
  








