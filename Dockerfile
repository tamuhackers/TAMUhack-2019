FROM python:3.6
LABEL maintainer="TAMUhackers"
ADD . /TAMUhack-2019
WORKDIR /TAMUhack-2019
RUN python -m pip install pipenv
RUN pipenv install --dev
RUN pipenv run pip install -e .
CMD ["pipenv", "run", "python", "tamuhackers19/main.py"]