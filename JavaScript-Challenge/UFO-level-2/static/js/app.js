// from data.js
var tableData = data;

// Select the button
var button = d3.select("#filter-btn");
var button2 = d3.select("#filter-btn2");
var button3 = d3.select("#filter-btn3");
var button4 = d3.select("#reset-btn");
// Create event handlers 
button.on("click", runEnter);
// button.on("click", radioChosen);
button2.on("click", runStateOrProvince);
button3.on("click", runCitySearch);
button4.on("click", runReset);
// YOUR CODE HERE!
// Get a reference to the table body
var tbody = d3.select("tbody");
 
// Console.log the weather data from data.js
console.log(tableData);

// Step 1: Loop Through `data` and console.log each weather report object
function createTable(currentData){
    tbody.html("");
    currentData.forEach(function(RC){
    console.log(RC)
    var row = tbody.append('tr');
    
    Object.entries(RC).forEach(function ([x,y] ) {
        console.log(`x is ${x} y is ${y}`)
        row.append('td').text(y);
    })
});
}
createTable(tableData)


function runEnter() {

    // Prevent the page from refreshing
    d3.event.preventDefault();
    
    // Select the input element and get the raw HTML node
    var inputElement = d3.select("#datetime");
    console.log(inputElement);
  
    // Get the value property of the input element
    var inputValue = inputElement.property("value");
  
    console.log(inputValue);
    console.log(tableData);
  
    var filteredData = tableData.filter(tableData => tableData.datetime === inputValue);
  
    console.log(filteredData);
        
    createTable(filteredData)
};

function order(){
    // Get variables
    var chkus = document.getElementById("chkus");
    var chkca = document.getElementById("chkca");
    var output = document.getElementById("output");
    var result = "<ul> "
    if (chkus.checked){
        result += "<li>" + chkus.value + "</li> ";
    } // end if
    if (chkca.checked){
        result += "<li>" + chkca.value + "</li> ";
    } // end if
    result += "</ul> "
    output.innerHTML = result;

    // filtering table based on country or countries chosen or not chosen
    if (chkus.checked && chkca.checked) {
        createTable(tableData);
    }
    else if (chkus.checked) {
        // inputCountry = "us";
        var filteredData = tableData.filter(tableData => tableData.country === "us");
        createTable(filteredData);
        // radioChosen(inputCountry);
        return;
    } 
    else if (chkca.checked) {
        // inputCountry = "ca";
        var filteredData = tableData.filter(tableData => tableData.country === "ca");
        createTable(filteredData);
        // radioChosen(inputCountry);
        return;
    }
    else tbody.html("");
} // end function

function radioChosen() {
    // Prevent the page from refreshing
    d3.event.preventDefault();

    // Select the input element and get the raw HTML node
    var inputRadio = d3.select("#country");
    console.log(inputRadio);

    // Get the value property of the input element
    var inputValue = inputRadio.property("value");

    console.log(inputValue);
    console.log(tableData);

    var filteredData = tableData.filter(tableData => tableData.country === inputCountry);

    console.log(filteredData);

    createTable(filteredData)
};

/* $("input[type=radio]").change(function(){
    var filter = this.value;
    if (filter == "All")
        $("tr.dataRow").css("visibility", "visible");
    else $("tr.dataRow").css("visibility", "collapse");
    var matchFound = false;
    $("tr.dataRow").find("td").each(function() {
        $this = $(this);
        if (!matchFound){
            if ($this.html() == filter){
                matchFound = true;
                $this.parent().css("visibility", "visible");
            }
        }
    });
}); */

function runStateOrProvince() {

    // Prevent the page from refreshing
    d3.event.preventDefault();
    
    // Select the input element and get the raw HTML node
    var inputElement = d3.select("#state");
    console.log(inputElement);
  
    // Get the value property of the input element
    var inputValue = inputElement.property("value").toLowerCase().trim();
  
    console.log(inputValue);
    console.log(tableData);
  
    var filteredData = tableData.filter(tableData => tableData.state === inputValue);
  
    console.log(filteredData);
        
    createTable(filteredData)
};

function runCitySearch() {

    // Prevent the page from refreshing
    d3.event.preventDefault();
    
    // Select the input element and get the raw HTML node
    var inputElement = d3.select("#city");
    console.log(inputElement);
  
    // Get the value property of the input element
    var inputValue = inputElement.property("value").toLowerCase().trim();
  
    console.log(inputValue);
    console.log(tableData);
  
    var filteredData = tableData.filter(tableData => tableData.city === inputValue);
  
    console.log(filteredData);
        
    createTable(filteredData)
};

function runReset() {
    d3.event.preventDefault();
    tbody.html("");
    createTable(tableData)
};