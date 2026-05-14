#!/usr/bin/env python3
"""Module demonstrating mixins."""


class SwimMixin:
    """Mixin providing swimming behavior."""

    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin providing flying behavior."""

    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class using mixins."""

    def roar(self):
        """Print roaring behavior."""
        print("The dragon roars!")
