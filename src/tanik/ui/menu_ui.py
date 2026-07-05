def draw_menu(current_state) -> None:
    buf: str = "\n"

    buf += "   ╔════════════════════════════\n"
    buf += "   ║  Hi! IT'S TaniK!\n"
    buf += "   ╚══════════\n\n"
    
    buf += "   ╔════════════════════════════\n"
    buf += "   ║ 1. Go fight!\n"
    buf += "   ║ 2. Stats\n"
    buf += "   ║ 3. Achivments\n"
    buf += "   ║ i. Inventory\n"
    buf += "   ║ u. Upgrades\n"
    buf += "   ║ s. Shop\n"
    buf += "   ║ v. Events\n"
    buf += "   ║ e. Settings\n"
    buf += "   ║ a. Save\n"
    buf += "   ║ q. Quit\n"
    buf += "   ╚══════════\n"
    buf += f"{current_state}\n"

    print(buf)
