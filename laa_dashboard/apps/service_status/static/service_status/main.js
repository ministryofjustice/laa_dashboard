/**
 * Created by jamesnarey on 29/04/2016.
 */


// This function gets cookie with a given name
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

//The functions below will create a header with csrftoken

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function sameOrigin(url) {
  // test that a given url is a same-origin URL
  // url could be relative or scheme relative or absolute
  var host = document.location.host; // host + port
  var protocol = document.location.protocol;
  var sr_origin = '//' + host;
  var origin = protocol + sr_origin;
  // Allow absolute or scheme relative URLs to same origin
  return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
    (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
      // or any other URL that isn't scheme relative or absolute i.e relative.
    !(/^(\/\/|http:|https:).*/.test(url));
}


function update_status_elements(response) {

  console.log('***********update_status_elements called*******************')
  console.log(response);

  var statuses = response;


  $.each( statuses, function( key, value ) {

      var row;

      //var element_id = key + "_status";

      console.log( key + ": " + value );

      console.log(key);

      row =document.getElementById(key); // .innerHTML = value.toString();

      row.getElementsByClassName("status_cell")[0].innerHTML = value.toString();

  });


}

function get_statuses() {
  console.log("AJAX Status Request made")
  $.ajax({
    url: "check_all_services/",
    type: "GET",

    success: function (json) {
      //console.log(json);
      update_status_elements(json);

    },

    error: function (xhr, errmsg, err) {
      console.log(xhr.status + ": " + xhr.responseText);
    }

  });
}


//Run on script import

console.log("main.js imported");

var csrftoken = getCookie('csrftoken');

$.ajaxSetup({
  beforeSend: function (xhr, settings) {
    if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
      // Send the token to same-origin, relative URLs only.
      // Send the token only if the method warrants CSRF protection
      // Using the CSRFToken value acquired earlier
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  }
});



//Run on page load
$(document).ready(function(){




});
