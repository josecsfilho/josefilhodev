import multiprocessing

bind = "127.0.0.1:8000"  # Endereço e porta que o Gunicorn irá escutar
workers = multiprocessing.cpu_count() * 2 + 1  # Número de workers
errorlog = "-"
