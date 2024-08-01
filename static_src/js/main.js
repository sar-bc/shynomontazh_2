let time_all = new Array();
let time_busy = new Array();
let client = new Array();
let time_btn_press = "";
let knopka_btn = "";

$(document).ready(function () {
    console.log("main.js");
    //==================
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
                url: "/api/client/",
                data: form_data,
                dataType: 'json',
                success : function(response){
                    console.log('ok - ', response)
                    if(response.status === 201){
                        $('.success_save').text("Запись сохранена.").removeClass('d-none')
                        setTimeout(function () {
                            window.location.reload()
                            // windows.location.href = "/?date="+date
                        }, 3000);
                        // window.location.reload()
                    }else if (response.status === 400) {
                           $('.enter').removeClass('d-none')
                     $('.error_save').text(response.error).removeClass('d-none')
                    }else if (response.status === 401) {
                        $('.success_save').text(response.error).removeClass('d-none')
                        setTimeout(function () {
                            // window.location.reload()
                            console.log(date)
                            window.location.href = "/?date=" + date
                        }, 3000);
                 }
                },
                error: function (response) {
                    console.log('err - ', response)
                }
            })
        }//confirm
        

    })
    //=================
    $("#form_del").submit(function(e){
        e.preventDefault();
        let form_data = $(this).serialize();
        if (confirm("Удалить вашу запись?")) {
            console.log("Удаляем=")
            $.ajax({
                type: this.method,
                url: "/api/client/del/",
                data: form_data,
                dataType: 'json',
                success : function(response){
                    console.log('ok - ', response)
                if(response.status === 201){
                // window.location.reload()
                $('.response').text(response.response).removeClass('d-none')
                setTimeout(function () {
                    window.location.reload()
                }, 3000);
            }else if (response.status === 400) {
                $('.error').text(response.error).removeClass('d-none')
            }
                },
                error: function (response) {
                    console.log('err - ', response)
                }
            })

        }

    })
    //=================
    let calendar = document.getElementById("date");
    if (calendar) {
    //запрашиваем с сервера по дате время
        $.get("/api/client/", function (get_data){
            console.log(get_data);
            calendar.value = get_data.date;//устанавливаем текущую дату 
            calendar.min = get_data.date;//минимальная дата текущая
            calendar.max = get_data.date_max;//максимальная дата
            remove_table();
        //////////////////////////
        table_create(get_data.time_all, get_data.time_busy);
        //////////////////////////

        })//$get

    }//calendar
})//doc ready
//================================================
function remove_table(){
    let t = document.getElementById("table_time");
            if(t){
                let parent = document.getElementById("table");
                parent.removeChild(t);
            }
}
//==================================================
function del_time(id){
    console.log("Удаляем запись!" + id);
    $.ajax({
        type: "delete",
        url: "/api/client/",
        data: id,
        dataType: 'json',
        success: function (response){
            console.log('ok - ', response)
        },
        error: function (response) {
            console.log('err - ', response)
        }
    })
}
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
//==========================================================
let time_arr = new Array();
function handleDateChange(event) {
    const selectedDate = event.target.value;
    // console.log(`Выбранная дата и время: ${selectedDate}`);
    $.get("/api/client/" + `${selectedDate}`+"/", function (data) {
        // console.log(data);
        remove_table();
        //////////////////////////
        table_create(data.time_all, data.time_busy);
        //////////////////////////    
    });
}
//==========================================================
function table_create(all, busy){
    let count = 0;
    
    let u = Math.ceil(all.length/4)
    let table  = document.createElement('table');
            table.setAttribute("id", "table_time");
            
            for(let i = 0; i < u; i++){
                let tr = table.insertRow();

                for(let j = 0; j < 4; j++){
                    let td = tr.insertCell();

                    if (count < all.length) {
                        if (busy.indexOf(all[count]) > -1) {
        
                            td.innerHTML = "<input type='button' name='time' class='btn btn-secondary'  disabled value='" + all[count] + "'></input>";
                        }
                        else {
                            td.innerHTML = "<input id = 'btn" + count + "' onclick=click_btn('btn" + count + "','" + all[count] + "'); type='button' name='time' class='btn btn-dark time_btn' value='" + all[count] + "'></input>";
        
                        }
                        count++;
                    }

                }//for
            }//for

    // ищем div  в котором создадим таблицу
    let div = document.getElementById("table");
    div.appendChild(table);

}
//==========================================================
 window.addEventListener("DOMContentLoaded", function() {
   [].forEach.call( document.querySelectorAll("[type=tel]"), function(input) {
     var keyCode;
     function mask(event) {
       event.keyCode && (keyCode = event.keyCode);
       var pos = this.selectionStart;
       if (pos < 3) event.preventDefault();
       var matrix = "+7 (___) ___ ____",
           i = 0,
           def = matrix.replace(/\D/g, ""),
           val = this.value.replace(/\D/g, ""),
           new_value = matrix.replace(/[_\d]/g, function(a) {
               return i < val.length ? val.charAt(i++) : a
           });
       i = new_value.indexOf("_");
       if (i != -1) {
           i < 5 && (i = 3);
           new_value = new_value.slice(0, i)
       }
       var reg = matrix.substr(0, this.value.length).replace(/_+/g,
           function(a) {
               return "\\d{1," + a.length + "}"
           }).replace(/[+()]/g, "\\$&");
       reg = new RegExp("^" + reg + "$");
       if (!reg.test(this.value) || this.value.length < 5 || keyCode > 47 && keyCode < 58) {
         this.value = new_value;
       }
       if (event.type == "blur" && this.value.length < 5) {
         this.value = "";
       }
     }

     input.addEventListener("input", mask, false);
     input.addEventListener("focus", mask, false);
     input.addEventListener("blur", mask, false);
     input.addEventListener("keydown", mask, false);

   });

 });
//==========================================================