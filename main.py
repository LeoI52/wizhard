"""
@author : Léo Imbert & Yael Ennon
@created : 11/09/25
@updated : 04/10/25
"""

#? -------------------- IMPORTATIONS -------------------- ?#

import colorsys
import random
import pyxel
import math
import time

#? -------------------- UTILS -------------------- ?#

ANCHOR_TOP_LEFT = 0
ANCHOR_TOP_RIGHT = 1
ANCHOR_BOTTOM_LEFT = 2
ANCHOR_BOTTOM_RIGHT = 3
ANCHOR_LEFT = 4
ANCHOR_RIGHT = 5
ANCHOR_TOP = 6
ANCHOR_BOTTOM = 7
ANCHOR_CENTER = 8

BOTTOM = 0
TOP = 1
LEFT = 2
RIGHT = 3

class Transition:

    def __init__(self, new_scene_id:int, speed:int, transition_color:int, new_camera_x:int=0, new_camera_y:int=0, action=None):
        self.new_scene_id = new_scene_id
        self.speed = speed
        self.transition_color = transition_color
        self.new_camera_x = new_camera_x
        self.new_camera_y = new_camera_y
        self.action = action
        self.direction = 1

class TransitionRectangle(Transition):

    def __init__(self, new_scene_id:int, duration:float, transition_color:int, dir:int=LEFT, new_camera_x:int=0, new_camera_y:int=0, action=None, fps:int=60):
        speed = pyxel.width / (duration / 2 * fps) if dir in [LEFT, RIGHT] else pyxel.height / (duration / 2 * fps)
        super().__init__(new_scene_id, speed, transition_color, new_camera_x, new_camera_y, action)
        self.dir = dir
        self.w = 0
        self.x = pyxel.width if dir == RIGHT else 0
        self.y = pyxel.height if dir == BOTTOM else 0

    def update(self, pyxel_manager):
        if self.dir in [RIGHT, LEFT]:
            self.w += self.speed * self.direction

            if (self.direction == 1 and self.dir == RIGHT) or (self.direction == -1 and self.dir == LEFT):
                self.x = self.x - self.speed if self.dir == RIGHT else self.x + self.speed
            if self.w > pyxel.width and self.direction == 1:
                self.direction = -1
                pyxel_manager.change_scene(self.new_scene_id, self.new_camera_x, self.new_camera_y, self.action)
                self.x = 0
            if self.w < 0 and self.direction == -1:
                pyxel_manager.finish_transition()
                return
        elif self.dir in [TOP, BOTTOM]:
            self.w += self.speed * self.direction

            if (self.direction == 1 and self.dir == BOTTOM) or (self.direction == -1 and self.dir == TOP):
                self.y = self.y - self.speed if self.dir == BOTTOM else self.y + self.speed
            if self.w > pyxel.height and self.direction == 1:
                self.direction = -1
                pyxel_manager.change_scene(self.new_scene_id, self.new_camera_x, self.new_camera_y, self.action)
                self.y = 0
            if self.w < 0 and self.direction == -1:
                pyxel_manager.finish_transition()
                return

    def draw(self, pyxel_manager):
        if self.dir in [RIGHT, LEFT]:
            pyxel.rect(pyxel_manager.camera_x + self.x, pyxel_manager.camera_y, self.w, pyxel.height, self.transition_color)
        elif self.dir in [TOP, BOTTOM]:
            pyxel.rect(pyxel_manager.camera_x, pyxel_manager.camera_y + self.y, pyxel.width, self.w, self.transition_color)

class PyxelManager:

    def __init__(self, width:int, height:int, scenes:list, default_scene_id:int=0, fps:int=60, fullscreen:bool=False, mouse:bool=False, quit_key:int=pyxel.KEY_ESCAPE, camera_x:int=0, camera_y:int=0, debug_background_color:int=0, debug_text_color:int=7):
        
        self.__scenes_dict = {scene.id:scene for scene in scenes}
        self.__current_scene = self.__scenes_dict[default_scene_id]
        self.__transition = None

        self.__cam_x = self.__cam_tx = camera_x
        self.__cam_y = self.__cam_ty = camera_y
        self.__cam_bounds = (-float("inf"), -float("inf"), float("inf"), float("inf"))
        self.__shake_amount = 0
        self.__shake_decay = 0

        self.__flash = {}

        self.__fps = fps
        self.__previous_frame_time = time.time()
        self.__current_fps = 0

        self.debug = False
        self.debug_background_color = debug_background_color
        self.debug_text_color = debug_text_color

        pyxel.init(width, height, fps=fps, quit_key=quit_key)
        pyxel.fullscreen(fullscreen)
        pyxel.mouse(mouse)

        if self.__current_scene.pyxres_path:
            pyxel.load(self.__current_scene.pyxres_path)
        pyxel.title(self.__current_scene.title)
        pyxel.screen_mode(self.__current_scene.screen_mode)
        pyxel.colors.from_list(self.__current_scene.palette)

    @property
    def camera_x(self)-> int|float:
        return self.__cam_x
    
    @property
    def camera_y(self)-> int|float:
        return self.__cam_y

    @property
    def mouse_x(self)-> int:
        return self.__cam_x + pyxel.mouse_x
    
    @property
    def mouse_y(self)-> int:
        return self.__cam_y + pyxel.mouse_y
    
    def set_camera(self, new_camera_x:int, new_camera_y:int):
        self.__cam_x = self.__cam_tx = max(self.__cam_bounds[0], min(new_camera_x, self.__cam_bounds[2] - pyxel.width))
        self.__cam_y = self.__cam_ty = max(self.__cam_bounds[1], min(new_camera_y, self.__cam_bounds[3] - pyxel.height))

    def move_camera(self, new_camera_x:int, new_camera_y:int):
        self.__cam_tx = max(self.__cam_bounds[0], min(new_camera_x, self.__cam_bounds[2] - pyxel.width))
        self.__cam_ty = max(self.__cam_bounds[1], min(new_camera_y, self.__cam_bounds[3] - pyxel.height))

    def set_camera_bounds(self, min_x:int, min_y:int, max_x:int, max_y:int):
        self.__cam_bounds = (min_x, min_y, max_x, max_y)
        self.__cam_tx = max(self.__cam_bounds[0], min(self.__cam_tx, self.__cam_bounds[2] - pyxel.width))
        self.__cam_ty = max(self.__cam_bounds[1], min(self.__cam_ty, self.__cam_bounds[3] - pyxel.height))
        self.__cam_x = max(self.__cam_bounds[0], min(self.__cam_x, self.__cam_bounds[2] - pyxel.width))
        self.__cam_y = max(self.__cam_bounds[1], min(self.__cam_y, self.__cam_bounds[3] - pyxel.height))

    def shake_camera(self, amount:int, decay:float):
        self.__shake_amount = amount
        self.__shake_decay = decay

    def flash(self, lifespan:int, color:int, intensity:float):
        self.__flash = {"life":lifespan, "color":color, "intensity":intensity}

    def change_scene(self, new_scene_id:int, new_camera_x:int=0, new_camera_y:int=0, action=None):
        self.set_camera(new_camera_x, new_camera_y)

        self.__current_scene = self.__scenes_dict[new_scene_id]
        if action:
            action()

        if self.__current_scene.pyxres_path:
            pyxel.load(self.__current_scene.pyxres_path)
        pyxel.colors.from_list(self.__current_scene.palette)
        pyxel.title(self.__current_scene.title)
        pyxel.screen_mode(self.__current_scene.screen_mode)

    def change_scene_transition(self, transition:Transition):
        self.__transition = transition

    def finish_transition(self):
        self.__transition = None

    def apply_palette_effect(self, effect_function, **kwargs):
        pyxel.colors.from_list(effect_function(self.__current_scene.palette, kwargs))

    def reset_palette(self):
        pyxel.colors.from_list(self.__current_scene.palette)

    def update(self):
        if self.__transition:
            self.__transition.update(self)

        self.__cam_x += (self.__cam_tx - self.__cam_x) * 0.1
        self.__cam_y += (self.__cam_ty - self.__cam_y) * 0.1

        if self.__shake_amount > 0:
            a = self.__shake_amount
            pyxel.camera(self.__cam_x + random.uniform(-a, a), self.__cam_y + random.uniform(-a, a))
            self.__shake_amount = max(0, self.__shake_amount - self.__shake_decay)
        else:
            pyxel.camera(self.__cam_x, self.__cam_y)

        if not self.__transition:
            self.__current_scene.update()

    def draw(self):
        self.__current_scene.draw()
        if self.__transition:
            self.__transition.draw(self)

        if self.__flash:
            pyxel.dither(self.__flash["intensity"])
            pyxel.rect(self.__cam_x, self.__cam_y, pyxel.width, pyxel.height, self.__flash["color"])
            pyxel.dither(1)
            self.__flash["life"] -= 1
            if self.__flash["life"] == 0:
                self.__flash = {}

        if self.debug:
            pyxel.rect(self.__cam_x + 1, self.__cam_y + 1, 66, 27, self.debug_background_color)
            pyxel.text(self.__cam_x + 3, self.__cam_y + 3, f"Scene[{self.__current_scene.id}]", self.debug_text_color)
            pyxel.text(self.__cam_x + 3, self.__cam_y + 9, f"Screen[{pyxel.mouse_x},{pyxel.mouse_y}]", self.debug_text_color)
            pyxel.text(self.__cam_x + 3, self.__cam_y + 15, f"World[{self.mouse_x:.0f},{self.mouse_y:.0f}]", self.debug_text_color)
            pyxel.text(self.__cam_x + 3, self.__cam_y + 21, f"Fps[{self.__current_fps:.0f}]", self.debug_text_color)

        if pyxel.frame_count % self.__fps == 0:
            self.__current_fps = 1 / (time.time() - self.__previous_frame_time)
        self.__previous_frame_time = time.time()

    def run(self):
        pyxel.run(self.update, self.draw)

class Scene:

    def __init__(self, id:int, title:str, update, draw, pyxres_path:str, palette:list, screen_mode:int=0):
        self.id = id
        self.title = title
        self.update = update
        self.draw = draw
        self.pyxres_path = pyxres_path
        self.palette = palette
        self.screen_mode = screen_mode

class Sprite:

    def __init__(self, img:int, u:int, v:int, w:int, h:int, colkey:int=None):
        self.img = img
        self.u, self.v = u, v
        self.w, self.h = w, h
        self.colkey = 0 if colkey == 0 else colkey
        self.flip_horizontal = False
        self.flip_vertical = False

class Animation:

    def __init__(self, sprite:Sprite, total_frames:int=1, frame_duration:int=20, loop:bool=True):
        self.sprite = sprite
        self.__total_frames = total_frames
        self.frame_duration = frame_duration
        self.__loop = loop
        self.__start_frame = pyxel.frame_count
        self.current_frame = 0
        self.__is_finished = False

    def is_finished(self)-> bool:
        return self.__is_finished and not self.__loop
    
    def is_looped(self)-> bool:
        return self.__loop
    
    def reset(self):
        self.__start_frame = pyxel.frame_count
        self.current_frame = 0
        self.__is_finished = False

    def update(self):
        if self.is_finished():
            return
        
        if pyxel.frame_count - self.__start_frame >= self.frame_duration:
            self.__start_frame = pyxel.frame_count
            self.current_frame += 1
            if self.current_frame >= self.__total_frames:
                if self.__loop:
                    self.current_frame = 0
                else:
                    self.__is_finished = True
                    self.current_frame = self.__total_frames - 1

    def draw(self, x:int, y:int, anchor:int=ANCHOR_TOP_LEFT):
        x, y = get_anchored_position(x, y, self.sprite.w, self.sprite.h, anchor)

        w = -self.sprite.w if self.sprite.flip_horizontal else self.sprite.w
        h = -self.sprite.h if self.sprite.flip_vertical else self.sprite.h
        pyxel.blt(x, y, self.sprite.img, self.sprite.u + self.current_frame * abs(self.sprite.w), self.sprite.v, w, h, self.sprite.colkey)

def get_anchored_position(x:int, y:int, width:int, height:int, anchor:int)-> tuple:
    if anchor in [ANCHOR_TOP_RIGHT, ANCHOR_BOTTOM_RIGHT, ANCHOR_RIGHT]:
        x -= width
    if anchor in [ANCHOR_BOTTOM_LEFT, ANCHOR_BOTTOM_RIGHT, ANCHOR_BOTTOM]:
        y -= height
    if anchor in [ANCHOR_TOP, ANCHOR_BOTTOM, ANCHOR_CENTER]:
        x -= width // 2
    if anchor in [ANCHOR_LEFT, ANCHOR_RIGHT, ANCHOR_CENTER]:
        y -= height // 2
        
    return x, y

def clamp(value:int|float, min_value:int|float, max_value:int|float)-> int|float:
    return max(min_value, min(value, max_value))

#? -------------------- CONSTANTS -------------------- ?#

PALETTE = [0x000000, 0x180d2f, 0x353658, 0x686b72, 0x8b97b6, 0xc5cddb, 0xffffff, 0x5ee9e9, 
           0x2890dc, 0x1831a7, 0x053239, 0x005f41, 0x08b23b, 0x47f641, 0xe8ff75, 0xfbbe82, 
           0xde9751, 0xb66831, 0x8a4926, 0x461c14, 0x1e090d, 0x720d0d, 0x813704, 0xda2424, 
           0xef6e10, 0xecab11, 0xece910, 0xf78d8d, 0xf94e6d, 0xc12458, 0x841252, 0x3d083b]

WIDTH, HEIGHT = 232, 144
FPS = 60

COLLISION_TILES = [1]
COLLISION_TILES = [(x, y) for x in range(32) for y in COLLISION_TILES]

ONE_WAY_TILES = [(0,9),(1,9),(2,9)]

#? -------------------- CLASSES -------------------- ?#

class Tilemap:

    def __init__(self, id:int, x:int, y:int, w:int, h:int, colkey:int):
        self.id = id
        self.x = x
        self.y = y
        self.w, self.h = w, h
        self.colkey = colkey

    def collision_rect_tiles(self, x:int, y:int, w:int, h:int, tiles:list)-> bool:
        start_tile_x = (x - self.x) // 8
        start_tile_y = (y - self.y) // 8
        end_tile_x = (x + w - self.x - 1) // 8
        end_tile_y = (y + h - self.y - 1) // 8

        start_tile_x = clamp(start_tile_x, 0, self.w // 8 - 1)
        start_tile_y = clamp(start_tile_y, 0, self.h // 8 - 1)
        end_tile_x = clamp(end_tile_x, 0, self.w // 8 - 1)
        end_tile_y = clamp(end_tile_y, 0, self.h // 8 - 1)

        for tile_y in range(int(start_tile_y), int(end_tile_y) + 1):
            for tile_x in range(int(start_tile_x), int(end_tile_x) + 1):
                tile_id = pyxel.tilemaps[self.id].pget(tile_x, tile_y)

                if tile_id in tiles:
                    return True
        
        return False
    
    def tiles_in_rect(self, x:int, y:int, w:int, h:int, tiles:list):
        result = []

        start_tile_x = (x - self.x) // 8
        start_tile_y = (y - self.y) // 8
        end_tile_x = (x + w - self.x - 1) // 8
        end_tile_y = (y + h - self.y - 1) // 8

        start_tile_x = clamp(start_tile_x, 0, self.w // 8 - 1)
        start_tile_y = clamp(start_tile_y, 0, self.h // 8 - 1)
        end_tile_x = clamp(end_tile_x, 0, self.w // 8 - 1)
        end_tile_y = clamp(end_tile_y, 0, self.h // 8 - 1)

        for tile_y in range(int(start_tile_y), int(end_tile_y) + 1):
            for tile_x in range(int(start_tile_x), int(end_tile_x) + 1):
                tile_id = pyxel.tilemaps[self.id].pget(tile_x, tile_y)
                if tile_id in tiles:
                    result.append((int(tile_x), int(tile_y)))

        return result

    def draw(self):
        pyxel.bltm(self.x, self.y, self.id, 0, 0, self.w, self.h, self.colkey)

class Player:

    def __init__(self, x:int, y:int, tilemap:Tilemap):
        self.x, self.y = x, y
        self.w, self.h = 7, 8

        #? Animations
        self.main_animation = Animation(Sprite(0, 0, 8, 8, 8, 27))
        self.crouch_animation = Animation(Sprite(0, 8, 8, 8, 8, 27))
        self.current_animation = self.main_animation

        #? Others
        self.tilemap = tilemap

        #? Velocity
        self.velocity_x = 0
        self.velocity_y = 0
        self.max_velocity_y = 4
        self.gravity = 0.4
        self.friction = 0.8

        #? Movement
        self.speed = 1

        #? Jump
        self.coyote_timer = 0
        self.coyote_time = 6
        self.jump_speed = 2
        self.jump_power = 5.5
        self.jumping = False
        self.falling_timer = 0

        #? Flares
        self.facing_right = True
        self.on_ground = False
        self.dead = False
        self.free = False

    def _update_velocity_x(self):
        if self.velocity_x != 0:
            step_x = 1 if self.velocity_x > 0 else -1
            for _ in range(int(abs(self.velocity_x))):
                if not self.tilemap.collision_rect_tiles(self.x + step_x, self.y, self.w, self.h, COLLISION_TILES):
                    self.x += step_x
                else:
                    self.velocity_x = 0
                    break

    def _update_velocity_y(self):
        if self.velocity_y == 0:
            return

        step_y = 1 if self.velocity_y > 0 else -1
        for _ in range(int(abs(self.velocity_y))):
            next_y = self.y + step_y

            if step_y < 0:
                if not self.tilemap.collision_rect_tiles(self.x, next_y, self.w, self.h, COLLISION_TILES):
                    self.y = next_y
                else:
                    self.velocity_y = 0
                    break
            else:
                solid_hits = self.tilemap.tiles_in_rect(self.x, next_y, self.w, self.h, COLLISION_TILES)
                if solid_hits:
                    top_tile_y = min(ty for _, ty in solid_hits)
                    tile_top_world = self.tilemap.y + top_tile_y * 8
                    self.y = tile_top_world - self.h
                    self.velocity_y = 0
                    break

                one_way_hits = self.tilemap.tiles_in_rect(self.x, next_y, self.w, self.h, ONE_WAY_TILES)
                if one_way_hits:
                    top_tile_y = min(ty for _, ty in one_way_hits)
                    tile_top_world = self.tilemap.y + top_tile_y * 8

                    feet_before = self.y + self.h
                    if feet_before <= tile_top_world:
                        self.y = tile_top_world - self.h
                        self.velocity_y = 0
                        break
                    else:
                        self.y = next_y
                else:
                    self.y = next_y

    def _handle_free_movement(self):
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 2
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 2
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 2
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += 2

    def _handle_timers(self):
        self.coyote_timer = max(0, self.coyote_timer - 1)

        self.falling_timer = max(0, self.falling_timer - 1)
        if self.falling_timer > 0 and not self.tilemap.collision_rect_tiles(self.x, self.y + 2, self.w, self.h, COLLISION_TILES):
            self.y += 2

    def _is_on_ground(self):
        feet_y = self.y + self.h
        on_ground = False
        if self.tilemap.collision_rect_tiles(self.x, self.y + 1, self.w, self.h, COLLISION_TILES):
            on_ground = True
        else:
            if self.velocity_y >= 0:
                one_way_hits = self.tilemap.tiles_in_rect(self.x, self.y + 1, self.w, self.h, ONE_WAY_TILES)
                if one_way_hits:
                    top_tile_y = min(ty for _, ty in one_way_hits)
                    tile_top_world = self.tilemap.y + top_tile_y * 8
                    if feet_y <= tile_top_world:
                        on_ground = True
        return on_ground

    def _handle_movement(self):
        if pyxel.btn(pyxel.KEY_Q) or pyxel.btn(pyxel.KEY_A):
            self.velocity_x = -self.jump_speed if self.jumping and self.velocity_y < 0 else -self.speed
            self.facing_right = False
        if pyxel.btn(pyxel.KEY_D):
            self.velocity_x = self.jump_speed if self.jumping and self.velocity_y < 0 else self.speed
            self.facing_right = True

    def _handle_jump(self):
        if pyxel.btn(pyxel.KEY_SPACE) and ((self.on_ground or self.coyote_timer > 0) and not self.jumping):
            self.velocity_y = -self.jump_power
            self.jumping = True

    def _handle_crouching(self):
        if pyxel.btnp(pyxel.KEY_S) and not self.tilemap.collision_rect_tiles(self.x, self.y + 1, self.w, self.h, COLLISION_TILES) and not self.jumping:
            self.falling_timer = 8

        if pyxel.btn(pyxel.KEY_S):
            if self.current_animation != self.crouch_animation:
                self.current_animation = self.crouch_animation
        elif self.current_animation != self.main_animation:
            self.current_animation = self.main_animation

    def update(self):
        self.current_animation.update()

        if pyxel.btnp(pyxel.KEY_F):
            self.free = not self.free

        if self.dead:
            return
        
        if self.free:
            self._handle_free_movement()
            return

        self._handle_timers()
        
        self.velocity_y = min(self.velocity_y + self.gravity, self.max_velocity_y)
        self.velocity_x *= self.friction

        self.on_ground = self._is_on_ground()

        if self.on_ground:
            if not self.jumping:
                self.velocity_y = 0
            self.jumping = False
            self.coyote_timer = self.coyote_time

        self._handle_movement()
        self._handle_jump()
        self._handle_crouching()

        self._update_velocity_y()
        self._update_velocity_x()

    def draw(self):
        self.current_animation.sprite.flip_horizontal = not self.facing_right
        self.current_animation.draw(self.x, self.y)

class CheckpointManager:

    def __init__(self, start_x:int, start_y:int):
        self.checkpoint_x, self.checkpoint_y = start_x, start_y

    def update(self, player:Player):
        if player.dead:
            player.x, player.y = self.checkpoint_x, self.checkpoint_y
            player.dead = False

class AnimatedTilesManager:

    def __init__(self, animated_tiles_dict:dict):
        self.animated_tiles_dict = animated_tiles_dict
        self.update_timer = 0

    def update(self, camera_x:int, camera_y:int):
        self.update_timer += 1

        if self.update_timer == 20:
            self.update_timer = 0
            for y in range(pyxel.height // 8):
                for x in range(pyxel.width // 8):
                    tile_id = pyxel.tilemaps[0].pget(camera_x // 8 + x, camera_y // 8 + y)
                    if tile_id in self.animated_tiles_dict.keys():
                        pyxel.tilemaps[0].pset(camera_x // 8 + x, camera_y // 8 + y, self.animated_tiles_dict[tile_id])

class Room: 

    def __init__(self, u:int, v:int, left:int=None, right:int=None, up:int=None, down:int=None, on_enter=None, on_exit=None):
        self.u, self.v = u * 8, v * 8
        self.left, self.right = left, right
        self.up, self.down = up, down
        self.on_enter, self.on_exit = on_enter, on_exit

    def update(self, pyxel_manager:PyxelManager, player:Player, checkpoint_manager:CheckpointManager, rooms:dict):
        if player.x + player.w <= self.u and self.left is not None:
            new_u = rooms.get(self.left).u
            new_v = rooms.get(self.left).v
            def action():
                if self.on_exit:    self.on_exit()
                player.x = new_u + pyxel.width - 8
                player.y = new_v + (player.y - self.v)
                checkpoint_manager.checkpoint_x = player.x
                checkpoint_manager.checkpoint_y = player.y
                if rooms.get(self.left).on_enter:    rooms.get(self.left).on_enter()
            pyxel_manager.change_scene_transition(TransitionRectangle(0, 0.25, 0, LEFT, new_u, new_v, action))
            return self.left
        
        elif player.x >= self.u + pyxel.width and self.right is not None:
            new_u = rooms.get(self.right).u
            new_v = rooms.get(self.right).v
            def action():
                if self.on_exit:    self.on_exit()
                player.x = new_u
                player.y = new_v + (player.y - self.v)
                checkpoint_manager.checkpoint_x = player.x
                checkpoint_manager.checkpoint_y = player.y
                if rooms.get(self.right).on_enter:    rooms.get(self.right).on_enter()
            pyxel_manager.change_scene_transition(TransitionRectangle(0, 0.25, 0, RIGHT, new_u, new_v, action))
            return self.right
        
        elif player.y + player.h <= self.v and self.up is not None:
            new_u = rooms.get(self.up).u
            new_v = rooms.get(self.up).v
            def action():
                if self.on_exit:    self.on_exit()
                player.x = new_u + (player.x - self.u)
                player.y = new_v + pyxel.height - 16
                checkpoint_manager.checkpoint_x = player.x
                checkpoint_manager.checkpoint_y = player.y
                if rooms.get(self.up).on_enter:    rooms.get(self.up).on_enter()
            pyxel_manager.change_scene_transition(TransitionRectangle(0, 0.25, 0, TOP, new_u, new_v, action))
            return self.up
        
        elif player.y >= self.v + pyxel.height and self.down is not None:
            new_u = rooms.get(self.down).u
            new_v = rooms.get(self.down).v
            def action():
                if self.on_exit:    self.on_exit()
                player.x = new_u + (player.x - self.u)
                player.y = new_v
                checkpoint_manager.checkpoint_x = player.x
                checkpoint_manager.checkpoint_y = player.y
                if rooms.get(self.down).on_enter:    rooms.get(self.down).on_enter()
            pyxel_manager.change_scene_transition(TransitionRectangle(0, 0.25, 0, BOTTOM, new_u, new_v, action))
            return self.down
        
class RoomManager:

    def __init__(self, rooms:dict, start_room_id:int):
        self.rooms = rooms
        self.current_room_id = start_room_id
        self.current_room = self.rooms.get(start_room_id)

    def update(self, pyxel_manager:PyxelManager, player:Player, checkpoint_manager:CheckpointManager):
        id = self.current_room.update(pyxel_manager, player, checkpoint_manager, self.rooms)
        if id is not None:
            self.current_room_id = id
            self.current_room = self.rooms.get(id)

#? -------------------- ROOMS -------------------- ?#

#? -------------------- GAME -------------------- ?#

class Game:

    def __init__(self):
        #? Scenes
        game_scene = Scene(0, "WizHard - Game", self.update_game, self.draw_game, "assets.pyxres", PALETTE)
        scenes = [game_scene]

        #? Init
        self.pyxel_manager = PyxelManager(WIDTH, HEIGHT, scenes, 0, FPS, True, True, camera_x=16, camera_y=16)

        #? Game Variables
        self.tilemap_0 = Tilemap(0, 0, 0, 256*8, 256*8, 0)
        self.tilemap_1 = Tilemap(1, 0, 0, 256*8, 256*8, 0)
        self.player = Player(25, 100, self.tilemap_0)

        #? Run
        self.pyxel_manager.run()

    def update_game(self):
        self.player.update()

    def draw_game(self):
        pyxel.cls(0)
        
        self.tilemap_0.draw()
        self.player.draw()
        self.tilemap_1.draw()

if __name__ == "__main__":
    Game()