Attribute VB_Name = "Module2"
Sub Stock_Data_Analyzer()
  For Each ws In Worksheets
  ws.Cells(1, 9).Value = "Ticker"
  ws.Cells(1, 10).Value = "Yearly Change"
  ws.Cells(1, 11).Value = "Percent Change"
  ws.Cells(1, 12).Value = "Total Stock Volume"
  ws.Cells(1, 9).WrapText = True
  ws.Cells(1, 10).WrapText = True
  ws.Cells(1, 11).WrapText = True
  ws.Cells(1, 12).WrapText = True
  ws.Cells(1, 9).Font.Bold = True
  ws.Cells(1, 10).Font.Bold = True
  ws.Cells(1, 11).Font.Bold = True
  ws.Cells(1, 12).Font.Bold = True
  ws.Cells(1, 9).Font.Underline = True
  ws.Cells(1, 10).Font.Underline = True
  ws.Cells(1, 11).Font.Underline = True
  ws.Cells(1, 12).Font.Underline = True
  Dim openStock As Double
  Dim closeStock As Double
  Dim Ticker As String
  Dim OutputRow As String
  Dim Total_Volume As Double
  OutputRow = 2
  Total_Volume = 0
  Dim lastRow As Long
  lastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row
  Ticker = ws.Cells(2, 1).Value
  openStock = ws.Cells(2, 3).Value
  For i = 2 To lastRow
      If (Ticker <> ws.Cells(i, 1).Value) Then
        closeStock = ws.Cells(i - 1, 6).Value
        ws.Cells(OutputRow, 10).Value = closeStock - openStock
          If ws.Cells(OutputRow, 10).Value >= 0 Then
            ws.Cells(OutputRow, 10).Interior.ColorIndex = 4
            Else
            ws.Cells(OutputRow, 10).Interior.ColorIndex = 3
          End If
        ws.Cells(OutputRow, 10).NumberFormat = "#,##0.00;-#,##0.00"
        ws.Cells(OutputRow, 9).Value = Ticker
        If openStock <> 0 Then
            ws.Cells(OutputRow, 11).Value = (closeStock - openStock) / openStock
            ws.Cells(OutputRow, 11).NumberFormat = "0.00%;[red]-0.00%"
        End If
        ws.Cells(OutputRow, 12).Value = Total_Volume
        ws.Cells(OutputRow, 12).NumberFormat = "#,##"
        Ticker = ws.Cells(i, 1).Value
        openStock = ws.Cells(i, 3).Value
        OutputRow = OutputRow + 1
        Total_Volume = ws.Cells(i, 7).Value
        ElseIf (Ticker = ws.Cells(i, 1).Value) Then
        Total_Volume = Total_Volume + ws.Cells(i, 7).Value
    End If
  Next i
  ws.Cells(1, 15).Value = "Ticker"
  ws.Cells(1, 16).Value = "Value By Iteration"
  ws.Cells(1, 17).Value = "Value By Formula"
  ws.Cells(2, 14).Value = "Greatest % Increase"
  ws.Cells(3, 14).Value = "Greatest % Decrease"
  ws.Cells(4, 14).Value = "Greatest Total Volume"
  ws.Cells(2, 17).Value = WorksheetFunction.Max(ws.Range("K2:K" & OutputRow))
  ws.Cells(2, 17).NumberFormat = "0.00%;[red]-0.00%"
  ws.Cells(3, 17).Value = WorksheetFunction.Min(ws.Range("K2:K" & OutputRow))
  ws.Cells(3, 17).NumberFormat = "0.00%;[red]-0.00%"
  ws.Cells(4, 17).Value = WorksheetFunction.Max(ws.Range("L2:L" & OutputRow))
  ws.Cells(4, 17).NumberFormat = "#,##"
  ws.Cells(1, 15).WrapText = True
  ws.Cells(1, 16).WrapText = True
  ws.Cells(1, 17).WrapText = True
  ws.Cells(1, 15).Font.Bold = True
  ws.Cells(1, 16).Font.Bold = True
  ws.Cells(1, 17).Font.Bold = True
  ws.Cells(1, 15).Font.Underline = True
  ws.Cells(1, 16).Font.Underline = True
  ws.Cells(1, 17).Font.Underline = True
  ws.Cells(4, 14).EntireColumn.ColumnWidth = 18.75
  Dim Ticker_Max_Increase As String
  Dim Ticker_Max_Decrease As String
  Dim Ticker_Max_Volume As String
  Dim Max_Increase As Double
  Dim Max_Decrease As Double
  Dim Max_Volume As Double
  Ticker_Max_Increase = ws.Cells(2, 9).Value
  Max_Increase = ws.Cells(2, 11).Value
  Ticker_Max_Decrease = ws.Cells(2, 9).Value
  Max_Decrease = ws.Cells(2, 11).Value
  Ticker_Max_Volume = ws.Cells(2, 9).Value
  Max_Volume = ws.Cells(2, 12).Value
  For t = 3 To OutputRow
    If (ws.Cells(t, 11).Value > Max_Increase) Then
        Max_Increase = ws.Cells(t, 11).Value
        Ticker_Max_Increase = ws.Cells(t, 9).Value
    End If
    If (ws.Cells(t, 11).Value < Max_Decrease) Then
        Max_Decrease = ws.Cells(t, 11).Value
        Ticker_Max_Decrease = ws.Cells(t, 9).Value
    End If
    If (ws.Cells(t, 12).Value > Max_Volume) Then
        Max_Volume = ws.Cells(t, 12).Value
        Ticker_Max_Volume = ws.Cells(t, 9).Value
    End If
  Next t
  ws.Cells(2, 15).Value = Ticker_Max_Increase
  ws.Cells(3, 15).Value = Ticker_Max_Decrease
  ws.Cells(4, 15).Value = Ticker_Max_Volume
  ws.Cells(2, 16).Value = Max_Increase
  ws.Cells(2, 16).NumberFormat = "0.00%;[red]-0.00%"
  ws.Cells(3, 16).Value = Max_Decrease
  ws.Cells(3, 16).NumberFormat = "0.00%;[red]-0.00%"
  ws.Cells(4, 16).Value = Max_Volume
  ws.Cells(4, 16).NumberFormat = "#,##"
  Next ws
End Sub
