FROM continuumio/miniconda3

WORKDIR /usr/src/app

# Copy environment.yml and create the conda environment
COPY environment.yml ./
RUN conda env create -f environment.yml

# Copy example.py to the working directory
COPY example.py ./

# Activate the conda environment and run example.py
CMD ["bash", "-c","source activate myenv && python ./example.py"]