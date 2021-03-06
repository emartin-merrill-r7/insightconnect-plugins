# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Create a Google document"


class Input:
    CONTENT = "content"
    TITLE = "title"
    

class Output:
    RESULT = "result"
    

class CreateDocumentInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "content": {
      "type": "string",
      "title": "Content",
      "description": "Document content",
      "order": 2
    },
    "title": {
      "type": "string",
      "title": "Title",
      "description": "Document Title",
      "order": 1
    }
  },
  "required": [
    "content",
    "title"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class CreateDocumentOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "result": {
      "$ref": "#/definitions/create_result",
      "title": "Result",
      "description": "Document creation result",
      "order": 1
    }
  },
  "required": [
    "result"
  ],
  "definitions": {
    "create_result": {
      "type": "object",
      "title": "create_result",
      "properties": {
        "documentId": {
          "type": "string",
          "title": "Document ID",
          "description": "Document ID",
          "order": 2
        },
        "replies": {
          "type": "array",
          "title": "Replies",
          "description": "Replies",
          "items": {
            "type": "object"
          },
          "order": 3
        },
        "writeControl": {
          "type": "object",
          "title": "Write Control",
          "description": "Write control",
          "order": 1
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
