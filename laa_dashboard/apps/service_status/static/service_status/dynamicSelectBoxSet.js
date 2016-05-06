/**
 * Created by jamesnarey on 06/05/2016.
 */
var dynamicSelectBoxSet = {

  selectBoxes: document.getElementsByTagName("select"),

  selectBoxChange: function (event) {
    var colour_class = event.target.value;
    colourChangeHelper.updateElementColourClass(event.target, colour_class);
    colourChangeHelper.updateElementColourClass(event.target.parentElement, colour_class);
    colourChangeHelper.setElementColours();
  },

  setInitSelectColourClass: function () {
    for (var i = 0; i < this.selectBoxes.length; i++) {
      colourChangeHelper.updateElementColourClass(this.selectBoxes[i], this.selectBoxes[i].value)
    }
  },

  addSelectChangeEvents: function () {

    $(this.selectBoxes).change(function (event) {

      dynamicSelectBoxSet.selectBoxChange(event)

    });

  }

};
