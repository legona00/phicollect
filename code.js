function doGet() {
    return HtmlService.createTemplateFromFile('Index').evaluate();
  }
  
  //GET DATA FROM GOOGLE SHEET AND RETURN AS AN ARRAY
  function getData() {
    var spreadSheetId = "1dAp23VEsPozpfNaPWapNMzQyC9oXwdAOPl6fa29h6Fg"; //CHANGE
    var dataRange = "Sorted!A1:C"; //CHANGE
  
    var range = Sheets.Spreadsheets.Values.get(spreadSheetId, dataRange);
    var values = range.values;
    Logger.log(values)
    return values;
  }
  
  function include(filename) {
    return HtmlService.createHtmlOutputFromFile(filename)
      .getContent();
  }
