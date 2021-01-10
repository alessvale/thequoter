
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
        let p2 = document.getElementById('author');
        if (result[0].quote[0] == ""){
          p.innerHTML = "...";
          p2.innerHTML = "";
        }
        else {
          p.innerHTML = "`" + result[0].quote[0] + "'";
          p2.innerHTML = result[0].quote[1]
        }
        console.log(result[0].quote[0]);
      },
      error: function(err){
        console.log(err);
      }
    })
  document.getElementById('textbox').value = ""
};
