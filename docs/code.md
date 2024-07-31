<!---- <!doctype html>
<html>

<head>
    {% if title %}
    <title>{{ title }} - Flood Prediction Model</title>
    {% else %}
    <title>Welcome to Flood Prediction Model</title>
    {% endif %}
</head>

<body>
    <div>Flood Prediction Model: <a href="/index">Home</a>
        <a href="/prediction">Prediction</a>
    </div>
    <hr>
    {% block content %}{% endblock %}
</body>

</html> 


<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    {% if title %}
    <title>{{ title }} - Flood Prediction Model</title>
    {% else %}
    <title>Welcome to Flood Prediction Model</title>
    {% endif %}

    <link
        href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
        rel="stylesheet"
        integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
        crossorigin="anonymous">
  </head>
  <body>
    
    <div>Flood Prediction Model: <a href="/index">Home</a>
        <a href="/prediction">Prediction</a></div>
        <hr>
    {% block content %}{% endblock %}

    <script
        src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
        crossorigin="anonymous">
    </script>
  </body>
</html>

-->
-------------

the login & logout part in base.html
<!--   
          <ul class="navbar-nav mb-2 mb-lg-0">
         {% if current_user.is_anonymous %}
            <li class="nav-item">
              <a class="nav-link" aria-current="page" href="{{ url_for('login') }}">Login</a>
            </li>
            {% else %}
            <li class="nav-item">
              <a class="nav-link" aria-current="page" href="{{ url_for('user', username=current_user.username) }}">Profile</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" aria-current="page" href="{{ url_for('logout') }}">Logout</a>
            </li>
            {% endif %}

          </ul>
-->