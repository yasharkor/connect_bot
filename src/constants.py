from types import SimpleNamespace

from utils import create_keyboard

KEYS = SimpleNamespace(**dict(
    random_connect=':bust_in_silhouette: Connect',
    settings=':gear: Settings'
))
KEYBOARDS = SimpleNamespace(**dict(
    main=create_keyboard([KEYS.random_connect, KEYS.settings])
))
