# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Retrieve an issue"


class Input:
    GET_ATTACHMENTS = "get_attachments"
    ID = "id"
    

class Output:
    FOUND = "found"
    ISSUE = "issue"
    

class GetIssueInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "get_attachments": {
      "type": "boolean",
      "title": "Get Attachments",
      "description": "Get attachments from issue",
      "default": false,
      "order": 2
    },
    "id": {
      "type": "string",
      "title": "ID",
      "description": "Issue ID",
      "order": 1
    }
  },
  "required": [
    "id"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class GetIssueOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "found": {
      "type": "boolean",
      "title": "Found",
      "description": "True if found",
      "order": 1
    },
    "issue": {
      "$ref": "#/definitions/issue",
      "title": "Issue",
      "description": "Issue",
      "order": 2
    }
  },
  "definitions": {
    "file": {
      "id": "file",
      "type": "object",
      "title": "File",
      "description": "File Object",
      "properties": {
        "content": {
          "type": "string",
          "title": "Content",
          "description": "File contents",
          "format": "bytes"
        },
        "filename": {
          "type": "string",
          "title": "Filename",
          "description": "Name of file"
        }
      }
    },
    "issue": {
      "type": "object",
      "title": "issue",
      "properties": {
        "assignee": {
          "type": "string",
          "title": "Assignee",
          "description": "Assigned User",
          "order": 11
        },
        "attachments": {
          "type": "array",
          "title": "Attachments",
          "description": "Attachments",
          "items": {
            "$ref": "#/definitions/file"
          },
          "order": 15
        },
        "created_at": {
          "type": "string",
          "title": "Created At",
          "description": "Created At",
          "order": 12
        },
        "description": {
          "type": "string",
          "title": "Description",
          "description": "Description",
          "order": 7
        },
        "fields": {
          "type": "object",
          "title": "Fields",
          "description": "Full list of fields",
          "order": 16
        },
        "id": {
          "type": "string",
          "title": "Id",
          "description": "Issue ID",
          "order": 1
        },
        "key": {
          "type": "string",
          "title": "Key",
          "description": "Issue Key",
          "order": 3
        },
        "labels": {
          "type": "array",
          "title": "Labels",
          "description": "Labels",
          "items": {
            "type": "string"
          },
          "order": 9
        },
        "project": {
          "type": "string",
          "title": "Project",
          "description": "Project",
          "order": 2
        },
        "reporter": {
          "type": "string",
          "title": "Reporter",
          "description": "Reporting User",
          "order": 10
        },
        "resolution": {
          "type": "string",
          "title": "Resolution",
          "description": "Resolution",
          "order": 8
        },
        "resolved_at": {
          "type": "string",
          "title": "Resolved At",
          "description": "Resolved At",
          "order": 14
        },
        "status": {
          "type": "string",
          "title": "Status",
          "description": "Status",
          "order": 4
        },
        "summary": {
          "type": "string",
          "title": "Summary",
          "description": "Summary",
          "order": 6
        },
        "updated_at": {
          "type": "string",
          "title": "Updated At",
          "description": "Updated At",
          "order": 13
        },
        "url": {
          "type": "string",
          "title": "Url",
          "description": "Issue URL",
          "order": 5
        }
      },
      "definitions": {
        "file": {
          "id": "file",
          "type": "object",
          "title": "File",
          "description": "File Object",
          "properties": {
            "content": {
              "type": "string",
              "title": "Content",
              "description": "File contents",
              "format": "bytes"
            },
            "filename": {
              "type": "string",
              "title": "Filename",
              "description": "Name of file"
            }
          }
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
