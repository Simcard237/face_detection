
var i;
i=setInterval(function (){
    fetch('testapi/')
    .then(response => response.json())
    .then(resp => {
        console.log(resp)
     if (resp.message===1){   
       console.log(resp); //output=> {"message":"VALUE_OF_MESSAGE"}
       content='<div class="item"><ul>'+
         '<li><h4>id User</h4><span>'+ resp.iduser+'</span></li>'+
         '<li><h4>Name</h4><span>'+resp.name+'</span></li>'+
         '<li><h4>Date</h4><span>'+resp.date+'</span></li>'+
         '<li><h4>Hour</h4><span>'+resp.hours+'</span></li>'+
       '</ul>'+
    ' </div>'
       
     
     document.getElementById("table").insertAdjacentHTML("beforeend",content)
    }
       
      });
},1000); 


