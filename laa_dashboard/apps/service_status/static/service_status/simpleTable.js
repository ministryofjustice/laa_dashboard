/**
 * Created by jamesnarey on 06/05/2016.
 */

var simpleTable = {

  width : "200px",
  height : "400px",
  useAuto : false,
  showNotes : true,
  notesHeight : "150px",
  notesFontSize : 12,
  statusFontSize: 14,

  headerElementID: "header",
  headerElement: undefined,
  statusIndicatorClass: "status_cell",
  statusIndicatorElements: undefined,
  tableElementID : "status_table",
  tableElement : undefined,
  notesRowElementID: "notes_row",
  notesRowElement: undefined,
  notesDivID : "notes_div",
  notesDiv: undefined,
  notesHeadingElementID: "notes_heading",
  notesHeadingElement: undefined,
  notesTextElementID: "notes_text",
  notesTextElement: undefined,

  statusJSONField : "manual_status",
  serviceData: [],
  activeNotes: [],
  currentNote: 0,




  getParameterWithDefault: function (paramName, defaultValue) {
    var paramCheck = this.getParameterByName(paramName);
    if (paramCheck != ("" || null)) {

      if (paramCheck === "true") {return true}
      else if (paramCheck === "false") {return false}
      else {return paramCheck}

    }
    else {
      return defaultValue;
    }
  },


  getParameterByName: function (name) {

    var url = window.location.href;
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
      results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';

    return decodeURIComponent(results[2].replace(/\+/g, " "));
  },


  getParams: function () {
    this.useAuto = this.getParameterWithDefault("use_auto", this.useAuto);
    this.showNotes = this.getParameterWithDefault("show_notes", this.showNotes);
    this.width = this.getParameterWithDefault("width", this.width);
    this.height = this.getParameterWithDefault("height", this.height);
    this.notesHeight = this.getParameterWithDefault("notes_height", this.notesHeight);
    this.fontSize = this.getParameterWithDefault("notes_font", this.notesFontSize);
    this.statusFontSize = this.getParameterWithDefault("status_font", this.statusFontSize);
  },


  setStatusField: function () {
    if (this.useAuto) {
      this.statusJSONField = "auto_status";
    }
    else {
      this.statusJSONField = "manual_status";
    }
  },


  setElements: function () {
    this.tableElement = document.getElementById(this.tableElementID);
    this.notesRowElement = document.getElementById(this.notesRowElementID);
    this.notesDiv = document.getElementById(this.notesDivID);
    this.notesHeadingElement = document.getElementById(this.notesHeadingElementID);
    this.notesTextElement = document.getElementById(this.notesTextElementID);
    this.statusIndicatorElements = document.getElementsByClassName(this.statusIndicatorClass);
    this.headerElement = document.getElementById(this.headerElementID);
  },


  setActiveNotes: function () {

    simpleTable.activeNotes = [];

    for (var i = 0; i < simpleTable.serviceData.length; i++) {

      var noteText = simpleTable.serviceData[i].notes;

      if (noteText != "") {

          simpleTable.activeNotes.push({ name: simpleTable.serviceData[i].name,
                                         notes: simpleTable.serviceData[i].notes
                                      });
      }

    }
  },


  setupTable: function () {
    this.tableElement.style.width = this.width;
    this.tableElement.style.height = this.height;

    this.headerElement.style.fontSize = this.statusFontSize;

    for (var i = 0; i < this.statusIndicatorElements.length; i++) {

      this.statusIndicatorElements[i].style.fontSize = this.statusFontSize;

    }

    this.notesDiv.style.height = this.notesHeight;
    this.notesDiv.style.width = this.width;
    this.notesDiv.style.fontSize = this.fontSize;


    if (this.showNotes == true) {

      simpleTable.notesRowElement.style.display = "block";

    }


  },


  updateIndicatorElements: function () {

    $.each(simpleTable.serviceData, function (index, response_item) {

      var named_elements = document.getElementsByClassName(response_item.name);

      $.each(named_elements, function (index, named_element) {

        if ($(named_element).hasClass(simpleTable.statusIndicatorClass)) {
          colourChangeHelper.updateElementColourClass(named_element, response_item[simpleTable.statusJSONField]);
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
        simpleTable.serviceData = json;
        simpleTable.updateIndicatorElements();
        simpleTable.setActiveNotes();
        colourChangeHelper.setElementColours();

      },

      error: function (xhr, errmsg, err) {
        console.log(xhr.status + ": " + xhr.responseText);
      }

    });
  },


  startAutoRefresh : function () {

    window.setInterval(this.getData, 5000);
    window.setInterval(this.switchNote, 3000);

  },


  switchNote : function () {

    if (simpleTable.showNotes && simpleTable.activeNotes != []) {


      if (simpleTable.currentNote < (simpleTable.activeNotes.length - 1)) {
        simpleTable.currentNote++;
      }
      else {
        simpleTable.currentNote = 0;
      }

      simpleTable.notesHeadingElement.innerHTML = simpleTable.activeNotes[simpleTable.currentNote].name;
      simpleTable.notesTextElement.innerHTML = simpleTable.activeNotes[simpleTable.currentNote].notes;

    }

  },


  init : function () {

    this.getParams();
    this.setElements();
    this.setStatusField();

    //setActiveNotes and setupTable must be run after all the get elements.
    this.setupTable();
    this.getData();
    this.startAutoRefresh();

  }


};


//Run on page load
$(document).ready(function () {

  simpleTable.init()


});
