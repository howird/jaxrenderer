from collections.abc import Sequence
from typing import NamedTuple, ParamSpec, TypeAlias, TypeVar

from ._meta_utils import add_tracing_name
from ._meta_utils import typed_jit as jit
from .geometry import (
    Camera,
    normalise,
    quaternion,
    quaternion_mul,
    rotation_matrix,
)
from .model import Model, ModelObject, batch_models, merge_objects
from .pipeline import render
from .renderer import CameraParameters, LightParameters, Renderer, ShadowParameters
from .scene import GUID, Scene
from .shapes.capsule import UpAxis, create_capsule
from .shapes.cube import create_cube
from .types import (
    Buffers,
    Colour,
    JaxFloating,
    JaxInteger,
    LightSource,
    SpecularMap,
    Texture,
    Vec3f,
)
from .utils import build_texture_from_PyTinyrenderer, transpose_for_display

K = TypeVar("K")
V = TypeVar("V")
DictT: TypeAlias = dict[K, V]


def replace_dict(base: DictT[K, V], new: DictT[K, V]) -> DictT[K, V]:
    return base | new

__all__ = [
    "add_tracing_name",
    "batch_models",
    "Buffers",
    "build_texture_from_PyTinyrenderer",
    "Camera",
    "CameraParameters",
    "Colour",
    "create_capsule",
    "create_cube",
    "DictT",
    "GUID",
    "JaxFloating",
    "JaxInteger",
    "jit",
    "LightParameters",
    "LightSource",
    "merge_objects",
    "Model",
    "ModelObject",
    "NamedTuple",
    "normalise",
    "ParamSpec",
    "quaternion_mul",
    "quaternion",
    "render",
    "Renderer",
    "replace_dict",
    "rotation_matrix",
    "Scene",
    "Sequence",
    "ShadowParameters",
    "SpecularMap",
    "Texture",
    "transpose_for_display",
    "TypeAlias",
    "UpAxis",
    "Vec3f",
]
