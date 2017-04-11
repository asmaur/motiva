$(document).ready(function(){

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

  if($('#contact-form').length){
    $('#contact-form').validator().on('submit', function (e) {
         
         var $this = $(this),
         $target = $(".form-response");
       if (e.isDefaultPrevented()) {
          $target.html("<div class='alert alert-danger'><p>Please select all required field.</p></div>");
       } else {
        var name = $("#form-name").val();
        var email = $("#form-email").val();
        var phone = $("#form-phone").val();
        var message = $("#form-message").val();
        var assunto = $("#form-subject").val();
        e.preventDefault();
        values = {"name": name, "email":email, "phone":phone, "assunto":assunto ,"message":message}
        console.log(values);

        $.ajax({
              url: "/contato/",
              type: "POST",
              data: {
               "name": name, "email":email, "phone":phone, "assunto":assunto ,"message":message
                
              },

              cache: false,

              beforeSend: function(xhr){
                //$("#loader").show();               
                $target.html("<div class='alert alert-info'><p>Loading ...</p></div>");
         
                xhr.setRequestHeader("X-CSRFToken", csrftoken);           
              },              
           
              success: function(data){
                console.log(data);
                if (data['sended']) {
                  
                    $this[0].reset();
                 $target.html("<div class='alert alert-success'><p>"+data['message']+"</p></div>");
                 
                  $.snackbar({
                    content: data['message'], // text of the snackbar
                    style: "toast", // add a custom class to your snackbar
                    timeout: 5000, // time in milliseconds after the snackbar autohides, 0 is disabled
                    htmlAllowed: true, // allows HTML as content value
                    onClose: function(){ } // callback called when the snackbar gets closed.
                });

                 
                }else{
                    $target.html("<div class='alert alert-danger'><p>"+data['message']+"</p></div>");
                }
                
              },

              error: function(){

              },

        }); 
        
       }
    });
  }
  
});