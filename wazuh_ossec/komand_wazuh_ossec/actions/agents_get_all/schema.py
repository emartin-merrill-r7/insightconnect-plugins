# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Returns a list with the available agents"


class Input:
    LIMIT = "limit"
    OFFSET = "offset"
    SEARCH = "search"
    SORT = "sort"
    STATUS = "status"
    

class Output:
    AGENTS = "agents"
    ERROR = "error"
    TOTALITEMS = "totalItems"
    

class AgentsGetAllInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "limit": {
      "type": "integer",
      "title": "Limit",
      "description": "Maximum number of elements to return",
      "order": 2
    },
    "offset": {
      "type": "integer",
      "title": "Offset",
      "description": "First element to return in the collection",
      "order": 1
    },
    "search": {
      "type": "string",
      "title": "Search",
      "description": "Looks for elements with the specified string",
      "order": 4
    },
    "sort": {
      "type": "string",
      "title": "Sort",
      "description": "Sorts the collection by a field or fields (separated by comma). Use +/- at the beginning to ascending or descending order. Allowed sort fields are status, ip, id, and name",
      "order": 3
    },
    "status": {
      "type": "string",
      "title": "Status",
      "description": "Filters by agent status",
      "enum": [
        "All",
        "Active",
        "Never Connected",
        "Disconnected"
      ],
      "order": 5
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class AgentsGetAllOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "agents": {
      "type": "array",
      "title": "Agents",
      "description": "List of Agents",
      "items": {
        "$ref": "#/definitions/agents"
      },
      "order": 2
    },
    "error": {
      "type": "integer",
      "title": "Error",
      "description": "Error code",
      "order": 3
    },
    "totalItems": {
      "type": "integer",
      "title": "Total Items",
      "description": "Total items",
      "order": 1
    }
  },
  "required": [
    "agents",
    "error",
    "totalItems"
  ],
  "definitions": {
    "agents": {
      "type": "object",
      "title": "agents",
      "properties": {
        "id": {
          "type": "string",
          "title": "Agent ID",
          "description": "Agent ID",
          "order": 1
        },
        "ip": {
          "type": "string",
          "title": "Agent IP",
          "description": "Agent IP",
          "order": 2
        },
        "name": {
          "type": "string",
          "title": "Agent Name",
          "description": "Agent Name",
          "order": 3
        },
        "status": {
          "type": "string",
          "title": "Agent Status",
          "description": "Agent Status",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
