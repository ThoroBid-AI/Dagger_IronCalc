// Google Sheets Apps Script
// Purpose: Replace all formulas with their current values (freeze results).
function freezeAllValues() {
  const ss = SpreadsheetApp.getActive();
  ss.getSheets().forEach((sheet) => {
    const range = sheet.getDataRange();
    range.copyTo(range, { contentsOnly: true });
  });
}
