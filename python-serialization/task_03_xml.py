#!/usr/bin/env python3
"""
Module for serializing and deserializing Python dictionaries using XML.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The filename to save the XML data.
    """
    root = ET.Element("data")  # Create root element

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)  # Create child element for each key
        child.text = str(value)  # Convert value to string

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.

    Args:
        filename (str): The XML file to read.

    Returns:
        dict: The deserialized dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}

        for child in root:
            result[child.tag] = child.text  # Values will be strings
        return result
    except Exception:
        return None
