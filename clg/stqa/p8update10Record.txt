import jxl.Cell;
import jxl.Sheet;
import jxl.Workbook;
import jxl.read.biff.BiffException;
//Code to update 10 student records into table into Excel file 
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;
import jxl.*;
import jxl.read.*;
import jxl.write.*;
import java.io.*;

public class updatestudrecords {
	@BeforeClass
	public void f1()
	{}
	@Test
	public void testImportexport1() throws Exception {
	FileInputStream fi = new FileInputStream("D:\\selenium pracs\\myBook1.xls");
	Workbook w = Workbook.getWorkbook(fi);
	Sheet s = w.getSheet(0);
	String a[][] = new String[s.getRows()][s.getColumns()];
	FileOutputStream fo = new FileOutputStream("D:\\selenium pracs\\myBook1res.xls");
	WritableWorkbook wwb = Workbook.createWorkbook(fo);
	WritableSheet ws = wwb.createSheet("result1", 0);
	for (int i = 0; i < s.getRows(); i++)
	for (int j = 0; j < s.getColumns(); j++)
	{
	a[i][j] = s.getCell(j, i).getContents();
	Label l2 = new Label(j, i, a[i][j]);
	ws.addCell(l2);
	Label l1 = new Label(6, 0, "Result");
	ws.addCell(l1);
	}
	for (int i = 1; i < s.getRows(); i++) {
		for (int j = 2; j < s.getColumns(); j++)
		{
		a[i][j] = s.getCell(j, i).getContents();
		int x=Integer.parseInt(a[i][j]);
		if(x > 35)
		{
		Label l1 = new Label(6, i, "pass");
		ws.addCell(l1);
		}
		else
		{
		Label l1 = new Label(6, i, "fail");
		ws.addCell(l1);
		break;   } 		}
		}
		wwb.write();
		wwb.close(); 
    }
}
