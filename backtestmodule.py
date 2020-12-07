# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 23:03:40 2020

@author: irod
"""

import csv

import os.path
import os
import time
import pyautogui
from datetime import datetime

done_backtesting_symbol_file='c://users/irod/documents/python/backtest automator/donebacktesting.txt'
#symbolsfile='c://users/irod/documents/python/backtest automator/symbolsIndex.csv'
symbolsfile='c://users/irod/documents/python/backtest automator/symbolsportfolioMixedTrend.csv'
#symbolsfile='c://users/irod/documents/python/backtest automator/symbolsportfolioUptrend.csv'
#symbolsfile='c://users/irod/documents/python/backtest automator/symbolsportfolioDowntrend.csv'
#symbolsfile='c://users/irod/documents/python/backtest automator/symbols2winlose.csv'
#symbolsfile='c://users/irod/documents/python/backtest automator/symbolswinners.csv'
#symbolsfile='c://users/irod/documents/python/backtest automator/symbolslosers.csv'
#symbolsfile='c://users/irod/documents/python/backtest automator/symbolsuncertain.csv'

def update_ts_chart_symbol(sym,index):
    print('serach for stop file:',done_backtesting_symbol_file,'after delay')
    if os.path.exists(done_backtesting_symbol_file):    
        send_symbol(sym)
    else:
        seconds=0;
        """this makes backtesting dynamic in duration"""
        while not os.path.exists(done_backtesting_symbol_file) and seconds<maxdelay:
            time.sleep(2)
            seconds+=2
            
    if os.path.exists(done_backtesting_symbol_file):      
         print('found stop file:',done_backtesting_symbol_file,'after delay')
         return True   
     
    else:    
         return False
         
def send_symbol(sym):
        """wintitle=GetWindowText(GetForegroundWindow())
        window = pyautogui.getWindow(wintitle)
        if window:
            print('win:',wintitle)
            window.moveTo(100,200,9)
        else:
            print('no window found')"""
        "used winspy+"""
        print('initial position')
        """pyautogui.position() """
        """pyautogui.locateCenterOnScreen('looksLikeThis.png')"""
        
        print('target position')
        """pyautogui.position()"""    
        print('sending symbol '+sym+' of length ',len(sym))
        pyautogui.doubleClick(x=150,y=150)  #
        offset=0;
        if len(sym)>4:
            offset=1
        if len(sym)-6*offset==4:     #moves from true size to true size+6
            pyautogui.hotkey('delete',sym[0],sym[1],sym[2],sym[3],'enter')     #brings out cmd line in ts
        elif len(sym)-6*offset==3:
            pyautogui.hotkey('delete',sym[0],sym[1],sym[2],'enter')  
        elif len(sym)-6*offset==2:
            pyautogui.hotkey('delete',sym[0],sym[1],'enter')  
        elif len(sym)-6*offset==1:
            pyautogui.hotkey('delete',sym[0],'enter')  
        time.sleep(1)
        #pyautogui.typewrite(sym,2)
        #pyautogui.hotkey('enter')
        time.sleep(2)
        
def process_portfolio(index):
    with open(symbolsfile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        symbol_count = 0
        
        for row in csv_reader:
            symbol=row[0]
            Timeout=update_ts_chart_symbol(symbol,index)
            if Timeout:
                print('Success processing symbol', symbol)
            else:
                print('Problem Processing symbol. try again', symbol)
                #send_symbol(symbol)               
            symbol_count += 1   
        print('Al symbols processed'); 
        pyautogui.doubleClick(r)  #click outside text box at end of every iteration  
        
