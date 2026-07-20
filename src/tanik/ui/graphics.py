from tanik.engine import AssetId, AssetManager, Color


def load_assets(assets: AssetManager) -> None:
    assets.load(AssetId.PLAYER, "@", Color.YELLOW)
    assets.load(AssetId.WALL, "#", Color.GRAY)
    assets.load(AssetId.SMALL_ENEMY, "e", Color.RED)
    assets.load(AssetId.NORMAL_ENEMY, "E", Color.RED)
    assets.load(AssetId.FLOOR, ".", Color.GRAY)
