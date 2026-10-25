FROM python:3.12.14-slim
WORKDIR /app
ENV PYTHONHASHSEED=0
COPY requirements.txt requirements-lock.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY src ./src
COPY session_05/README.md ./session_05/README.md
CMD ["sh", "-c", "python src/generate_synthetic.py && python src/run_experiment.py && python src/build_project_cards.py"]
