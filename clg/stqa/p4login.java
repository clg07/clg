package package1;
import java.util.concurrent.TimeUnit;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.testng.Assert;
import org.testng.annotations.AfterMethod;
import org.testng.annotations.DataProvider;
import org.testng.annotations.Test;
import org.openqa.selenium.firefox.FirefoxDriver;

//import DDT.FirefoxDriver;
public class WordPressNew {
	FirefoxDriver driver; //global variable
	@Test(dataProvider="wordpressData")
	public void loginToWordpress(String username,String password) throws InterruptedException
	{
	System.setProperty("webdriver.gecko.driver", "E:\\seleniumsettings\\gecko\\geckodriver.exe");
	//FirefoxDriver driver = new FirefoxDriver(); as its local , to make it global has been mentioned above
	driver = new FirefoxDriver();
	driver.manage().window().maximize();
	driver.manage().timeouts().implicitlyWait(20,TimeUnit.SECONDS);
	driver.get("http://demosite.center/wordpress/wp-login.php");
	driver.findElement(By.id("user_login")).sendKeys("username");
	driver.findElement(By.id("user_pass")).sendKeys("password");
	driver.findElement(By.xpath("//*[@id=\"wp-submit\"]")).click();
	Thread.sleep(5000);
	//System.out.println(driver.getTitle());
	//till here it will show 3 runs and 0 failures for admin1, admin2 and admin3 until we dont provide any validations, 
	//the task would depend on script
	//for this we will use assert to show validations
	Assert.assertTrue(driver.getTitle().contains("Dashboard"),"User is not able to login:invalid Credential");
	//if above assertion failes then only User is not able to login would be printed
	System.out.println("Page title is verified:User is able to login successfullly");
	}	
	@AfterMethod
	public void tearDown() //if testcase fails then teardown() would get exec
	{
		driver.quit();
	}
	@DataProvider(name="wordpressData")

public Object[][] passData() // give atleast one  username/password which is a running...
{
	Object[][] data=new Object[3][2];
	data[0][0]="admin1";
	
	data[0][1]="demo1";
	data[1][0]="admin";
	data[1][1]="demo123";
	data[2][0]="admin2";
	data[0][1]="admin1234";
	return data;
}
}
