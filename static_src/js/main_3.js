let time_all = new Array();
let time_busy = new Array();
let client = new Array();
let time_btn_press = "";
let knopka_btn = "";

$(document).ready(function () {
    console.log("main.js");
    $("#form").submit(function(e){
        e.preventDefault();
        let form = document.getElementById('form');
        // let avto = form.elements['avto'].value;
        let date = form.elements['date'].value;
        let form_data = $(this).serialize();
        form_data = form_data + "&time=" + time_btn_press;

        console.log(form_data);
        

        if (confirm('Подтвердите вашу запись\n' + time_btn_press + ' ' + date)) {
            $.ajax({
                type: this.method,
                url: this.action,
                data: form_data,
                dataType: 'json',
                success : function(response){
                    console.log('ok - ', response)
                    if(response.status === 201){
                        $('.success_save').text("Запись сохранена.").removeClass('d-none')
                        setTimeout(function () {
                            window.location.reload()
                        }, 3000);
                        // window.location.reload()
                    }else if (response.status === 400) {
                           $('.enter').removeClass('d-none')
                     $('.error_save').text(response.error).removeClass('d-none')
                    }
                },
                error: function (response) {
                    console.log('err - ', response)
                }
            })
        }//confirm
        

    })

    let calendar = document.getElementById("date");
    if (calendar) {

    }    
});//$(document).ready
//==================================================
function click_btn(knopka, time) {
    if (knopka_btn.length > 3) {
        //console.log("была до этого кнопка " + knopka_btn);
        let btn_prev = document.getElementById(knopka_btn);
        btn_prev.style.color = "#fff";
    }
    knopka_btn = knopka;
    //console.log("press btn " + knopka);
    let btn = document.getElementById(knopka);
    btn.style.color = "green";
    time_btn_press = time;
    //console.log(time_btn_press);
}
//=================================================
function handleDateChange(event) {
    const selectedDate = event.target.value;
    console.log(`Выбранная дата и время: ${selectedDate}`);
    window.location.href = "/?date=" + selectedDate;

    
}
//=================================================