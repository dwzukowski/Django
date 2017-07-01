# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Founder, Concern, Asset, Liability, Equity, AssetType, LiabilityType
import bcrypt 
from decimal import *
from django.db.models import Count, Min, Sum, Avg

def index(request):
    return render(request, 'register/index.html')
def register(request):
    check= Founder.manager.add(request.POST['name'], request.POST['email'],request.POST['userName'], request.POST['password'], request.POST['confirmpassword'])
    if not check[0]:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/')
    else:
        request.session['loggedinUser']= check[1].id
        return redirect('/company')
def company(request):
    if not 'loggedinUser' in request.session:
        messages.add_message(request, messages.ERROR, 'Please sign in')
        return redirect('/')
    else:
        context={
            'founder': Founder.manager.get(id=request.session['loggedinUser']),
            'concerns': Concern.manager.filter(founder_id=request.session['loggedinUser'])
        }
        return render(request, 'register/company.html', context)
def logout(request):
    request.session.clear()
    return redirect('/')
def login(request):
    check= Founder.manager.loginValidation(request.POST['userName'], request.POST['password'])
    print check
    if not check[0]:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/')
    else:
        request.session['loggedinUser']= check[1]
        return redirect('/company')
def newconcern(request):
    check= Concern.manager.add(request.session['loggedinUser'], request.POST['name'], request.POST['description'], request.POST['industry'], str(request.POST['founded_at']))
    if not check[0]:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
        return redirect('/company')
    request.session['loggedinConcern']= check[1].id
    return redirect('/company')
def financials(request, concern_id):
    context={
        'concern': Concern.manager.get(id=concern_id)
    }
    print context['concern'] 
    return render(request, 'register/financials.html', context)
def getstarted(request, concern_id):
    request.session['loggedinConcern']= concern_id
    context={
        'types': AssetType.manager.all(),
        'assets': Asset.manager.filter(concern_id=request.session['loggedinConcern']),
        'total_assets': Asset.manager.filter(concern_id=request.session['loggedinConcern']).aggregate(total_assets=Sum('cost')),
        'liabilityTypes': LiabilityType.manager.all(),
        'liabilities': Liability.manager.filter(concern_id=request.session['loggedinConcern']),
        'total_liabilities': Liability.manager.filter(concern_id=request.session['loggedinConcern']).aggregate(total_liabilities=Sum('value')),
    }
    return render(request,'register/getstarted.html', context)
def addAssetType(request):
    check= AssetType.manager.add(request.POST['assettype'])
    print check
    if not check[0]:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
    return redirect('/company/financials/getstarted/{}'.format(request.session['loggedinConcern']))

def addAsset(request):
    print request.POST['assetType']
    assetType= AssetType.manager.filter(name=request.POST['assetType'])
    assetType= assetType[0].id
    check= Asset.manager.add(request.session['loggedinConcern'], assetType, request.POST['description'], Decimal(request.POST['cost']), str(request.POST['acquired_at']))
    print check
    #print getcontext()
    #print type(Decimal(request.POST['cost']))
    if not check[0]:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
    return redirect('/company/financials/getstarted/{}'.format(request.session['loggedinConcern']))

def destroyAsset(request, asset_id):
    context={
        'asset': Asset.manager.get(id=asset_id),
    }
    return render(request,'register/confirmAssetDestroy.html', context)
def confirmDestroyAsset(request, asset_id):
    Asset.manager.destroy(asset_id)
    return redirect('/company/financials/getstarted/{}'.format(request.session['loggedinConcern']))

def createLiabilityType(request):
    check= LiabilityType.manager.add(request.POST['type'])
    print request.POST['type']
    if not check[0]:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
    return redirect('/company/financials/getstarted/{}'.format(request.session['loggedinConcern']))
def addLiability(request):
    liabilityType= LiabilityType.manager.get(name=request.POST['liabilityType'])
    liabilityType= liabilityType.id
    check= Liability.manager.add(request.session['loggedinConcern'], liabilityType, request.POST['description'], Decimal(request.POST['value']), str(request.POST['incurred_at']))
    if not check[0]:
        for message in check[1]:
            messages.add_message(request, messages.ERROR, message)
    return redirect('/company/financials/getstarted/{}'.format(request.session['loggedinConcern']))

def destroyLiability(request, liability_id):
    context={
        'liability': Liability.manager.get(id=liability_id),
    }
    return render(request,'register/confirmLiabilityDestroy.html', context)
def confirmDestroyLiability(request, liability_id):
    Liability.manager.destroy(liability_id)
    return redirect('/company/financials/getstarted/{}'.format(request.session['loggedinConcern']))