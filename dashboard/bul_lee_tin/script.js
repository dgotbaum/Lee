$(document).ready( function (){
    $("#forumPost").click(function () {
        var employee = $("input[id=NAME]").val();
        var msg = $("textarea[id=MESSAGE]").val();
        
       $("ul").append('<li class="media"><a class="pull-left" id="remove"><span class="glyphicon glyphicon-remove"></span></a><div class="media-body"><h4 class="media-heading" style="color: #98002E">' + employee + '</h4>' + msg +  '</div></li>');
    });
    $(document).on("click", ".glyphicon", function() { $(this).parent().parent().fadeOut(300);});
});