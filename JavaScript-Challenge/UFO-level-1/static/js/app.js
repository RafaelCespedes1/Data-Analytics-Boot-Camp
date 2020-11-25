// from data.js
var tableData = data;

// Select the button
var button = d3.select("#filter-btn");

// Create event handlers 
button.on("click", runEnter);

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