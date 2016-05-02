/**
 * Created by jamesnarey on 29/04/2016.
 */

var ok_hex_colour = '#009900';
var not_ok_hex_colour = '#e60000';

function update_status_elements(response) {

  console.log('***********update_status_elements called*******************')
  console.log(response);

  var statuses = response;


  $.each( statuses, function( key, value ) {

      var row;
      var auto_cell;

      //var element_id = key + "_status";

      console.log( key + ": " + value );

      console.log(key);

      row =document.getElementById(key); // .innerHTML = value.toString();

      auto_cell = row.getElementsByClassName("auto_status_cell")[0];
      //auto_cell.innerHTML = value.toString();
      auto_cell.classList.add(value.toString());

  });


}



function set_cell_colours() {

  console.log('***********update_cell_colours called*******************')

  var trueCells = document.getElementsByClassName("true");

  for (var i = 0; i < trueCells.length; i++) {

    trueCells[i].style.backgroundColor=ok_hex_colour;
  }

  var falseCells = document.getElementsByClassName("false");

  for (var i = 0; i < falseCells.length; i++) {

    falseCells[i].style.backgroundColor=not_ok_hex_colour;
  }


}




function get_statuses() {
  console.log("AJAX Status Request made")
  $.ajax({
    url: "check_all_services/",
    type: "GET",

    success: function (json) {
      //console.log(json);
      update_status_elements(json);
      set_cell_colours();

    },

    error: function (xhr, errmsg, err) {
      console.log(xhr.status + ": " + xhr.responseText);
    }

  });
}




//Run on script import

console.log("main.js imported");

//Run on page load
$(document).ready(function(){




});
