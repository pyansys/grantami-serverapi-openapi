"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from enum import Enum


class GsaCriterionType(Enum):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Allowed Enum values
    """
    BOOLEAN = "boolean"
    TEXT = "text"
    TEXTPREFIX = "textPrefix"
    RECORDLISTMEMBER = "recordListMember"
    RECORDPROPERTY = "recordProperty"
    REFERENCE = "reference"
    RECORDANCESTOR = "recordAncestor"
    RECORDANCESTORHISTORY = "recordAncestorHistory"
    SUBSET = "subset"
    TABULARLINKINGVALUE = "tabularLinkingValue"
    ATTRIBUTE = "attribute"
    LOCALCOLUMN = "localColumn"
    NAMEDCRITERION = "namedCriterion"