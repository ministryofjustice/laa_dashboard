var statusRequest = {

  {% for service in services.items %}

      {{service.name}}: {{service.name}}_status

  {% endfor %}

}
