def getIcon(name: str) -> str:
    if name == "com.mitchellh.ghostty":
        return "/home/rohan/.config/ignis/assets/ghostty.svg"
    elif name == "zen":
        return "/home/rohan/.config/ignis/assets/zen-browser.svg"
    elif name == "org-tlauncher-tlauncher-rmo-TLauncher":
        return "/home/rohan/.config/ignis/assets/minecraft.svg"
    else:
        return name
