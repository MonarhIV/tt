1.запустить creatdb
2.Открыть 2 терминала
  a)В 1 перейти в /tt/client
    и запустить:
      python manage.py runserver

  b)во 2 в /tt/WebAPI
    и запустить:
      uvicorn main:app --port 4000 --reload
