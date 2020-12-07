import time
import os.path
from datetime import datetime
from backTestAutomator import backTestmodule

def portfolio_automator(number):
    index=0
    #send dummy symbol to start..assumes bdummy symbol in workspace, not in list
    try:
        while index<number:
            index += 1
            bt.process_portfolio(index)
            print(index)
    except KeyboardInterrupt:   #type ctrl+c to stop
        pass        
    print('all iterations processed')

 
if __name__ == '__main__':
    if os.path.exists(backTestmodule.done_backtesting_symbol_file):      
            print('clean up file if it exists on startup:',backTestmodule.done_backtesting_symbol_file)    
            #remove dne file so we wait until next symbik has been processed
            os.remove(backTestmodule.done_backtesting_symbol_file) 
            time.sleep(2)
    bt=backTestmodule.backtest() 
    time.sleep(2)
    recyclecount=75
    now = datetime.now().time() # time object
    print("before =", now) 
    portfolio_automator(recyclecount)
    now = datetime.now().time() # time object
    print("after =", now) 
