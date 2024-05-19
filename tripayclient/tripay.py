from typing import Optional, List
import attrs
from tripayclient.core.auth import Auth
from tripayclient.core.open_transactions import OpenTransactions
from tripayclient.core.closed_transactions import ClosedTransactions
from tripayclient.core.calculator import Calculator
from tripayclient.schemas.channel_enum import ChannelTypeEnum, ModeEnum


@attrs.define
class Authentication:
    """
    Class For Authentication
    """
    private_key: str
    api_key: str

    async def get_signature(self, merchant_code: str, merchant_ref: str, amount: int):
        """
        generate signature
        """

        return await Auth(self.private_key, self.api_key).get_signature(merchant_code, merchant_ref, amount)


@attrs.define
class OpenTransaction:
    """
    Class for Open Transaction
    """
    private_key: str
    api_key: str

    async def create(self, merchant_code: str, payload: dict):
        """
        Method for create open transaction
        """
        _signature = await Authentication(self.private_key, self.api_key).get_signature(
            merchant_code=merchant_code,
            merchant_ref=payload['merchant_ref'],
            amount=payload['amount']
        )

        return await OpenTransactions(
            api_key=self.api_key,
            signature=_signature
        ).create(
            payload
        )

    async def detail(self, uuid: str):
        """
        Method to get detail of transaction
        """

        return await OpenTransactions(
            self.api_key,
        ).detail(
            uuid
        )

    async def listing_payment(self, uuid: str):
        """
        Method for listing payment open transaction
        """

        return await OpenTransactions(
            self.api_key
        ).listing_payment(
            uuid
        )


@attrs.define
class ClosedTransaction:
    """
    Class for closed transaction
    """
    api_key: str
    private_key: str
    mode: ModeEnum

    @property
    def _get_url(self):
        return self.mode.value

    async def create(self, merchant_code: str, payload: dict, order_items: List[dict]):
        """
        Method for create transaction
        """
        _signature = await Authentication(self.private_key, self.api_key).get_signature(
            merchant_code=merchant_code,
            merchant_ref=payload['merchant_ref'],
            amount=payload['amount']
        )
        return await ClosedTransactions(
            self.api_key,
            self._get_url,
            signature=_signature
        ).create(
            payload,
            order_items
        )

    async def detail(self, payload: dict):
        """
        Getting detail from closed transaction
        """

        return await ClosedTransactions(
            self.api_key,
            self._get_url(),
        ).detail(
            payload
        )


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
    ClosedTransaction: ClosedTransaction = attrs.field(init=False)
    OpenTransaction: OpenTransaction = attrs.field(init=False)

    def __attrs_post_init__(self):
        self.ClosedTransaction = ClosedTransaction(self.api_key, self.private_key, self.mode)
        self.OpenTransaction = OpenTransaction(self.private_key, self.api_key)

    @property
    def _get_url(self):
        return self.mode.value

    async def listing_transactions(self, page: Optional[int] = None, per_page: Optional[int] = None):
        """
        Listing Transactions
        """

        return await ClosedTransactions(self.api_key, self._get_url).listing(page, per_page)
