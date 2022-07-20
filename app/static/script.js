function formSubmit(onclick, form_id, location, display) {

    $('.' + onclick).click(function() {
    var form = document.querySelector("#" + form_id);

    if (!form.checkValidity()) {
        var tmpSubmit = document.createElement('button');
        form.appendChild(tmpSubmit);
        tmpSubmit.click();
        form.removeChild(tmpSubmit);
    } else {
        $.ajax({
            url: "/" + location,
            type: "POST",
            data: $("#" + form_id).serialize(),
            success: function(response) {
                    $('#' + display).html(response);
            }
        });
    }
    });
};
