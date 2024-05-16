import json
from typing import Optional

import attrs
import httpx

from tripayclient.core.exceptions import FailedCreateTransactionsError, FailedGetDetailTransaction, \
    FailedListingTransactionsError


@attrs.define
class OpenTransactions:
    """
    Class for open transactions
    Open Transactions is not support Sandbox Mode
    """
    api_key: str
    signature: Optional[str] = None
    
    async def create(self, payload: dict):
        """
        Method for create open transactions
        exp payload:
        {
            'method': method,
            'merchant_ref': merchant_ref,
            'customer_name': 'Nama Pelanggan',
            'signature': signature
        }
        """
        headers = {
            "Authorization": "Bearer " + self.api_key
        }

        try:
            req = httpx.post(
                "https://tripay.co.id/api/open-payment/create", data=payload, headers=headers
            )

            return json.dumps(req.text)

        except Exception as e:
            raise FailedCreateTransactionsError(str(e))


    async def detail(self, uuid: str):
        """
        detail open transaction
        """
        headers = {
            "Authorization": "Bearer " + self.api_key
        }

        try:
            req = httpx.get("https://tripay.co.id/api/open-payment/" + uuid + "/detail" , headers=headers)
            return json.dumps(req.text)
        except Exception as e:
            raise FailedGetDetailTransaction(str(e))

    async def listing_payment(self, uuid: str):
        """
        Method for listing payment open transaction
        """
        headers = {
            "Authorization": "Bearer " + self.api_key
        }

        try:
            req = httpx.get(url="https://tripay.co.id/api/open-payment/" + uuid + "/transactions", headers=headers)

            return json.dumps(req.text)
        except Exception as e:
            raise FailedListingTransactionsError(str(e))

