# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 12:55:44 2020

@author: irod
"""
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

done_backtesting_symbol_file='c://users/irod/documents/python/backtest automator/backtest project1/backtestAutomator/donebacktesting.txt'
#symbolsfile='c://users/irod/documents/python/backtest automator/symbolsIndex.csv'

symbolsfile='c://users/irod/documents/python/backtest automator/backtest project1/backtestAutomator/symbolsportfolioMixedTrend.csv'

#symbolsfile='c://users/irod/documents/python/backtest automator/backtest project1/backtestAutomator/goodandbadsymbols.csv'

entersymboltextboxfile='c://users/irod/documents/python/backtest automator/backtest project1/backtestAutomator/entersymbol.png'
#symbolsfile='c://users/irod/documents/python/backtest automator/symbolsportfolioUptrend.csv'
#symbolsfile='c://users/irod/documents/python/backtest automator/symbolsportfolioDowntrend.csv'
#symbolsfile='c://users/irod/documents/python/backtest automator/symbols2winlose.csv'
#symbolsfile='c://users/irod/documents/python/backtest automator/symbolswinners.csv'
#symbolsfile='c://users/irod/documents/python/backtest automator/symbolslosers.csv'
#symbolsfile='c://users/irod/documents/python/backtest automator/symbolsuncertain.csv'

class backtest:
    def update_ts_chart_symbol(sym,index):
        maxdelay=45
        print('serach for stop file:',done_backtesting_symbol_file,'after delay')
        if os.path.exists(done_backtesting_symbol_file):    
            backtest.send_symbol(sym)
            time.sleep(2)
            os.remove(done_backtesting_symbol_file)
            return True
        else:
            seconds=0
            """this makes backtesting dynamic in duration"""
            while not os.path.exists(done_backtesting_symbol_file) and seconds<maxdelay:
                time.sleep(2)
                seconds+=2
            #done file foiund by now, send next symbol     
            if os.path.exists(done_backtesting_symbol_file):      
                print('found stop file:',done_backtesting_symbol_file,'after delay')    
                backtest.send_symbol(sym)
                time.sleep(2)
                #remove dne file so we wait until next symbik has been processed
                os.remove(done_backtesting_symbol_file)
                return True   
             
            else:    
                 return False
             
    def send_symbol(sym):
            print('initial position')

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
            #pyautogui.typewrite(sym,2)
            #pyautogui.hotkey('enter')
            time.sleep(2)

            
#self needed es enry point into backtest class   from class main         
    def process_portfolio(self,index):
        #r=pyautogui.locateCenterOnScreen(entersymboltextboxfile)  
        with open(symbolsfile) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            symbol_count = 0
            
            for row in csv_reader:
                symbol=row[0]
                #pyautogui.doubleClick(r)  #click outside text box at end of every iteration  
                Timeout=backtest.update_ts_chart_symbol(symbol,index)
                if Timeout:
                    print('Success processing symbol', symbol)
                else:
                    print('Problem Processing symbol. try again with DISTINCT dummy symbol, to trigger new bacjtest  in ts, then skip', "J")
                    backtest.send_symbol("J")            
                symbol_count += 1   
                time.sleep(1)
                
            print('Al symbols processed');   
            r=pyautogui.locateCenterOnScreen(entersymboltextboxfile)  
            print(r)              
            pyautogui.doubleClick(r)  #click outside text box at end of every iteration  
            time.sleep(1)
    
