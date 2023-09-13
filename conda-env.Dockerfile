FROM miniconda-base:latest

WORKDIR /app
COPY environment.yml .

RUN conda init bash
RUN . /root/.bashrc
RUN conda update conda
RUN conda env create -f environment.yml