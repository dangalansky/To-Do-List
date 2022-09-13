var array = [];

//line-through function + push to array
$("li").each(function(i) {
    $(this).click(function(){
        var text = $(this).text();
        if(!array.includes(text)) {
            $(this).addClass("linethrough");
            array.push(text);
        }
    });
});

//send array to flask
function removeItems() {
    $.post("/remove", {"array" : array});
}
