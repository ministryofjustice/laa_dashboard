/**
 * Created by jamesnarey on 29/04/2016.
 */

var colourChangeHelper = {

  colours: ['red', 'amber', 'green'],
  greenHex: '#009900',
  amberHex: '#ff6600',
  redHex: '#e60000',

  setElementColours: function () {

    this.setColourByClass("green", this.greenHex);
    this.setColourByClass("amber", this.amberHex);
    this.setColourByClass("red", this.redHex);

  },

  setColourByClass: function (colour, hex_colour) {

    var elements = document.getElementsByClassName(colour);

    for (var i = 0; i < elements.length; i++) {

      elements[i].style.backgroundColor = hex_colour;
    }

  },

  updateElementColourClass: function (target_element, colour) {

    for (var i = 0; i < this.colours.length; i++) {
      if ($(target_element).hasClass(this.colours[i])) {
        target_element.classList.remove(this.colours[i]);
      }
    }

    target_element.classList.add(colour);

  }

};








//Run on script import

console.log("colourChangeHelper.js imported");

//Run on page load
$(document).ready(function () {

  console.log("document ready event");


});


