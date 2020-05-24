$(function () {
   /* //显示/隐藏密码
    $('#eye').click(function () {
        var eye = $("#eye")[0];
        var pwd = $("#password")[0];
        if (pwd.type == "password") {
            pwd.type = "textarea.html";
            eye.className = 'fa fa-eye-slash'
        } else {
            pwd.type = "password";
            eye.className = 'fa fa-eye'
        }
    });
    $('#eye1').click(function () {
        var eye = $("#eye1")[0];
        var pwd = $("#password1")[0];
        if (pwd.type == "password") {
            pwd.type = "textarea.html";
            eye.className = 'fa fa-eye-slash'
        } else {
            pwd.type = "password";
            eye.className = 'fa fa-eye'
        }
    });
    $('#eye2').click(function () {
        var eye = $("#eye2")[0];
        var pwd = $("#password2")[0];
        if (pwd.type == "password") {
            pwd.type = "textarea.html";
            eye.className = 'fa fa-eye-slash'
        } else {
            pwd.type = "password";
            eye.className = 'fa fa-eye'
        }
    });*/

    // 校验用户名是否被注册
    $('#username').blur(function () {
        alert('xxx');
        var name = $('#username').val();
        var error = $('#username_error');
        var csrf = $('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            url: '/buyer/register_check_ajax/',
            type: 'get',
            data: {'username': name, 'csrfmiddlewaretoken': csrf,},
            success: function (res) {
                if (res.status == 'true') {
                    error.text('该账号已被注册');
                } else {
                    error.text('')
                }
            },
        })
    });

    //注册验证
    $("#sub_btn").click(function () {
        // 两次密码校验
        var pwd1 = $("#password1").val();
        var pwd2 = $("#password2").val();
        if (pwd1 != pwd2) {
            $("#err_msg2").text("两次密码不一致");
            return false;
        }
    });
});

