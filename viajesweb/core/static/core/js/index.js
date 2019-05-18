window.onscroll = function() {myFunction()};

function myFunction() {
  if (document.body.scrollTop >150 || document.documentElement.scrollTop > 150) {
    document.getElementById("myImg").className = "derecha rounded img-fluid col-12 float-left col-lg-6";
    document.getElementById("myText").className = "izquierda col-12 float-right h6 col-lg-6 mt-3";
  }
}
