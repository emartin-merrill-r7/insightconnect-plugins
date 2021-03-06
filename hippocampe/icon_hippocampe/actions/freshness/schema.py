# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Check if the feeds are up to date. A threshold can be defined in Hippocampe/core/conf/hippo/hippo.conf (by default 1 day)"


class Input:
    pass

class Output:
    FRESHNESS_STATUSES = "freshness_statuses"
    

class FreshnessInput(komand.Input):
    schema = json.loads("""
   {}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class FreshnessOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "freshness_statuses": {
      "type": "array",
      "title": "Freshness Statuses",
      "description": "List of all feeds with their freshness statuses",
      "items": {
        "$ref": "#/definitions/freshness_status"
      },
      "order": 1
    }
  },
  "required": [
    "freshness_statuses"
  ],
  "definitions": {
    "freshness_status": {
      "type": "object",
      "title": "freshness_status",
      "properties": {
        "feed": {
          "type": "string",
          "title": "Feed",
          "description": "Feed",
          "order": 1
        },
        "freshness": {
          "type": "string",
          "title": "Freshness",
          "description": "Freshness status",
          "order": 2
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
