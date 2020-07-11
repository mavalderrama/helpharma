# helpharma
ds4a_helpharma

# Building Image

The Dockerfiles can be built from the root project directory with the following command:

```shell script
docker build -t mavalderrama/helpharma -f Dockerfile frontend
```

# Run your Container

To use FalconCV and jupyter lab execute following command, it will share your $HOME to your container, also

```shell script
docker run --gpus all --rm -it -p 8888:8888 -p 8787:8787 -p 8786:8786 -v $HOME:$HOME haruiz/falconcv
docker run --name helpharma -it --rm mavalderrama/helpharma
```

## Go to your favorite browser and assuming you are running Docker on your local machine type:

Link: [http://localhost:8888/lab](localhost:8888/lab)

