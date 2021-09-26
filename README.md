# songwhip zsh plugin
Get song links in markdown and other formats using songwhip.com for most popular music services

### Requirements
* python3
* python libs:
  * requests
  * lxml


## Installation

### Manual

1. Clone this repository somewhere on your machine. This guide will assume `~/.zsh/songwhip`.

```sh
git clone https://github.com/zsh-users/zsh-apple-touchbar ~/.zsh/songwhip
```

2. Add the following to your `.zshrc`:

```sh
source ~/.zsh/songwhip/songwhip.plugin.zsh
```


### Oh My Zsh

1. Clone this repository into `$ZSH_CUSTOM/plugins` (by default `~/.oh-my-zsh/custom/plugins`)

```sh
git clone https://github.com/zheqd/songwhip.git $ZSH_CUSTOM/plugins/songwhip
```

2. Add the plugin to the list of plugins for Oh My Zsh to load:

```sh
plugins=(songwhip)
```
## Usage

```sh
sw <track-link>
```
### Example

```bash
sw https://music.yandex.com/album/6768361/track/49333874
[Yandex](https://music.yandex.com/track/49333874)
[Spotify](https://open.spotify.com/track/4hWdGAGZepqE1X68o4ss82)
[Apple Music](https://music.apple.com/ru/album/we-could-leave/1449253497?i=1449253756&app=music)
[YouTube](https://youtube.com/watch?v=HSTh5DJyFVk)
[Tidal](https://listen.tidal.com/track/102088942)
[Amazon Music](https://music.amazon.com/albums/B07MQ24N4P?trackAsin=B07MFRD1MF)
[YouTube Music](https://music.youtube.com/watch?v=HSTh5DJyFVk)
[Deezer](https://www.deezer.com/track/614311812)
[Napster](https://napster.com/mansionair/we-could-leave/we-could-leave)
```
