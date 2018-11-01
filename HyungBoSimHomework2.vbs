Sub Easy():


Dim TotalVolumeOfStock As Double

Range("H1").Value = "Ticker"
Range("I1").Value = "Total Stock Volume"

Numberofrows = Cells(Rows.Count, 1).End(xlUp).Row


For i = 3 To Numberofrows

    If Cells(i, 1).Value <> Cells(i - 1, 1).Value Then
   


        Range("H" & j + 2).Value = Cells(i - 1, 1).Value
      
        Range("I" & j + 2).Value = TotalVolumeOfStock
     
        TotalVolumeOfStock = TotalVolumeOfStock + Cells(i - 1, 7).Value
       
        TotalVolumeOfStock = 0
       
        j = j + 1
     
    Else
        TotalVolumeOfStock = TotalVolumeOfStock + Cells(i, 7).Value

    End If

Next i

End Sub
