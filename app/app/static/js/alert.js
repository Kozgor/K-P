function pageLoad(){
    var closebutton = document.getElementById('closebtn');
    closebutton.addEventListener("click", function(){
        document.getElementById('alertmessage').style.display="none";
        })
    }

    function closeAlert() {
        document.getElementById('alertmessage').style.display="none";
      }
      setTimeout(closeAlert, 5000);

pageLoad();

