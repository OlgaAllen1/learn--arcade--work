def check_item_clicked(x, y, item):
    return item.left <= x <= item.right and item.bottom <= y <= item.top


def destroy_all_sprites(sprite_list):
    while len(sprite_list) > 0:
        sprite = sprite_list[0]
        sprite.remove_from_sprite_lists()
        sprite.kill()
