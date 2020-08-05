

bl_info = {
    "name": "Procedural Compute - API Client",
    "blender": (2, 80, 0),
    "category": "Object",
}


def register():
    from .core import register as register_core
    from .cfd import register as register_cfd
    register_core()
    register_cfd()


def unregister():
    from .core import unregister as unregister_core
    from .cfd import unregister as unregister_cfd
    unregister_core()
    unregister_cfd()


if __name__ == "__main__":
    from .core import register as register_core
    register_core()