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


$(document).ready(function () {
  $(".languagesslide").hide();
  $(".closebtn").hide();

  $("#languagebtn").mouseover(function () {

    if ($('.languagesslide').is(':hidden')) {
      $(".languagesslide").slideDown("slow");
      $(".premiumsslide").hide();
      $(".exercisesslide").hide();
      $(".mycodeslide").hide();

    }
  });

});

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
  $(".content").scroll(function () {

    $(".mycodeslide").slideUp("slow");
    $(".languagesslide").slideUp("slow");
    $(".premiumsslide").slideUp("slow");
    $(".exercisesslide").slideUp("slow");

  });
  $(".content1").scroll(function () {

    $(".mycodeslide").slideUp("slow");
    $(".languagesslide").slideUp("slow");
    $(".premiumsslide").slideUp("slow");
    $(".exercisesslide").slideUp("slow");

  });
});



/*******************************/


$(document).ready(function () {



  $(".content").show();


  $(".content1").show();

  $(".p1").click(function () {
    $(".content").show();
    $(".content1").hide();
  });

  $(".p2").click(function () {
    $(".content").hide();
    $(".content1").show();
  });
});

