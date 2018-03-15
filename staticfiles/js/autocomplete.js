 $(function(){
    $.fn.atwho.debug = true

    var jeremy = decodeURI("J%C3%A9r%C3%A9my") // Jérémy
    var names = ["Penicilline","Chemo Therapy","Cobalt60","Alatrol","Civit","Omeprazol","Azythromycin","Napa","Paracetamol","NapaExtra","Joshua","Emily","Daniel","Madison","Jayden","Abigail","Noah","Chloe","你好","你你你", jeremy, "가"];
    /*{% if medicine_array %}
        {% for i in medicine_array %}
        document.write(i);
        {% endfor %}
    {% endif %}
    /*var names = $.map(names,function(value,i) {
      return {'id':i,'name':value,'email':value+"@email.com"};
    });*/

    var dose = ["20 mg","50 mg"]
    var timetable = ["once a day", "twice a day", "for 5 days"]

    var at_config = {
      at: "@m",
      data: names,
      headerTpl: '<div class="atwho-header">Suggested Medicine List<small>↑&nbsp;↓&nbsp;</small></div>',
      insertTpl: '${name}',
      displayTpl: "<li>${name}</li>",
      limit: 7
    }

    var at_configd = {
      at: "@d",
      data: dose,
      headerTpl: '<div class="atwho-header">Suggested Dose List<small>↑&nbsp;↓&nbsp;</small></div>',
      insertTpl: '${dose}',
      displayTpl: "<li>${dose}</li>",
      limit: 7
    }

    var at_configt = {
      at: "@t",
      data: timetable,
      headerTpl: '<div class="atwho-header">Suggested Time List<small>↑&nbsp;↓&nbsp;</small></div>',
      insertTpl: '${timetable}',
      displayTpl: "<li>${timetable}</li>",
      limit: 7
    }

    $inputor = $('#inputor').atwho(at_config).atwho(at_configd).atwho(at_configt);
    $inputor.caret('pos', 47);
    $inputor.focus().atwho('run');

    $('#editable').atwho(at_config).atwho(at_configd).atwho(at_configt);

    ifr = $('#iframe1')[0]
    doc = ifr.contentDocument || iframe.contentWindow.document
    if ((ifrBody = doc.body) == null) {
      // For IE
      doc.write("<body></body>")
      ifrBody = doc.body
    }
    ifrBody.contentEditable = true
    ifrBody.id = 'ifrBody'
    ifrBody.innerHTML = 'For <strong>WYSIWYG</strong> which using <strong>iframe</strong> such as <strong>ckeditor</strong>'
    $(ifrBody).atwho('setIframe', ifr).atwho(at_config).atwho(at_configd).atwho(at_configt)

  });
