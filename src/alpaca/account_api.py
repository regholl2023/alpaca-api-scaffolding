from alpaca.trading.client import TradingClient
import logging

# Not sure if this is required. Included in documentation.
from alpaca.trading.requests import GetAssetsRequest

logger = logging.getLogger()

class AlpacaAccountClient:
    def __init__(self, api_key, secret_key, base_url):
        self.client = TradingClient(api_key, secret_key, base_url)

    def get_account(self):
        """Returns the account."""
        try:
            account = self.client.get_account()
            # Check if our account is restricted from trading.
            if account.trading_blocked:
                print('Account is currently restricted from trading.')
            return account
        except Exception as e:
            logger.error(f"Error fetching user account: {e}")
        return None

    def get_cash_balance(self):
        """Returns the account's cash balance."""
        try:
            account = self.account()
            return account.cash
        except Exception as e:
            logger.error(f"Error fetching account cash: {e}")
        return None
    
    def get_buying_power(self):
        """Returns the account's buying power balance."""
        try:
            account = self.account()
            return account.buying_power
        except Exception as e:
            logger.error(f"Error fetching buying power: {e}")
        return None
    
    def get_balance_change(self):
        """Returns the account's current balance vs. balance at the last market close."""
        try:
            account = self.account()
            # Check our current balance vs. our balance at the last market close
            balance_change = float(account.equity) - float(account.last_equity)
            return balance_change
        except Exception as e:
            logger.error(f"Error fetching daily balance change power: {e}")
        return None
    
   