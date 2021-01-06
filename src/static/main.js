
let url = "/compute";

let button = document.getElementById('button');
let textbox = document.getElementById('textbox');

button.onclick = function(){
  let text = document.getElementById('textbox').value;
    $.ajax({
      url: url,
      method: "POST",
      data: {text: text},
      success: function(result, status){
        console.log(result);
        let p = document.getElementById('quote');
        if (result[0].quote == ""){
          p.innerHTML = "...";
        }
        else {
          p.innerHTML = "`" + result[0].quote + "'";
        }
        console.log(result[0].quote);
      },
      error: function(err){
        console.log(err);
      }
    })
  document.getElementById('textbox').value = ""
};
