$('#toggle_btn').change(function () {
    $('#toggle_btn').attr('disabled', true);

    var token = $('input[name="csrfmiddlewaretoken"]', $('#toggle_light_form')).val();

    $.ajax({
        type: "POST",
        url: "/toggle_light/",
        data: { light_id: $('#light_id').val(), checked: $('#toggle_btn').prop('checked'), csrfmiddlewaretoken: token },
        success: function (result) {
            $('#toggle_btn').removeAttr('disabled');
            $('#request_ok').show();
            $('#request_failed').hide();
        },
        error: function (errMsg) {
            $('#request_failed').show();
            $('#request_ok').hide();
        }
    });
});