from email import message
from django.shortcuts import render
from django.http import HttpResponse,FileResponse
import os
import pathlib
from django.shortcuts import redirect
import json
from app import WCSC
# Create your views here.

def download(req,folder):
    pass

def index(req):
    # to call function and WCSC.py
    if(req.method == "POST"):
        print("####",req.POST)
        url = req.POST['url']
        depth = int(req.POST['depth'])
        headers=0
        if( req.POST['header']== 1):
            headers=1
        images=0
        if( req.POST['images']== 1):
            images=1
        links=0
        if( req.POST['links']== 1):
            links=1
        mails=0
        if( req.POST['mails']== 1):
            mails=1
        print(req.POST,"######")
        # body_unicode = req.body.decode('utf-8')
        # body = json.loads(req.body)
        WCSC.crawl(url,depth,headers,images,links,mails)
        folder= os.path.join(str(os.getcwd() + "\\report.zip"))
        print(folder)
        file_server= pathlib.Path(folder)
        if not file_server.exists():
            return  HttpResponse("file not found")
        else:
            file_to_download = open(str(file_server), 'rb')
            response = HttpResponse(file_to_download, content_type='application/force-download')
            response['Content-Disposition'] = 'attachment; filename="%s"' % 'report.zip'
            return response
        return redirect('/')




    return render(req,"index.html")