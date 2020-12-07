import csv

import os.path
import os
import time
import pyautogui
from datetime import datetime
import backtestmodule
done_backtesting_symbol_file='c://users/irod/documents/python/backtest automator/donebacktesting.txt'
#symbolsfile='c://users/irod/documents/python/backtest automator/symbolsIndex.csv'
symbolsfile='c://users/irod/documents/python/backtest automator/symbolsportfolioMixedTrend.csv'
#symbolsfile='c://users/irod/documents/python/backtest automator/symbolsportfolioUptrend.csv'
#symbolsfile='c://users/irod/documents/python/backtest automator/symbolsportfolioDowntrend.csv'
#symbolsfile='c://users/irod/documents/python/backtest automator/symbols2winlose.csv'
#symbolsfile='c://users/irod/documents/python/backtest automator/symbolswinners.csv'
#symbolsfile='c://users/irod/documents/python/backtest automator/symbolslosers.csv'
#symbolsfile='c://users/irod/documents/python/backtest automator/symbolsuncertain.csv'


def portfolio_automator(number):
    index=0
    #send dummy symbol to start..assumes bdummy symbol in workspace, not in list
    try:
        while index<number:
            index += 1
            backtestmodule.process_portfolio(index)
            print(index)
    except KeyboardInterrupt:   #type ctrl+c to stop
        pass        
    print('all iterations processed');
            
if __name__ == '__main__':
    time.sleep(2)
    recyclecount=75
    maxdelay=45
    r=pyautogui.locateCenterOnScreen('entersymbol.png')    
    print(r)
    now = datetime.now().time() # time object
    print("before =", now) 
    portfolio_automator(recyclecount)
    now = datetime.now().time() # time object
    print("after =", now) 
