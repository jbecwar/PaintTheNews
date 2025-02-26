# PaintTheNews

## Description
PaintTheNews is a project that generates abstract emotional paintings based on the latest news headlines.  Content is published automaticly to https://paintthenews.com

## Installation
To install the required dependencies, run:
```
pip install -r requirements.txt
```

## Usage
To run the project, execute:
```
python main.py
```

### Tests
To run the unit tests, execute:
```
python -m unittest
```

## Features
- Fetches the latest news headlines
- Generates abstract paintings based on the headlines
- Creates a video from the generated paintings
- Automatically pushes updates to GitHub

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## Acknowledgements
- [NYT](https://www.nytimes.com/) for the public RSS feeds
- [Feedparser](https://github.com/kurtmckee/feedparser) for parsing RSS feeds
- [Diffusers](https://github.com/huggingface/diffusers) for the Stable Diffusion models
- [Cloudflair](https://www.cloudflare.com/) for hosting
