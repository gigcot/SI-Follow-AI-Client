from template.request_generator.base_request import BaseRequest
from user_defined_protocol.protocol import UserDefinedProtocolNumber


class LlamaAgentOperationRequest(BaseRequest):
    def __init__(self, **kwargs):
        self.__protocolNumber = UserDefinedProtocolNumber.LLaMA_AGENT_OPERATION.value
        self.parameterList = kwargs.get("data", [])

    def getProtocolNumber(self):
        return self.__protocolNumber

    def getParameterList(self):
        return tuple(self.parameterList)

    def toDictionary(self):
        return {
            "protocolNumber": self.__protocolNumber,
            "parameterList": self.parameterList,
        }

    def __str__(self):
        return f"LlamaGetFileListRequest(protocolNumber={self.__protocolNumber}, parameterList={self.parameterList})"
