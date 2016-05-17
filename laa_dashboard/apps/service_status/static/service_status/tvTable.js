/**
 * Created by jamesnarey on 17/05/2016.
 */

/**
 * Created by jamesnarey on 06/05/2016.
 */

var tvTable = {

  tableElementID : "status_table",
  tableElement : undefined,

  notesCellClass: "notes_cell",
  notesCellElements: undefined,
  statusJSONField: 'manual_status',
  statusIndicatorClass: "manual_status_cell",
  notesField : "notes",
  serviceData: [],


  setElements: function () {
    this.tableElement = document.getElementById(this.tableElementID);
    this.statusIndicatorElements = document.getElementsByClassName(this.statusIndicatorClass);
    this.notesCellElements = document.getElementsByClassName(this.notesCellClass);
  },


  updateIndicatorElements: function () {

    $.each(tvTable.serviceData, function (index, response_item) {

      var named_elements = document.getElementsByClassName(response_item.name);

      $.each(named_elements, function (index, named_element) {

        if ($(named_element).hasClass(tvTable.statusIndicatorClass)) {
          colourChangeHelper.updateElementColourClass(named_element, response_item[tvTable.statusJSONField]);
        }

      });

    });

  },

  updateNotes: function () {

    $.each(tvTable.serviceData, function (index, response_item) {
      //console.log(response_item);
      var named_elements = document.getElementsByClassName(response_item.name);

      $.each(named_elements, function (index, named_element) {

        if ($(named_element).hasClass(tvTable.notesCellClass)) {
          console.log(response_item[tvTable.notesField]);
          named_element.innerHTML = response_item[tvTable.notesField];
          //colourChangeHelper.updateElementColourClass(named_element, response_item[tvTable.statusJSONField]);
        }

      });

    });
  },


  getData: function () {
    console.log("Get statuses request made");
    $.ajax({
      url: "/services/get_statuses/",
      type: "GET",

      success: function (json) {
        tvTable.serviceData = json;
        tvTable.updateIndicatorElements();
        tvTable.updateNotes();
        colourChangeHelper.setElementColours();

      },

      error: function (xhr, errmsg, err) {
        console.log(xhr.status + ": " + xhr.responseText);
      }

    });
  },


  startAutoRefresh : function () {

    window.setInterval(this.getData, 5000);

  },



  init : function () {


    this.setElements();


    //setActiveNotes and setupTable must be run after all the get elements.

    this.getData();
    this.startAutoRefresh();

  }


};


//Run on page load
$(document).ready(function () {

  tvTable.init()


});
