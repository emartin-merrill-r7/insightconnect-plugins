# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Retrieve detailed information associated with a given indicator"


class Input:
    ID = "id"
    WITH = "with"
    

class Output:
    DATA = "data"
    

class GetIndicatorInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "id": {
      "type": "integer",
      "title": "Indicator ID",
      "description": "The ID of the requested indicator",
      "order": 1
    },
    "with": {
      "type": "array",
      "title": "With",
      "description": "The classes of items related to the indicator to return. e.g. ['adversaries', 'attachments']",
      "items": {
        "type": "string"
      },
      "order": 2
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetIndicatorOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "data": {
      "type": "object",
      "title": "Data",
      "description": "The properties of the indicator",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
