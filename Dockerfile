FROM python:3.12.14-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src ./src
CMD ["sh", "-c", "python src/generate_synthetic.py && python src/run_experiment.py && python src/build_project_cards.py"]
