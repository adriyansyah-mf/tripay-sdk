import pytest
from unittest.mock import AsyncMock, patch
from tripayclient.tripay import Tripay
from tripayclient.schemas.channel_enum import ModeEnum

@pytest.mark.asyncio
async def test_closed_transaction():
    private_key = "Z8Wo7-bLjeA-TrQZL-ZzL2v-UTPq5"
    api_key = "DEV-I6CNNeKNuWLq0G6oKS2kQwj8kVPfx7B6vvsXmtVy"
    merchant_code = "T000"

    payload = {
        'method': 'BRIVA',
        'merchant_ref': "INV0002",
        'amount': 5000,
        'customer_name': 'Nama Pelanggan',
        'customer_email': 'emailpelanggan@domain.com',
        'customer_phone': '081234567890',
        'return_url': 'https://domainanda.com/redirect',
        'expired_time': 1721375469,
    }

    order_items = [
        {
            'sku': 'PRODUK1',
            'name': 'Nama Produk 1',
            'price': 5000,
            'quantity': 1,
            'product_url': 'https://tokokamu.com/product/nama-produk-1',
            'image_url': 'https://tokokamu.com/product/nama-produk-1.jpg'
        }
    ]

    # Initialize the Tripay instance
    t = Tripay(
        api_key=api_key,
        private_key=private_key,
        mode=ModeEnum.sandbox
    )

    with patch('tripayclient.tripay.Authentication.get_signature', new_callable=AsyncMock) as mock_get_signature, \
         patch('tripayclient.tripay.ClosedTransactions.create', new_callable=AsyncMock) as mock_create:
        mock_get_signature.return_value = "mocked_signature"
        mock_create.return_value = {"status": "success"}

        # Call the method
        result = await t.ClosedTransaction.create(
            merchant_code,
            payload,
            order_items
        )


        # Assert the results
        assert result == {"status": "success"}
        mock_get_signature.assert_called_once_with(
            merchant_code=merchant_code,
            merchant_ref=payload['merchant_ref'],
            amount=payload['amount']
        )
        mock_create.assert_called_once_with(payload, order_items)

