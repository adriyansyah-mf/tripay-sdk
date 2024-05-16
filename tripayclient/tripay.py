from typing import Optional, List

import attrs
from tripayclient.core.auth import Auth
from tripayclient.core.open_transactions import OpenTransactions
from tripayclient.core.closed_transactions import ClosedTransactions
from tripayclient.core.instructions import Instructions
from tripayclient.core.calculator import Calculator
from tripayclient.schemas.channel_enum import ChannelTypeEnum, ModeEnum


@attrs.define
class Authentication:
    """
    Class For Authentication
    """
    private_key: str
    api_key: str

    async def get_signature(self,  merchant_code: str, merchat_ref: str, amount: int):
        """
        generate signature
        """

        return await Auth(self.private_key, self.api_key).get_signature(merchant_code, merchat_ref, amount)
    

@attrs.define
class Calculate:
    url: str
    api_key: str

    async def calc(self, channel: ChannelTypeEnum, amount: int):
        """
        Method for Calculate Fee Transaction
        """

        return await Calculator(self.url, self.api_key).Calculator(channel, amount)

@attrs.define(slots=False)
class Tripay:

    api_key: str
    private_key: str
    mode: ModeEnum

    def _get_url(self):
        return self.mode.value

    async def listing_transactions(self, page: Optional[int] = None, per_page: Optional[int] = None):
        """
        Listing Transactions
        """

        return await ClosedTransactions(self.api_key, self._get_url()).listing(page, per_page)

    async def create_closed_transaction(self,merchant_code: str, payload: dict, order_items: List[dict]):
        """
        Create Close Transaction
        """
        _signature = await Authentication(self.private_key, self.api_key).get_signature(
            merchant_code=merchant_code,
            merchat_ref=payload['merchant_ref'],
            amount=payload['amount']
        )

        payload['signature'] = _signature
        return await ClosedTransactions(
            self.api_key,
            self._get_url(),
            signature=_signature
        ).create(
            payload,
            order_items
        )

    async def detail_closed_transaction(self, payload: dict):
        """
        Getting detail from closed transaction
        """

        return await ClosedTransactions(
            self.api_key,
            self._get_url(),
        ).detail(
            payload
        )






