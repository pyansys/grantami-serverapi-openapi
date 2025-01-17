# Copyright (C) 2023 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
    MI Server API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import re  # noqa: F401
from typing import TYPE_CHECKING, Any, Dict, List, Optional  # noqa: F401

from . import ModelBase

if TYPE_CHECKING:
    from . import *


class GrantaServerApiObjectIdentifier(ModelBase):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes
    ----------
    swagger_types: Dict[str, str]
        The key is attribute name and the value is attribute type.
    attribute_map: Dict[str, str]
        The key is attribute name and the value is json key in definition.
    subtype_mapping: Dict[str, str]
        The key is the unmangled property name and the value is the corresponding type.
    discriminator: Optional[str]
        Name of the property used as discriminator for subtypes.
    """
    swagger_types = {
        "guid": "str",
        "identity": "int",
        "name": "str",
    }

    attribute_map = {
        "guid": "guid",
        "identity": "identity",
        "name": "name",
    }

    subtype_mapping = {}

    discriminator = None

    def __init__(
        self,
        *,
        guid: "Optional[str]" = None,
        identity: "Optional[int]" = None,
        name: "Optional[str]" = None,
    ) -> None:
        """GrantaServerApiObjectIdentifier - a model defined in Swagger

        Parameters
        ----------
            guid: str, optional
            identity: int, optional
            name: str, optional
        """
        self._guid = None
        self._name = None
        self._identity = None

        if guid is not None:
            self.guid = guid
        if name is not None:
            self.name = name
        if identity is not None:
            self.identity = identity

    @property
    def guid(self) -> "str":
        """Gets the guid of this GrantaServerApiObjectIdentifier.
        The GUID of this object. The GUID represents the object on a semantic level, and two objects of  the same type with the same GUID are considered to represent \"the same concept\". GUIDs should be  robust against data changes and database upgrades, and should be preferred where possible.

        Returns
        -------
        str
            The guid of this GrantaServerApiObjectIdentifier.
        """
        return self._guid

    @guid.setter
    def guid(self, guid: "str") -> None:
        """Sets the guid of this GrantaServerApiObjectIdentifier.
        The GUID of this object. The GUID represents the object on a semantic level, and two objects of  the same type with the same GUID are considered to represent \"the same concept\". GUIDs should be  robust against data changes and database upgrades, and should be preferred where possible.

        Parameters
        ----------
        guid: str
            The guid of this GrantaServerApiObjectIdentifier.
        """
        self._guid = guid

    @property
    def name(self) -> "str":
        """Gets the name of this GrantaServerApiObjectIdentifier.
        The name of this object. The name represents the object at a human-readable level, but two objects of  the same type with the same need not represent \"the same concept\". Because the name is less uniquely identifying,  clients should prefer GUIDs where possible, and operations based on name instead of GUID may fail if the name  cannot be uniquely resolved. Certain object types may consider names to be equivalent

        Returns
        -------
        str
            The name of this GrantaServerApiObjectIdentifier.
        """
        return self._name

    @name.setter
    def name(self, name: "str") -> None:
        """Sets the name of this GrantaServerApiObjectIdentifier.
        The name of this object. The name represents the object at a human-readable level, but two objects of  the same type with the same need not represent \"the same concept\". Because the name is less uniquely identifying,  clients should prefer GUIDs where possible, and operations based on name instead of GUID may fail if the name  cannot be uniquely resolved. Certain object types may consider names to be equivalent

        Parameters
        ----------
        name: str
            The name of this GrantaServerApiObjectIdentifier.
        """
        self._name = name

    @property
    def identity(self) -> "int":
        """Gets the identity of this GrantaServerApiObjectIdentifier.
        The underlying identity of this object. This represents the object at a data level, and two objects  of the same type with the same identity are considered to represent \"the same object\". However, identities  are not robust against database upgrades, and are only reliable and consistent within a currently-  loaded database in a running MI instance. Clients should prefer GUIDs where possible, and operations  based on identity which persist data will be resolved to GUIDs instead (and may fail if this cannot  be done).

        Returns
        -------
        int
            The identity of this GrantaServerApiObjectIdentifier.
        """
        return self._identity

    @identity.setter
    def identity(self, identity: "int") -> None:
        """Sets the identity of this GrantaServerApiObjectIdentifier.
        The underlying identity of this object. This represents the object at a data level, and two objects  of the same type with the same identity are considered to represent \"the same object\". However, identities  are not robust against database upgrades, and are only reliable and consistent within a currently-  loaded database in a running MI instance. Clients should prefer GUIDs where possible, and operations  based on identity which persist data will be resolved to GUIDs instead (and may fail if this cannot  be done).

        Parameters
        ----------
        identity: int
            The identity of this GrantaServerApiObjectIdentifier.
        """
        self._identity = identity

    @classmethod
    def get_real_child_model(cls, data: ModelBase) -> str:
        """Raises a NotImplementedError for a type without a discriminator defined.

        Parameters
        ----------
        data: ModelBase
            Object representing a subclass of this class

        Raises
        ------
        NotImplementedError
            This class has no discriminator, and hence no subclasses
        """
        raise NotImplementedError()

    def __repr__(self) -> str:
        """For 'print' and 'pprint'"""
        return self.to_str()

    def __eq__(self, other: Any) -> bool:
        """Returns true if both objects are equal"""
        if not isinstance(other, GrantaServerApiObjectIdentifier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other: Any) -> bool:
        """Returns true if both objects are not equal"""
        return not self == other
