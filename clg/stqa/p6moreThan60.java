import jxl.*;
import jxl.read.*;
import jxl.write.*;
import java.io.*;
import org.testng.annotations.Test;
public class countstuds {
	@Test
	public void testImportexport1() throws Exception {
	FileInputStream fi = new FileInputStream("D:\\selenium pracs\\myBook1.xls");
	Workbook w = Workbook.getWorkbook(fi);
	Sheet s = w.getSheet(0);
	String a[][] = new String[s.getRows()][s.getColumns()];
	FileOutputStream fo = new FileOutputStream("D:\\selenium pracs\\countBook1res.xls");
	WritableWorkbook wwb = Workbook.createWorkbook(fo);
	WritableSheet ws = wwb.createSheet("result", 0);
	int c=0;
	for (int i = 0; i < s.getRows(); i++) {
	for (int j = 0; j < s.getColumns(); j++)
	{
	if(i >= 1)
	{ 	String b= new String();
	b=s.getCell(3,i).getContents();
	int x= Integer.parseInt(b);
	if( x < 60)
	{ 	c++;
	break;   	}
	}
	a[i][j] = s.getCell(j, i).getContents();
	Label l2 = new Label(j, i-c, a[i][j]);
	ws.addCell(l2);
	}    }
	wwb.write();
	wwb.close();
	}     
}
