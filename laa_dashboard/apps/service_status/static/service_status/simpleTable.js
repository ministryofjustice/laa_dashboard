/**
 * Created by jamesnarey on 06/05/2016.
 */

var simpleTable = {

  width : 200,
  height : 400,
  useAuto : false,
  showNotes : true,
  // notesHeight : 150,
  notesFontSize : 10,
  statusField : "manual_status",
  tableElementId : "status_table",
  tableElement : undefined,
  scrollBoxElementId: "notes_scroll_cell",
  scrollBoxElement: undefined,

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
    var useAutoParam = this.getParameterByName("use_auto");
    return (useAutoParam != null && useAutoParam.toLowerCase() === 'true');
  },

  getStatusField: function () {
    if (this.useAuto) {
      this.statusField = "auto_status";
    }
    else {
      this.statusField = "manual_status";
    }
  },

  getTableElement: function () {
    this.tableElement = document.getElementById(this.tableElementId);
  },

  getScrollBoxElement: function () {
    this.scrollBoxElement = document.getElementById(this.scrollBoxElementId);
  },

  setupTable: function () {
    this.tableElement.style.width = this.width;
    this.tableElement.style.height = this.height;
    // this.scrollBoxElement.style.height = this.notesHeight;
    this.scrollBoxElement.style.fontSize = this.notesFontSize;
  },

  updateSimpleTableElements: function (response, type_class) {

    $.each(response, function (index, response_item) {

      var named_elements = document.getElementsByClassName(response_item.name);
      // console.log(response_item.name);

      $.each(named_elements, function (index, named_element) {

        if ($(named_element).hasClass(type_class)) {
          // console.log(response_item[simpleTable.statusField]);
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
        // console.log(json);
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
    // window.setInterval(this.scrollNotes, 50);

  },

  // scrollNotes : function () {
  //
  //   if (simpleTable.scrollBoxElement.scrollTop < simpleTable.scrollBoxElement.scrollHeight - simpleTable.scrollBoxElement.offsetHeight - 1) {
  //
  //     simpleTable.scrollBoxElement.scrollTop = simpleTable.scrollBoxElement.scrollTop + 1
  //   }
  //   else {
  //     simpleTable.scrollBoxElement.scrollTop = 0;
  //   }
  //   console.log("Scroll_box")
  // },

  init : function () {

    this.setUseAuto();
    this.getStatusField();
    this.getTableElement();
    this.getScrollBoxElement();
    this.setupTable();
    this.startAutoRefresh();

  }


};



