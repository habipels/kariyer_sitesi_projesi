<!-- Option 1: Bootstrap Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-/bQdsTh/da6pkI1MST/rWKFNjaCP5gBSY4sEBT38Q/9RBh9AH40zEOg7Hlq2THRZ" crossorigin="anonymous">
</script>
<script>
if ($(window).width() < 960) {
    $(".mainnav").removeClass("fixed-top")
}
$("#uyeOpen").click(function() {
    $(".hero-image-short").slideUp(function() {
        $("#full-width").slideDown()
    })

})
//profil-duzenle
$("#profileImage").click(function(e) {
    $("#imageUpload").click();
});
$("#yetenekEkle").click(function(e) {
    yetenekInputu = $(".yeniYetenek").html()
    $('#yetenekEkle').before(yetenekInputu);

});
</script>