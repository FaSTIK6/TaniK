from .bus import bus 
import raylib as rl 
from utils import c_str 

player_hp = 100 

def hpDamage(hp: int) -> None:
    global player_hp
    player_hp -= hp


bus.connect("HP_DAMAGE", hpDamage) 

if __name__ == "__main__": 
    rl.InitWindow(800, 450, c_str("New library")) 
    rl.SetTargetFPS(60) 

    while not rl.WindowShouldClose(): 
        rl.BeginDrawing() 
        rl.ClearBackground(rl.WHITE) 

        if rl.IsKeyPressed(rl.KEY_W): 
            bus.emit("HP_DAMAGE", 10) 

        rl.DrawText(c_str(f"hp: {player_hp}"), 100, 100, 100, rl.BLACK) 

        rl.EndDrawing() 

    rl.CloseWindow()
