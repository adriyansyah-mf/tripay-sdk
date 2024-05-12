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

    async def __call__(self,  channel = ChannelTypeEnum) -> str:
        """Getting Instruction For Payment

        Returns:
            str: Detailed to pay 
        """
        print(channel)
        payload = {
            "code": channel.value
        }
        try:
            headers = {
                "Authorization": "Bearer " + self.api_key
            }
            print(self.mode.value+"payment/instruction")
            req = httpx.get(
                self.mode.value+"payment/instruction", params=payload, headers=headers
            )
            
            return req.text
        except Exception as e:
            print("masuk sini")
            raise FailedGetInstructionsError(str(e))
        
