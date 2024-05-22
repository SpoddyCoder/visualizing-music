# Endless Ever, Special Llamas
Originally recorded in our local practice room on an old 8 track back in 1998. The recorder used standard audio cassettes - which is not a lot of bandwidth to squeeze in the big sound of the Special Llamas!
Audio decomposed into stems by Spleeter and re-mixed in Reaper.

https://www.youtube.com/watch?v=E_SUavxxSs8

Song written, performed and recorded by Special Llamas, 1998
Remastered by P. Fernihough, 2024


## Environment & Tools

### AI Visualization
* Ubuntu22.04 running on WSL2:
  * https://github.com/SpoddyCoder/wsl-builds
* Using the WLS2 `resource-ai` build to install lucid-sonic-dreams & spleeter:

```
cd ~/wsl-builds
./build.sh biscuit update,qol,x11,vscode
./build.sh biscuit-ai conda,cuda124
./build.sh resource-ai spleeter,lsd
```

* AI Model: StyleGAN2
* Dataset: Textures, Trypophobia, Microscope Images
* [lsd generator code](../../lucid-sonic-dreams/endless-ever/)

### Audio + Video Editing
* DAW: Reaper
* NLE: DaVinci Resolve
