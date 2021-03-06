# GENERATED BY KOMAND SDK - DO NOT EDIT
import komand
import json


class Component:
    DESCRIPTION = "Search the database to find vulnerabilities and exploits"


class Input:
    DATABASE = "database"
    SEARCH = "search"
    

class Output:
    RESULTS_FOUND = "results_found"
    SEARCH_RESULTS = "search_results"
    

class SearchDbInput(komand.Input):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "database": {
      "type": "string",
      "title": "Database",
      "description": "Name of the database",
      "default": "All",
      "enum": [
        "Vulnerability Database",
        "Metasploit Modules",
        "All"
      ],
      "order": 1
    },
    "search": {
      "type": "string",
      "title": "Search",
      "description": "Search parameter for database",
      "order": 2
    }
  },
  "required": [
    "database",
    "search"
  ]
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)


class SearchDbOutput(komand.Output):
    schema = json.loads("""
   {
  "type": "object",
  "title": "Variables",
  "properties": {
    "results_found": {
      "type": "boolean",
      "title": "Results Found",
      "description": "Will return false if no results are found",
      "order": 2
    },
    "search_results": {
      "type": "array",
      "title": "Vulnerability",
      "description": "Vulnerability and exploits found",
      "items": {
        "$ref": "#/definitions/vuln_found"
      },
      "order": 1
    }
  },
  "required": [
    "results_found"
  ],
  "definitions": {
    "vuln_found": {
      "type": "object",
      "title": "vuln_found",
      "properties": {
        "history": {
          "type": "string",
          "title": "Metasploit History",
          "description": "The history of the Metasploit module",
          "order": 12
        },
        "link": {
          "type": "string",
          "title": "Link",
          "description": "Link to vulnerability",
          "order": 2
        },
        "module": {
          "type": "string",
          "title": "Metasploit Module",
          "description": "Path to Metasploit module",
          "order": 7
        },
        "module_name": {
          "type": "string",
          "title": "Metasploit Module Name",
          "description": "The name of the Metasploit module",
          "order": 9
        },
        "module_options": {
          "type": "string",
          "title": "Metasploit Module Options",
          "description": "The options offered for the Metasploit module",
          "order": 8
        },
        "name": {
          "type": "string",
          "title": "Name",
          "description": "Name of vulnerability",
          "order": 1
        },
        "published": {
          "type": "string",
          "title": "Published",
          "description": "Published date of vulnerability",
          "order": 6
        },
        "reliability": {
          "type": "string",
          "title": "Reliability of Metasploit Module",
          "description": "The reliability of running a Metasploit module",
          "order": 10
        },
        "severity": {
          "type": "string",
          "title": "Severity",
          "description": "Severity of vulnerability",
          "order": 3
        },
        "source_code": {
          "type": "string",
          "title": "Source Code",
          "description": "Source code of Metasploit module",
          "order": 11
        },
        "summary": {
          "type": "string",
          "title": "Summary",
          "description": "Brief summary of vulnerability",
          "order": 5
        },
        "type": {
          "type": "string",
          "title": "Type",
          "description": "Type of vulnerability",
          "order": 4
        }
      }
    }
  }
}
    """)

    def __init__(self):
        super(self.__class__, self).__init__(self.schema)
