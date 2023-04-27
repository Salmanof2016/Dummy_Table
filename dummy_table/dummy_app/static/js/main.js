// fetchData();
//
// async function fetchData() {
//     let response = await fetch('/ajax/data/', {
//         headers: {
//             'Accept': 'application/json',
//             'X-Requested-With': 'XMLHttpRequest'
//         },
//     });
//     let data = await response.json();
//     console.log(data)
//     data.forEach(user => {
//         document.querySelector('tbody').insertAdjacentHTML("beforeend", `<tr><td>${user.id}</td><td>${user.book_name}</td><td>${user.writer}</td></tr>`);
//     })
// }
//
//
//
// let form = document.getElementById('form');
//
// form.addEventListener('submit', event => {
//     event.preventDefault();
//     let formData = new FormData(form);
//     let data = Object.fromEntries(formData);
//     console.log(data)
//
//     fetch('ajax/data/post/' , {
//         Method : 'POST',
//         headers :{
//             'Content-Type': 'application/json'
//         },
//         data: JSON.stringify(data),
//     })
// })

// $(document).ready(function () {
//
//     // get Method
//     let csrf = $("input[name=csrfmiddlewaretoken]").val();
//
//     $('.btn').click(function () {
//         $.ajax({
//             url: '',
//             type: 'get',
//             data: {
//                 button_text: $(this).text()
//             },
//             success: function (response) {
//                 $(".btn").text(response.seconds)
//                 $("#tr_add").append('<th>'+ response.seconds + '</th>')
//             }
//         });
//     });
//
//     // post method
//     $('#tr_add').on('click' , 'th' , function (){
//         $.ajax({
//             url: '',
//             type: 'post',
//             data: {
//                 text: $(this).text(),
//                 csrfmiddlewaretoken: csrf
//             },
//             success: function(response){
//                 $('.down').append('<li>' + response.data + '</li>')
//             }
//         })
//     })
//
// });

$(document).ready(function () {
    setInterval(function () {
        $.ajax({
            type : 'GET',
            url : '/getFormData/',
            success : function (response){
                console.log(response)
            },
            error : function (response){
              alert('Error getting data')
            }
        })
    },1000)
})

