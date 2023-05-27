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

/*************************/



$(document).ready(function () {

  $(".menu").mouseover(function () {
    $(".mycodeslide").slideUp("slow");
    $(".languagesslide").slideUp("slow");
    $(".premiumsslide").slideUp("slow");
    $(".exercisesslide").slideUp("slow");
  });

  $(".container").mouseover(function () {
    $(".mycodeslide").slideUp("slow");
    $(".languagesslide").slideUp("slow");
    $(".premiumsslide").slideUp("slow");
    $(".exercisesslide").slideUp("slow");
  });


});



$(document).ready(function () {
  $(".submenu1").hide();
  $(".submenu2").hide();
  $(".submenu2").hide();
  $(".submenu3").hide();
  $(".submenu4").hide();
  $(".submenu5").hide();
  $(".submenu6").hide();
  $(".submenu7").hide();
  $(".submenu8").hide();
  $(".submenu9").hide();
  $(".submenu10").hide();
  $(".submenu11").hide();
  $(".submenu12").hide();
  $(".submenu13").hide();
  $(".submenu14").hide();
  $(".submenu15").hide();

  $(".dropdownbtn1").click(function () {
    $(".submenu1").slideDown("slow");
    $(".submenu2").slideUp("slow");
    $(".submenu3").slideUp("slow");
    $(".submenu4").slideUp("slow");
    $(".submenu5").slideUp("slow");
    $(".submenu6").slideUp("slow");
    $(".submenu7").slideUp("slow");
    $(".submenu8").slideUp("slow");
    $(".submenu9").slideUp("slow");
    $(".submenu10").slideUp("slow");
    $(".submenu11").slideUp("slow");
    $(".submenu12").slideUp("slow");
    $(".submenu13").slideUp("slow");
    $(".submenu14").slideUp("slow");
    $(".submenu15").slideUp("slow");


  });

  $(".dropdownbtn2").click(function () {
    $(".submenu2").slideDown("slow");
    $(".submenu1").slideUp("slow");
    $(".submenu3").slideUp("slow");
    $(".submenu4").slideUp("slow");
    $(".submenu5").slideUp("slow");
    $(".submenu6").slideUp("slow");
    $(".submenu7").slideUp("slow");
    $(".submenu8").slideUp("slow");
    $(".submenu9").slideUp("slow");
    $(".submenu10").slideUp("slow");
    $(".submenu12").slideUp("slow");
    $(".submenu11").slideUp("slow");
    $(".submenu12").slideUp("slow");
    $(".submenu13").slideUp("slow");
    $(".submenu14").slideUp("slow");
    $(".submenu15").slideUp("slow");
  });

  $(".dropdownbtn3").click(function () {
    $(".submenu3").slideDown("slow");
    $(".submenu2").slideUp("slow");
    $(".submenu1").slideUp("slow");
    $(".submenu4").slideUp("slow");
    $(".submenu5").slideUp("slow");
    $(".submenu6").slideUp("slow");
    $(".submenu7").slideUp("slow");
    $(".submenu8").slideUp("slow");
    $(".submenu9").slideUp("slow");
    $(".submenu10").slideUp("slow");
    $(".submenu11").slideUp("slow");
    $(".submenu12").slideUp("slow");
    $(".submenu13").slideUp("slow");
    $(".submenu14").slideUp("slow");
    $(".submenu15").slideUp("slow");
  });

  $(".dropdownbtn4").click(function () {
    $(".submenu4").slideDown("slow");
    $(".submenu2").slideUp("slow");
    $(".submenu3").slideUp("slow");
    $(".submenu1").slideUp("slow");
    $(".submenu5").slideUp("slow");
    $(".submenu6").slideUp("slow");
    $(".submenu7").slideUp("slow");
    $(".submenu8").slideUp("slow");
    $(".submenu9").slideUp("slow");
    $(".submenu10").slideUp("slow");
    $(".submenu12").slideUp("slow");
    $(".submenu11").slideUp("slow");
    $(".submenu13").slideUp("slow");
    $(".submenu14").slideUp("slow");
    $(".submenu15").slideUp("slow");
  });

  $(".dropdownbtn5").click(function () {
    $(".submenu5").slideDown("slow");
    $(".submenu2").slideUp("slow");
    $(".submenu3").slideUp("slow");
    $(".submenu4").slideUp("slow");
    $(".submenu1").slideUp("slow");
    $(".submenu6").slideUp("slow");
    $(".submenu7").slideUp("slow");
    $(".submenu8").slideUp("slow");
    $(".submenu9").slideUp("slow");
    $(".submenu10").slideUp("slow");
    $(".submenu12").slideUp("slow");
    $(".submenu11").slideUp("slow");
    $(".submenu13").slideUp("slow");
    $(".submenu14").slideUp("slow");
    $(".submenu15").slideUp("slow");
  });

  $(".dropdownbtn6").click(function () {
    $(".submenu6").slideDown("slow");
    $(".submenu2").slideUp("slow");
    $(".submenu3").slideUp("slow");
    $(".submenu4").slideUp("slow");
    $(".submenu5").slideUp("slow");
    $(".submenu1").slideUp("slow");
    $(".submenu7").slideUp("slow");
    $(".submenu8").slideUp("slow");
    $(".submenu9").slideUp("slow");
    $(".submenu10").slideUp("slow");
    $(".submenu12").slideUp("slow");
    $(".submenu11").slideUp("slow");
    $(".submenu13").slideUp("slow");
    $(".submenu14").slideUp("slow");
    $(".submenu15").slideUp("slow");
  });

  $(".dropdownbtn7").click(function () {
    $(".submenu7").slideDown("slow");
    $(".submenu2").slideUp("slow");
    $(".submenu3").slideUp("slow");
    $(".submenu4").slideUp("slow");
    $(".submenu5").slideUp("slow");
    $(".submenu6").slideUp("slow");
    $(".submenu1").slideUp("slow");
    $(".submenu8").slideUp("slow");
    $(".submenu9").slideUp("slow");
    $(".submenu10").slideUp("slow");
    $(".submenu12").slideUp("slow");
    $(".submenu11").slideUp("slow");
    $(".submenu13").slideUp("slow");
    $(".submenu14").slideUp("slow");
    $(".submenu15").slideUp("slow");
  });

  $(".dropdownbtn8").click(function () {
    $(".submenu8").slideDown("slow");
    $(".submenu2").slideUp("slow");
    $(".submenu3").slideUp("slow");
    $(".submenu4").slideUp("slow");
    $(".submenu5").slideUp("slow");
    $(".submenu6").slideUp("slow");
    $(".submenu7").slideUp("slow");
    $(".submenu1").slideUp("slow");
    $(".submenu9").slideUp("slow");
    $(".submenu10").slideUp("slow");
    $(".submenu12").slideUp("slow");
    $(".submenu11").slideUp("slow");
    $(".submenu13").slideUp("slow");
    $(".submenu14").slideUp("slow");
    $(".submenu15").slideUp("slow");
  });

  $(".dropdownbtn9").click(function () {
    $(".submenu9").slideDown("slow");
    $(".submenu2").slideUp("slow");
    $(".submenu3").slideUp("slow");
    $(".submenu4").slideUp("slow");
    $(".submenu5").slideUp("slow");
    $(".submenu6").slideUp("slow");
    $(".submenu7").slideUp("slow");
    $(".submenu8").slideUp("slow");
    $(".submenu1").slideUp("slow");
    $(".submenu10").slideUp("slow");
    $(".submenu12").slideUp("slow");
    $(".submenu11").slideUp("slow");
    $(".submenu13").slideUp("slow");
    $(".submenu14").slideUp("slow");
    $(".submenu15").slideUp("slow");
  });

  $(".dropdownbtn10").click(function () {
    $(".submenu10").slideDown("slow");
    $(".submenu2").slideUp("slow");
    $(".submenu3").slideUp("slow");
    $(".submenu4").slideUp("slow");
    $(".submenu5").slideUp("slow");
    $(".submenu6").slideUp("slow");
    $(".submenu7").slideUp("slow");
    $(".submenu8").slideUp("slow");
    $(".submenu9").slideUp("slow");
    $(".submenu1").slideUp("slow");
    $(".submenu12").slideUp("slow");
    $(".submenu11").slideUp("slow");
    $(".submenu13").slideUp("slow");
    $(".submenu14").slideUp("slow");
    $(".submenu15").slideUp("slow");
  });

  $(".dropdownbtn11").click(function () {
    $(".submenu11").slideDown("slow");
    $(".submenu2").slideUp("slow");
    $(".submenu3").slideUp("slow");
    $(".submenu4").slideUp("slow");
    $(".submenu5").slideUp("slow");
    $(".submenu6").slideUp("slow");
    $(".submenu7").slideUp("slow");
    $(".submenu8").slideUp("slow");
    $(".submenu9").slideUp("slow");
    $(".submenu10").slideUp("slow");
    $(".submenu1").slideUp("slow");
    $(".submenu12").slideUp("slow");
    $(".submenu13").slideUp("slow");
    $(".submenu14").slideUp("slow");
    $(".submenu15").slideUp("slow");
  });

  $(".dropdownbtn12").click(function () {
    $(".submenu12").slideDown("slow");
    $(".submenu2").slideUp("slow");
    $(".submenu3").slideUp("slow");
    $(".submenu4").slideUp("slow");
    $(".submenu5").slideUp("slow");
    $(".submenu6").slideUp("slow");
    $(".submenu7").slideUp("slow");
    $(".submenu8").slideUp("slow");
    $(".submenu9").slideUp("slow");
    $(".submenu10").slideUp("slow");
    $(".submenu11").slideUp("slow");
    $(".submenu1").slideUp("slow");
    $(".submenu13").slideUp("slow");
    $(".submenu14").slideUp("slow");
    $(".submenu15").slideUp("slow");
  });

  $(".dropdownbtn13").click(function () {
    $(".submenu13").slideDown("slow");
    $(".submenu2").slideUp("slow");
    $(".submenu3").slideUp("slow");
    $(".submenu4").slideUp("slow");
    $(".submenu5").slideUp("slow");
    $(".submenu6").slideUp("slow");
    $(".submenu7").slideUp("slow");
    $(".submenu8").slideUp("slow");
    $(".submenu9").slideUp("slow");
    $(".submenu10").slideUp("slow");
    $(".submenu11").slideUp("slow");
    $(".submenu12").slideUp("slow");
    $(".submenu1").slideUp("slow");
    $(".submenu14").slideUp("slow");
    $(".submenu15").slideUp("slow");
  });

  $(".dropdownbtn14").click(function () {
    $(".submenu14").slideDown("slow");
    $(".submenu2").slideUp("slow");
    $(".submenu3").slideUp("slow");
    $(".submenu4").slideUp("slow");
    $(".submenu5").slideUp("slow");
    $(".submenu6").slideUp("slow");
    $(".submenu7").slideUp("slow");
    $(".submenu8").slideUp("slow");
    $(".submenu9").slideUp("slow");
    $(".submenu10").slideUp("slow");
    $(".submenu11").slideUp("slow");
    $(".submenu12").slideUp("slow");
    $(".submenu13").slideUp("slow");
    $(".submenu1").slideUp("slow");
    $(".submenu15").slideUp("slow");
  });

  $(".dropdownbtn15").click(function () {
    $(".submenu15").slideDown("slow");
    $(".submenu2").slideUp("slow");
    $(".submenu3").slideUp("slow");
    $(".submenu4").slideUp("slow");
    $(".submenu5").slideUp("slow");
    $(".submenu6").slideUp("slow");
    $(".submenu7").slideUp("slow");
    $(".submenu8").slideUp("slow");
    $(".submenu9").slideUp("slow");
    $(".submenu10").slideUp("slow");
    $(".submenu11").slideUp("slow");
    $(".submenu12").slideUp("slow");
    $(".submenu13").slideUp("slow");
    $(".submenu14").slideUp("slow");
    $(".submenu1").slideUp("slow");
  });
});


