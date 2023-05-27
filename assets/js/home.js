// $(document).ready(function () {
//   $("#login").click(function () {
//     // $("").hide();
//   });
// });

$(document).ready(function () {

  $("#search").click(function () {
    $(this).css("background-color", "rgb(255,255,255)");
  });
});

// $(document).ready(function () {
//   $(".loginback").hide();
// });

$(document).ready(function () {

  $(".loginback").hide();
  $('.loginbtn').click(function () {
    if ($('.loginback').is(':hidden')) {
      $('.introductions').hide();
      $('.midline').hide();
      $('.midcontent').hide();
      $('.footer').hide();
      $('nav').hide();
      $('.slides').hide();
      $('.loginback').show();
    } else {

    }
  });
});

$(document).ready(function () {

  $(".closebtn").click(function () {
    $('.introductions').show();
    $('.midline').show();
    $('.midcontent').show();
    $('.footer').show();
    $('nav').show();
    $('.slides').show();
    $('.loginback').hide();
  });
});


function googleTranslateElementInit() {
  new google.translate.TranslateElement(
    { pageLanguage: 'en' },
    'google_element'
  );
}


$(document).ready(function () {
  $("#google_element").hide();

  $(".icongt").click(function () {

    if ($('#google_element').is(':hidden')) {
      $('#google_element').show();
    } else {

      $('#google_element').hide();
    }

  });

});


/******** slides ********/

$(document).ready(function () {
  $(".languagesslide").hide();

  $("#languagebtn").mouseover(function () {

    if ($('.languagesslide').is(':hidden')) {
      $(".languagesslide").slideDown("slow");
      $(".premiumsslide").hide();
      $(".exercisesslide").hide();
      $(".mycodeslide").hide();
      $(".languagesslide").show();

    }
  });


  $(".languagesslide").mouseover(function () {


    $(".premiumsslide").hide();
    $(".exercisesslide").hide();
    $(".mycodeslide").hide();
    $(".languagesslide").show();
  });

  // $(".languagesslide").mouseout(function () {

  //   $(".languagesslide").slideUp("slow");
  //   $(".premiumsslide").hide();
  //   $(".exercisesslide").hide();
  //   $(".mycodeslide").hide();
  // });



});





// $(document).ready(function () {

//   $("#languagebtn").mouseout(function () {
//     $(".languagesslide").slideUp("slow");
//   });
// });





$(document).ready(function () {
  $(".exercisesslide").hide();

  $("#exercisesbtn").mouseover(function () {

    if ($('.exercisesslide').is(':hidden')) {
      $(".exercisesslide").slideDown("slow");
      $(".languagesslide").hide();
      $(".premiumsslide").hide();
      $(".mycodeslide").hide();

    }
  });

});

$(document).ready(function () {
  $(".premiumsslide").hide();

  $("#questionsbtn").mouseover(function () {

    if ($('.premiumsslide').is(':hidden')) {
      $(".premiumsslide").slideDown("slow");
      $(".languagesslide").hide();
      $(".exercisesslide").hide();
      $(".mycodeslide").hide();

    }
  });

});



$(document).ready(function () {
  $(".mycodeslide").hide();

  $("#mycodebtn").mouseover(function () {

    if ($('.mycodeslide').is(':hidden')) {
      $(".mycodeslide").slideDown("slow");
      $(".languagesslide").hide();
      $(".premiumsslide").hide();
      $(".exercisesslide").hide();
    }
  });

});

$(document).ready(function () {
  $(".upload").hide();

  $(".img").mouseover(function () {

      if ($('.upload').is(':hidden')) {

          $(".upload").show();

      }

  });

});

$(document).ready(function () {
 
  $(".upload").mouseout(function () {

      if ($('.upload').is(':visible')) {

          $(".upload").hide();

      }

  });

});



$(document).ready(function () {
  var prevScrollpos = window.pageYOffset;
  window.onscroll = function () {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
      document.getElementById("lslide").style.top = "0";
    } else {
      $(".mycodeslide").slideUp("slow");
      $(".premiumsslide").slideUp("slow");
      $(".exercisesslide").slideUp("slow");
      $(".languagesslide").slideUp("slow");
    }
    prevScrollpos = currentScrollPos;
  }
});

