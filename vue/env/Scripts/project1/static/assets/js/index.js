
var i;
i=setInterval(function (){
    fetch('testapi/')
    .then(response => response.json())
    .then(resp => {
       console.log(resp); //output=> {"message":"VALUE_OF_MESSAGE"}
       let message=resp.message;
       
       if (message===1){
        document.getElementById("success").setAttribute("style","display:block")
        document.querySelector('.img1').setAttribute("id","reload"); 
       };
       if (message===2){
        
        document.getElementById("error").setAttribute("style","display:inline")
        document.querySelector('.img1').setAttribute("id","reload"); 
       
       
       };
       
      });
},1000); 


