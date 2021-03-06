# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Isolate a machine from the network, but keep the connection to Windows ATP open"


class Input:
    COMMENT = "comment"
    ISOLATION_TYPE = "isolation_type"
    MACHINE_ID = "machine_id"
    

class Output:
    MACHINE_ISOLATION_RESPONSE = "machine_isolation_response"
    

class IsolateMachineInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "comment": {
      "type": "string",
      "title": "Comment",
      "description": "Comment to associate with the isolation action",
      "order": 3
    },
    "isolation_type": {
      "type": "string",
      "title": "Isolation Type",
      "description": "Type of isolation to perform on target machine",
      "enum": [
        "Full",
        "Selective"
      ],
      "order": 2
    },
    "machine_id": {
      "type": "string",
      "title": "Machine ID",
      "description": "Machine ID",
      "order": 1
    }
  },
  "required": [
    "comment",
    "isolation_type",
    "machine_id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class IsolateMachineOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "machine_isolation_response": {
      "$ref": "#/definitions/machine_action_response",
      "title": "Machine Action Response",
      "description": "A response that includes the result of the action, and supplemental information about the action taken",
      "order": 1
    }
  },
  "required": [
    "machine_isolation_response"
  ],
  "definitions": {
    "machine_action_response": {
      "type": "object",
      "title": "machine_action_response",
      "properties": {
        "@odata.context": {
          "type": "string",
          "title": "OData Context",
          "description": "OData Context",
          "order": 5
        },
        "creationDateTimeUtc": {
          "type": "string",
          "title": "Creation Date Time UTC",
          "description": "Date and time this request was created",
          "order": 2
        },
        "error": {
          "type": "string",
          "title": "Error",
          "description": "Error associated with this action",
          "order": 7
        },
        "id": {
          "type": "string",
          "title": "ID",
          "description": "ID",
          "order": 9
        },
        "lastUpdateTimeUtc": {
          "type": "string",
          "title": "Last Update Time UTC",
          "description": "Last Update for this requested action",
          "order": 4
        },
        "machineId": {
          "type": "string",
          "title": "Machine ID",
          "description": "Machine ID this request was taken on",
          "order": 3
        },
        "requestor": {
          "type": "string",
          "title": "Requestor",
          "description": "User associated with this action",
          "order": 6
        },
        "requestorComment": {
          "type": "string",
          "title": "Requestor Comment",
          "description": "Comment associated with this action",
          "order": 10
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Isolation action status",
          "order": 1
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type of action",
          "order": 8
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
