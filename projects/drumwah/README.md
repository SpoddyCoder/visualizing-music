# Drumwah
When this was originally recorded I was just messing about putting a toy drum machine through a crybaby wah pedal - as with a lot of my stuff, just a raw tape demo. Re-imagined in 2024 and becomes the first release in the visualizing music project.

https://www.youtube.com/watch?v=z8TY0dtIzLw

Song written, performed and recorded by Paul Fernihough, 1998, 2024


## Environment & Tools
This song serves as our launch point - getting environments, software, tools and lots of initial learning done.
Lucid Sonic Dreams is no longer maintained and the most popular forks have also been left for a while now - this was the hardest part to get working, quite a few dependency issues to work through to get it working on an up to date python stack.

### AI Visualization
* Ubuntu22.04 running on WSL2:
  * https://github.com/SpoddyCoder/wsl-builds
* Using the WLS2 `resource-ai` build to install lucid-sonic-dreams:

```
cd ~/wsl-builds
./build.sh biscuit update,qol,x11,vscode
./build.sh biscuit-ai conda,cuda124
./build.sh resource-ai lsd
```

* AI Model: StyleGAN2
* Dataset: Cats
* [lsd generator code](../../lucid-sonic-dreams/drumwah.py)

### Audio + Video Editing
* DAW: Reaper
* NLE: DaVinci Resolve
