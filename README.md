# get-started-openai
Starting points for open ai gym and agents

## Getting started

### Creating conda environment for open universe

``` sh
# Environment
conda create --name rl
source activate rl

# Installing pre-reqs
## On Mac
brew install tmux htop cmake golang libjpeg-turbo
## On Linux
use sudo apt-get install -y tmux htop cmake golang libjpeg-dev

pip install "gym[atari]"
pip install universe
pip install six
pip install tensorflow
conda install -y -c https://conda.binstar.org/menpo opencv3
conda install -y numpy
conda install -y scipy
```

### Testing environment

```sh
git clone https://github.com/naren-m/get-started-openai.git
cd get-started-openai

python sample.py
```


## References

- [Conda env creation for open ai](https://github.com/openai/universe-starter-agent)

- [OpenAI Gym setup](https://gist.github.com/iambrian/2bcc8fc03eaecb2cbe53012d2f505465)

- [Python programming tutorial on Open AI](https://www.youtube.com/watch?v=3zeg7H6cAJw)

