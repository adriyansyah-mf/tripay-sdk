import asyncio
from tripayclient.core.auth import Auth
from tripayclient.schemas.channel_enum import ChannelTypeEnum, ModeEnum
from tripayclient.core.exceptions import FailedGetInstructionsError
import attrs
import httpx

@attrs.define
class Instructions:

    api_key: str
    mode: ModeEnum
    url: str

    async def __call__(self,  channel = ChannelTypeEnum) -> str:
        """Getting Instruction For Payment

        Returns:
            str: Detailed to pay 
        """
        payload = {
            "code": channel.value
        }
        try:
            headers = {
                "Authorization": "Bearer " + self.api_key
            }
            req = httpx.get(
                self.url+"payment/instruction", params=payload, headers=headers
            )
            
            return req.text
        except Exception as e:
            raise FailedGetInstructionsError(str(e))
        
