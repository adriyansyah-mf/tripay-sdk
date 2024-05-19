import attrs
import hmac
import hashlib

@attrs.define
class Auth:
    """ Class for Authentication to call API
    """
    privateKey : str
    apiKey: str


    async def get_signature(self, merchant_code: str, merchat_ref: str, amount: int) -> str:
        """Method to get signature

        Args:
            merchant_code (str): Code Your Merchant
            merchat_ref (str): merchant referal
            amount (int): amount transaction

        Returns:
            str: signature
        """

        signStr = "{}{}{}".format(merchant_code, merchat_ref, amount)
        
        return hmac.new(bytes(self.privateKey,'latin-1'), bytes(signStr,'latin-1'), hashlib.sha256).hexdigest()
    
    