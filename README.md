<p>1.запустить <B>creatdb</B></p>
<p>2.Открыть 2 терминала</p>
  <p>a)В 1 перейти в /tt/client</p>
    <p>и запустить:</p>
     <p><B> python manage.py runserver</B></p>

  <p>b)во 2 в /tt/WebAPI</p>
    <p>и запустить:</p>
      <p><B>uvicorn main:app --port 4000 --reload</B></p>
