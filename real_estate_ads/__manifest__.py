{
    "name": "Real EState Ads",
    "description": """
        Real Estate Module to show available properties
    """,
    "version": "1.0",
    "website": "www.ccbm.sn",
    "category": "Sales",
    "author": "CCBM-DEV",
    "depends": [],
    "data": [
        'security/ir.model.access.csv',
        'views/property_view.xml',
        'views/property_type_view.xml',
        'views/property_tag_view.xml',
        'views/menu_items.xml',

        # Data Files
        'data/property_type.xml',
        'data/estate.property.type.csv'
    ],
    "installable": True,
    "application": True,
    "license": "LGPL-3"
}