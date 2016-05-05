/**
 * Created by jamesnarey on 29/04/2016.
 */


function setColourByClass(colour, hex_colour) {

  var elements = document.getElementsByClassName(colour);

  for (var i = 0; i < elements.length; i++) {

    elements[i].style.backgroundColor = hex_colour;
  }

}

function setElementColours() {

  var green_hex_colour = '#009900';
  var amber_hex_colour = '#ff6600';
  var red_hex_colour = '#e60000';


  setColourByClass("green", green_hex_colour);
  setColourByClass("amber", amber_hex_colour);
  setColourByClass("red", red_hex_colour);

}


function get_statuses() {
  console.log("Get statuses request made")
  $.ajax({
    url: "/services/get_statuses/",
    type: "GET",

    success: function (json) {
      console.log(json);
      updateStatusElements(json, "auto_cell");
      setElementColours();

    },

    error: function (xhr, errmsg, err) {
      console.log(xhr.status + ": " + xhr.responseText);
    }

  });
}


function updateStatusElements(response, class_name) {

  for (var i = 0; i < response.length; i++) {

    var named_elements = document.getElementsByClassName(value.name);

    for (var i = 0; i < named_elements.length; i++) {

      if ($(value).hasClass(class_name)) {
        updateElementColourClass(value, response)
      }
    }

  }

}

function updateElementColourClass(target_element, colour) {

  var colours = ['red', 'amber', 'green']

  for (var i = 0; i < colours.length; i++) {
    if ($(target_element).hasClass(colours[i]) && colours[i] != colour) {
      target_element.classList.remove(colours[i]);
    }
  }

  target_element.classList.add(colour)

}


function selectBoxChange(event) {
  console.log("Change registered");
  var colour_class = event.target.value;
  updateElementColourClass(event.target, colour_class);
  updateElementColourClass(event.target.parentElement, colour_class);
  setElementColours();
}

function setInitSelectColourClass() {
  var select_boxes = document.getElementsByTagName("select");
  for (var i = 0; i < select_boxes.length; i++) {
    updateElementColourClass(select_boxes[i], select_boxes[i].value)
  }
}


function addSelectChangeEvents() {

    $('select').change(function( event ){ // <---- "event" parameter here

      selectBoxChange(event)

    });

}

//Run on script import

console.log("main.js imported");

//Run on page load
$(document).ready(function () {

  console.log("document ready event");


});
