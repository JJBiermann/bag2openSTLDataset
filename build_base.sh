docker build -t miniconda-base:latest -f miniconda.Dockerfile .
docker build -t bag-base:latest -f conda-env.Dockerfile .