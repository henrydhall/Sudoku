function copyReduced() 
{
    // Get the text field
    var copyText = document.getElementById("reduced_puzzle");
  
     // Copy the text inside the text field
    navigator.clipboard.writeText(copyText.textContent);
  
    // Alert the copied text
    alert("Copied the reduced puzzle: " + copyText.textContent);
} 