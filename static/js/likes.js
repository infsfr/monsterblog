$(function(){
    $('#like-button').click(function(){
        var likes = parseInt($('#likes-counter').html());
        var post_id = parseInt($(this).attr('postid'))
        likes += 1;
        $('#likes-counter').html(likes);
        $.ajax({
            url: '/add_like/'+post_id+'/',
        });

    });
});