/**
 * Created by jamesnarey on 29/04/2016.
 */

// function set_cell_colours() {
//
//   var ok_hex_colour = '#009900';
//   var not_ok_hex_colour = '#e60000';
//
//   console.log('***********update_cell_colours called*******************')
//
//   var trueCells = document.getElementsByClassName("true");
//
//   for (var i = 0; i < trueCells.length; i++) {
//
//     trueCells[i].style.backgroundColor = ok_hex_colour;
//   }
//
//   var falseCells = document.getElementsByClassName("false");
//
//   for (var i = 0; i < falseCells.length; i++) {
//
//     falseCells[i].style.backgroundColor = not_ok_hex_colour;
//   }
//
//
// }

function set_cell_colours() {

  var green_hex_colour = '#009900';
  var amber_hex_colour = '#ff6600';
  var red_hex_colour = '#e60000';

  console.log('***********new_update_cell_colours called*******************')

  var greenCells = document.getElementsByClassName("green");

  for (var i = 0; i < greenCells.length; i++) {

    greenCells[i].style.backgroundColor = green_hex_colour;
  }

  var amberCells = document.getElementsByClassName("amber");

  for (var i = 0; i < amberCells.length; i++) {

    amberCells[i].style.backgroundColor = amber_hex_colour;
  }

  var redCells = document.getElementsByClassName("red");

  for (var i = 0; i < redCells.length; i++) {

    redCells[i].style.backgroundColor = red_hex_colour;
  }

}


function get_statuses() {
  console.log("Get statuses request made")
  $.ajax({
    url: "/services/get_statuses/",
    type: "GET",

    success: function (json) {
      console.log(json);
      update_status_elements(json);
      set_cell_colours();

    },

    error: function (xhr, errmsg, err) {
      console.log(xhr.status + ": " + xhr.responseText);
    }

  });
}

// function update_status_elements(response) {
//
//   console.log('***********update_status_elements called*******************')
//   console.log(response);
//
//   $.each(response, function( index, value ) {
//
//     var row;
//     var auto_cell;
//     var manual_cell;
//     var to_unset;
//
//     row = document.getElementById(value.name);
//
//     auto_cell = row.getElementsByClassName("auto_status_cell")[0];
//     manual_cell = row.getElementsByClassName("manual_status_cell")[0];
//
//
//     if (auto_cell != undefined) {
//       if ($(auto_cell).hasClass(value.auto_status)) {
//
//       } else {
//
//         if (value.auto_status = true) {
//           to_unset = false;
//         } else {
//           to_unset = true;
//         }
//
//         auto_cell.classList.remove(to_unset.toString());
//         auto_cell.classList.add(value.auto_status.toString());
//
//       }
//     }
//
//     if (manual_cell != undefined) {
//       if ($(manual_cell).hasClass(value.manual_status)) {
//
//       } else {
//
//         if (value.manual_status = true) {
//           to_unset = false;
//         } else {
//           to_unset = true;
//         }
//
//         manual_cell.classList.remove(to_unset.toString());
//         manual_cell.classList.add(value.manual_status.toString());
//
//       }
//     }
//
//
//   });
//
// }

function update_status_elements(response, class_name) {

  $.each(response, function( index, value ) {

    var named_elements = document.getElementsByClassName(value.name);
    var auto_status = value.auto_status;
    var manual_status = value.manual_status;

    $.each(named_elements, function( index, value ) {

      if ($(value).hasClass("auto_cell")) {
        update_colour_class(value, response)
      }

    });


  });

}

function update_colour_class(target_element, colour) {

  var colours = ['red', 'amber', 'green']

  for (var i = 0; i < colours.length; i++) {
    if ($(target_element).hasClass(colours[i]) && colours[i] != colour) {
      target_element.classList.remove(colours[i]);
    }
  }

  target_element.classList.add(colour)

}

function updateSelectedColours() {
  console.log("Change registered");
  var colour_class = event.target.value;
  update_colour_class(event.target, colour_class);
  update_colour_class(event.target.parentElement, colour_class);
  set_cell_colours();
}

function initial_select_box_colour_class() {
  var select_boxes = document.getElementsByTagName("select");
  for (var i = 0; i < select_boxes.length; i++) {
    update_colour_class(select_boxes[i], select_boxes[i].value)
  }
}

function add_select_box_events() {

  var select_boxes =  document.getElementsByTagName("select");

  for (var i = 0; i < select_boxes.length; i++) {
    select_boxes[i].onchange = updateSelectedColours;
  }

}

//
// function update_status_elements(response) {
//
//   console.log('***********update_status_elements called*******************')
//   console.log(response);
//
//   var statuses = response;
//
//
//   $.each( statuses, function( key, value ) {
//
//     var row;
//     var auto_cell;
//
//     //var element_id = key + "_status";
//
//     console.log( key + ": " + value );
//
//     console.log(key);
//
//     row = document.getElementById(key); // .innerHTML = value.toString();
//
//     auto_cell = row.getElementsByClassName("auto_status_cell")[0];
//     //auto_cell.innerHTML = value.toString();
//     auto_cell.classList.add(value.toString());
//
//   });
//
//
// }
//
// function get_statuses() {
//   console.log("AJAX Status Request made")
//   $.ajax({
//     url: "/services/check_all_services/",
//     type: "GET",
//
//     success: function (json) {
//       console.log(json);
//       update_status_elements(json);
//       set_cell_colours();
//
//     },
//
//     error: function (xhr, errmsg, err) {
//       console.log(xhr.status + ": " + xhr.responseText);
//     }
//
//   });
// }

//Run on script import

console.log("main.js imported");

//Run on page load
$(document).ready(function () {

  console.log("document ready event");


});
