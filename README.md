# [HumanSeg](https://github.com/PaddlePaddle/PaddleSeg/tree/release/2.4/contrib/PP-HumanSeg)

HumanSeg is using to segment human in videos.

This is the optimized docker version of it.

Input:

!['input video'](./demo/input.gif "Input video")

Output:

!['output video'](./demo/output.gif "Output video")

## Build Docker

Using CPU:
```bash
docker build -t humanseg -f Dockerfile.cpu . --force-rm
```
Using GPU:
```bash
docker build -t humanseg -f Dockerfile.gpu . --force-rm
```

## Usage
1. Put videos you want to replace into folder `./input`.
2. Run inferring:
   - On CPU:
   ```bash
   docker-compose -f docker-compose-cpu.yml up
   ```
   - On GPU:
   ```bash
   docker-compose -f docker-compose-gpu.yml up
   ```
3. The output will be in the `./output` folder after the run.

Note: You can change the input/output directory in the docker-compose file.
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
