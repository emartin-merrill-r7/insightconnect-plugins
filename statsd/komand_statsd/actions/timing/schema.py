# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "This action is used to record timer information"


class Input:
    DELTA = "delta"
    RATE = "rate"
    STAT = "stat"
    

class Output:
    DELTA = "delta"
    STAT = "stat"
    

class TimingInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "delta": {
      "type": "integer",
      "title": "Delta value",
      "description": "The number of milliseconds whatever action took",
      "order": 2
    },
    "rate": {
      "type": "number",
      "title": "Sample rate",
      "description": "A sample rate e.g. 1. Default is 1",
      "order": 3
    },
    "stat": {
      "type": "string",
      "title": "Timer name",
      "description": "The name of the timer to use",
      "order": 1
    }
  },
  "required": [
    "delta",
    "stat"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class TimingOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "delta": {
      "type": "integer",
      "title": "Delta",
      "description": "The number of milliseconds whatever action took",
      "order": 2
    },
    "stat": {
      "type": "string",
      "title": "Stat",
      "description": "The name of the used timer",
      "order": 1
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
