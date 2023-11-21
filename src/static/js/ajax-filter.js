
function ajaxSend(url, params) {
    fetch(`${url}?${params}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
    .then(responce => responce.json())
    .then(json => render(json))
    .catch(error => console.error(error))
}


const form = document.querySelector('form[name=filter-json]')

form.addEventListener('submit', function(e) {
    e.preventDefault()
    let url = this.action
    let params = new URLSearchParams(new FormData(this)).toString()
    ajaxSend(url, params)
})


function render(data) {
    let template = Hogan.compile(HTML)
    let output = template.render(data)

    const div = document.querySelector('.product-list-filter')
    div.innerHTML = output
}

let HTML = '\
{{#product_list}}\
<div>\
    <div class="uk-card uk-card-default">\
        <div class="uk-card-header">\
            <h3 class="uk-margin-remove"><a href="/product/{{ slug }}">{{ title }}</a></h3>\
        </div>\
        <div class="uk-card-body">\
            <div class="uk-h3"><b>{{price}}</b> руб.</div>\
        </div>\
    </div>\
</div>\
{{/product_list}}\
'