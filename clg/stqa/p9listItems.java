<select id="continents">
<option value="Asia">Asia</option>
<option value="Europe">Europe</option>
<option value="Africa">Africa</option>
</select>


import java.util.List;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.openqa.selenium.firefox.*;
import org.openqa.selenium.firefox.FirefoxOptions;
import org.openqa.selenium.firefox.FirefoxProfile;
import org.openqa.selenium.firefox.internal.ProfilesIni;
import org.openqa.selenium.support.ui.Select;
public class ComboBox {
static String driverPath = "C:\\Users\\Usman\\503\\geckodriver.exe";
public static void main(String[] args) {
 System.setProperty("webdriver.gecko.driver",driverPath);
 //NOTE THAT: following commented lines are required for old machines
 //DesiredCapabilities capabilities = DesiredCapabilities.firefox();
 //capabilities.setCapability("marionette",true);
 //ProfilesIni allProfiles = new ProfilesIni();
 //FirefoxProfile fp = new FirefoxProfile();
 //fp.setPreference(FirefoxProfile.PORT_PREFERENCE,"7055");
 //FirefoxOptions options = new FirefoxOptions();
 //options.setProfile(fp);
WebDriver driver = new FirefoxDriver();
String appUrl ="https://www.toolsqa.com/automation-practice-form/";
//DYNAMIC URL(WEBSITE)
//String appUrl = "file:///D:/Usman/College/503%20pracs/combobox.html"; //STATIC URL(LOCAL FILE)

driver.get(appUrl);
Select oSelect = new Select(driver.findElement(By.id("continents")));
//Select oSelect = new Select(driver.findElement(By.tagName("select"))); //this works too
List<WebElement> oSize = oSelect.getOptions();
int iListSize = oSize.size();
for(int i =0; i < iListSize ; i++)
{
// Storing the value of the option
String sValue = oSelect.getOptions().get(i).getText();
// Printing the stored value
System.out.println(sValue);
}
System.out.println("Total No. Items in Dropdown: "+iListSize);
//driver.quit();
}
}
