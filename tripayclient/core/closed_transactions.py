from typing import Optional, List
import httpx
import attrs
import json
from tripayclient.core.exceptions import FailedListingTransactionsError, FailedCreateTransactionsError, \
    FailedGetDetailTransaction


@attrs.define
class ClosedTransactions:
    """
    Class For Transaction
    """
    api_key: str
    url: str
    signature: Optional[str] = None

    async def listing(self, page: Optional[int] = None, per_page: Optional[int] = None):
        """
        Listing Transaction
        """
        payloads = {
            "page": page if page is not None else 1,
            "per_page": per_page if per_page is not None else 5
        }

        headers = {
            "Authorization": "Bearer " + self.api_key
        }

        try:
            req = httpx.get(
                self.url, params=payloads, headers=headers
            )

            return json.dumps(req.text)
        except Exception as e:
            FailedListingTransactionsError(str(e))



    async def create(self, payload: dict, order_items: List[dict]
                                  ):

        """
        Method for create closed transactions
        exp payloads:
        {
            'method': 'BRIVA',
            'merchant_ref': merchant_ref,
            'amount': amount,
            'customer_name': 'Nama Pelanggan',
            'customer_email': 'emailpelanggan@domain.com',
            'customer_phone': '081234567890',
            'return_url': 'https://domainanda.com/redirect',
            'expired_time': expiry,
            'signature': signature
        }

        exp order_items:
        [
            {
              'sku': 'PRODUK1',
              'name': 'Nama Produk 1',
              'price': 500000,
              'quantity': 1,
              'product_url': 'https://tokokamu.com/product/nama-produk-1',
              'image_url': 'https://tokokamu.com/product/nama-produk-1.jpg'
            },
            {
              'sku': 'PRODUK2',
              'name': 'Nama Produk 2',
              'price': 500000,
              'quantity': 1,
              'product_url': 'https://tokokamu.com/product/nama-produk-2',
              'image_url': 'https://tokokamu.com/product/nama-produk-2.jpg'
            }
          ]
        """
        payload["signature"] = self.signature if self.signature is not None else None
        i = 0
        for item in order_items:
            for k in item:
                payload['order_items[' + str(i) + '][' + str(k) + ']'] = item[k]
            i += 1

        headers = {"Authorization": "Bearer " + self.api_key}
        try:
            req = httpx.post(url=self.url+"transaction/create", data=payload, headers=headers)

            return json.dumps(req.text)
        except Exception as e:

            raise FailedCreateTransactionsError(str(e))

    async def detail(self, payload: dict):
        """
        Method for detail closed transaction
        exp payload
        { "reference": "T0001000000000000006" }
        """

        headers = {
            "Authorization": "Bearer "+self.api_key
        }

        try:
            req = httpx.get(
                self.url+'/api/transaction/detail', params=payload, headers=headers
            )

            return json.dumps(req.text)
        except Exception as e:
            FailedGetDetailTransaction(str(e))



