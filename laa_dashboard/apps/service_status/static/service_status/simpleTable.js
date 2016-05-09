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
  statusField : "manual_status",
  tableElementId : "status_table",
  tableElement : undefined,

  notesRowElementID: "notes_row",
  notesElementsClass : "notes_div",
  notesTextElementsClass: "notes_text",
  activeNotesElements: [],
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


  setUseAuto: function () {
    this.useAuto = this.getParameterWithDefault("use_auto", this.useAuto);
  },

  setShowNotes: function () {
    this.showNotes = this.getParameterWithDefault("show_notes", this.showNotes);
  },


  setStatusField: function () {
    if (this.useAuto) {
      this.statusField = "auto_status";
    }
    else {
      this.statusField = "manual_status";
    }
  },


  setTableElement: function () {
    this.tableElement = document.getElementById(this.tableElementId);
  },

  setTableDimensions: function () {

    this.width = this.getParameterWithDefault("width", this.width);
    this.height = this.getParameterWithDefault("height", this.height);
    this.notesHeight = this.getParameterWithDefault("notes_height", this.notesHeight);

    // var widthArg;
    // var heightArg;
    //
    // var widthArgLength;
    // var heightArgLength;
    //
    // var lastWidthChar;
    // var lastHeightChar;
    //
    // var widthArgValue;
    // var heightArgValue;
    //
    // widthArg = this.getParameterWithDefault("width");
    // heightArg = this.getParameterWithDefault("height");
    //
    // widthArgLength = widthArg.length;
    // heightArgLength = heightArg.length;
    //
    // lastWidthChar = widthArg.substr(widthArgLength - 1);
    // lastHeightChar = heightArg.substr(heightArgLength - 1);
    //
    // if (lastWidthChar == "%") {
    //   widthArgValue = widthArg.substr(0, widthArgLength - 1);
    //   va
    // }
    // else {
    //
    // }
    //
    // if (lastHeightChar == "%") {
    //   heightArgValue = heightArg.substr(0, heightArgLength - 1);
    // }
    // else {
    //
    // }

  },

  setNotesFontSize: function () {
    this.fontSize = this.getParameterWithDefault("notes_font", this.notesFontSize);
  },


  setupNotesElements: function () {

    var allNotesElements = document.getElementsByClassName(this.notesElementsClass);

    for (var i = 0; i < allNotesElements.length; i++) {

      allNotesElements[i].style.fontSize = this.notesFontSize;
      allNotesElements[i].style.height = this.notesHeight;

      var noteText = allNotesElements[i].getElementsByClassName(this.notesTextElementsClass)[0];

      var isEmpty = $(noteText).is(':empty');

      if (!isEmpty) {
          allNotesElements[i].style.fontSize = this.notesFontSize;
          this.activeNotesElements.push(allNotesElements[i]);
      }

    }
  },


  setupTable: function () {
    this.tableElement.style.width = this.width;
    this.tableElement.style.height = this.height;


    if (this.showNotes == true) {

      this.activeNotesElements[this.currentNote].style.display = "block";

    }


  },


  updateSimpleTableElements: function (response, type_class) {

    $.each(response, function (index, response_item) {

      var named_elements = document.getElementsByClassName(response_item.name);

      $.each(named_elements, function (index, named_element) {

        if ($(named_element).hasClass(type_class)) {
          colourChangeHelper.updateElementColourClass(named_element, response_item[simpleTable.statusField]);
        }

      });

    });

  },


  getStatuses: function () {
    console.log("Get statuses request made");
    $.ajax({
      url: "/services/get_statuses/",
      type: "GET",

      success: function (json) {
        simpleTable.updateSimpleTableElements(json, "manual_status_cell");
        colourChangeHelper.setElementColours();

      },

      error: function (xhr, errmsg, err) {
        console.log(xhr.status + ": " + xhr.responseText);
      }

    });
  },


  startAutoRefresh : function () {

    window.setInterval(this.getStatuses, 5000);
    window.setInterval(this.switchNote, 10000);

  },


  switchNote : function () {

    if (simpleTable.showNotes) {

      simpleTable.activeNotesElements[simpleTable.currentNote].style.display = "none";

      if (simpleTable.currentNote < (simpleTable.activeNotesElements.length - 1)) {
        simpleTable.currentNote++;
      }
      else {
        simpleTable.currentNote = 0;
      }

      simpleTable.activeNotesElements[simpleTable.currentNote].style.display = "block";

    }

  },


  init : function () {

    this.setUseAuto();
    this.setShowNotes();
    this.setStatusField();
    this.setTableElement();
    this.setTableDimensions();
    this.setNotesFontSize();

    //setupNotesElements and setupTable must be run after all the get elements.
    this.setupNotesElements();
    this.setupTable();
    this.startAutoRefresh();

  }


};



