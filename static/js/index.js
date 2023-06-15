function dropDownFunction(listID) {

    if (document.getElementById(listID).style.display === "none") {
    document.getElementById(listID).style.display = "block";
    }else if(document.getElementById(listID).style.display === ""){
    document.getElementById(listID).style.display = "block";
    }else {
    document.getElementById(listID).style.display = "none";
    }

}

function copyEmail() {
  // Get the text field
//  var copyText = document.getElementById("myEmail");

  // Select the text field
//  copyText.select();
//  copyText.setSelectionRange(0, 99999); // For mobile devices

   // Copy the text inside the text field
  navigator.clipboard.writeText("christ@kallas2.com");

  // Alert the copied text
  alert("Copied the text: christ@kallas2.com");
}