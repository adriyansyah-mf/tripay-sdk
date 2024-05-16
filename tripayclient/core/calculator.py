import json

import attrs
import httpx

from tripayclient.core.exceptions import FailedCalculateFeeError
from tripayclient.schemas.channel_enum import ChannelTypeEnum


@attrs.define
class Calculator:

    url: str
    api_key: str

    async def Calculator(self, channel: ChannelTypeEnum, amount: int):
        """
        Method For Calculate Fee Transaction
        """
        headers = {
            "Authorization" : "Bearer "+ self.api_key
        }
        payloads = {
            "code": channel.value,
            "amount": amount
        }
        try:
            req = httpx.get(
                self.url, headers=headers, params=payloads
            )

            return json.dumps(req.text)
        except Exception as e:
            FailedCalculateFeeError(str(e))