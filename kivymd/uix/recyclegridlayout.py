"""
Components/RecycleGridLayout
============================

:class:`~kivy.uix.recyclegridlayout.RecycleGridLayout` class equivalent. Simplifies working
with some widget properties. For example:

GridLayout
----------

.. code-block::

    RecycleGridLayout:
        size_hint_y: None
        height: self.minimum_height

        canvas:
            Color:
                rgba: app.theme_cls.primary_color
            Rectangle:
                pos: self.pos
                size: self.size

MDRecycleGridLayout
------------

.. code-block::

    MDRecycleGridLayout:
        adaptive_height: True
        md_bg_color: app.theme_cls.primary_color

Available options are:
----------------------

- adaptive_height_
- adaptive_width_
- adaptive_size_

.. adaptive_height:
adaptive_height
---------------

.. code-block:: kv

    adaptive_height: True

Equivalent

.. code-block:: kv

    size_hint_y: None
    height: self.minimum_height

.. adaptive_width:
adaptive_width
--------------

.. code-block:: kv

    adaptive_width: True

Equivalent

.. code-block:: kv

    size_hint_x: None
    width: self.minimum_width

.. adaptive_size:
adaptive_size
-------------

.. code-block:: kv

    adaptive_size: True

Equivalent

.. code-block:: kv

    size_hint: None, None
    size: self.minimum_size
"""

from kivy.uix.recyclegridlayout import RecycleGridLayout

from kivymd.uix import MDAdaptiveWidget
from kivymd.uix.behaviors import DeclarativeBehavior


class MDRecycleGridLayout(
    DeclarativeBehavior, RecycleGridLayout, MDAdaptiveWidget
):
    pass
