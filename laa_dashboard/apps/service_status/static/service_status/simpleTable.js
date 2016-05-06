/**
 * Created by jamesnarey on 06/05/2016.
 */

var simpleTable = {

  width : 200,
  height : 400,
  useAuto : false,
  showNotes : true,
  notesHeight : 150,
  notesFontSize : 10,
  statusField : "manual_status",
  tableElementId : "status_table",
  tableElement : undefined,

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

  setupTable: function () {
    this.tableElement.style.width = this.width;
    this.tableElement.style.height = this.height;
  },

  updateSimpleTableElements: function (response, type_class) {

    $.each(response, function (index, response_item) {

      var named_elements = document.getElementsByClassName(response_item.name);
      console.log(response_item.name);

      $.each(named_elements, function (index, named_element) {

        if ($(named_element).hasClass(type_class)) {
          console.log(response_item[simpleTable.statusField]);
          colourChangeHelper.updateElementColourClass(named_element, response_item[simpleTable.statusField]);
        }

      });

    });

  },

  getStatuses: function () {
    console.log("Get statuses request made")
    $.ajax({
      url: "/services/get_statuses/",
      type: "GET",

      success: function (json) {
        console.log(json);
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

  },

  init : function () {

    this.setUseAuto();
    this.getStatusField();
    this.getTableElement();
    this.setupTable();
    this.startAutoRefresh();

  }


};



