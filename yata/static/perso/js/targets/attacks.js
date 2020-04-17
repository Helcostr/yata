// toggle target from attack list button
$(document).on('click', '.attack-list-target', function(e){
    e.preventDefault();
    var targetId = $(this).closest("tr").attr("data-tId");
    var attackId = $(this).closest("tr").attr("data-aId");
    var reload = $(".catch-buttons-attack-"+targetId);
    reload.load( "/target/attack/", {
        targetId: targetId,
        attackId: attackId,
        type: "toggle",
        csrfmiddlewaretoken: getCookie("csrftoken")
    });
    reload.html('<i class="fas fa-spinner fa-pulse"></i>');
});

// toggle revive from revives list button
$(document).on('click', '.attack-list-paid', function(e){
    e.preventDefault();
    var attackId = $(this).closest("tr").attr("data-aId");
    $(this).closest("td").load( "/target/attack/", {
        attackId: attackId,
        type: "paid",
        csrfmiddlewaretoken: getCookie("csrftoken")
    }).html('<i class="fas fa-spinner fa-pulse"></i>');
});

// show losses
$(document).on('click', '#targets-attacks-losses', function(e){
    e.preventDefault();
    $( "#attack-losses" ).load( "/target/losses/", {
        csrfmiddlewaretoken: getCookie("csrftoken")
    })
});
// show losses
$(document).on('click', '.targets-attacks-losses-payall', function(e){
    e.preventDefault();
    console.log("coucou", $(this).attr("data-val"));
    $( "#attack-losses" ).load( "/target/losses/", {
        payall: $(this).attr("data-val"),
        csrfmiddlewaretoken: getCookie("csrftoken")
    })
});
$(document).on('click', '.close', function(e){
    e.preventDefault();
    $(this).parent("div.container").css("display", "none");
});
