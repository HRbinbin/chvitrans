function subtran() {
    var ch = document.getElementById('ch').value;
    $.ajax({
        type: 'post',
        dataType: "json",
        url: "trans/",
        data: {
            ch: ch,
        },
        success: function (data) {
            var vi = document.getElementById('vi');
            vi.value = data['vi'];
        },
        error: function (jqXHR) {
            console.log("Error: " + jqXHR.status);
        }
    });
}