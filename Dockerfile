FROM continuumio/miniconda3

WORKDIR /usr/src/app

# Copy the environment specs and update the base envorinment
#  so that you don't need to source anything or muck with your PATH variable
COPY environment.yml ./
RUN conda env update -n base -f environment.yml

CMD ["/bin/bash"]