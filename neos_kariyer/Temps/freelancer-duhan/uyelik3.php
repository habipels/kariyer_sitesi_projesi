<!DOCTYPE html>
<html lang="en">

<?php include("includes/head.php") ?>

<body>
    <!--navbar-->
    <?php include("includes/nav.php") ?>
    <!--**navbar**-->
    <!--hero image-->
    <div class="hero-image">

        <div class="hero-text-avatar" style="top:0;left:45%;">
            <img src="images/ilan-avatar.png" alt="profil resmi" style="width:200px;">
        </div>

        <div class="hero-text-form">
            <form>
                <div class="form-group">
                    <label for="name">Şehir</label>
                    <select class="form-select" aria-label="Default select example">
                        <option selected>Lütfen seçiniz</option>
                        <option value="1">İstanbul</option>
                        <option value="2">Ankara</option>
                        <option value="3">İzmir</option>
                    </select>
                </div>
                <br>
                <div class="form-group">
                    <label for="email">Uzmanlık alanınız</label>
                    <select class="form-select" aria-label="Default select example">
                        <option selected>Lütfen seçiniz</option>
                        <option value="1">Grafik Tasarım</option>
                        <option value="2">Web Geliştirme</option>
                        <option value="3">Three</option>
                    </select>
                </div>
                <br>
                <label for="">Alanınızda kaç yıl deneyimlisiniz?</label>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="r" id="r1">
                    <label class="form-check-label" for="r1">
                        0 - 2 sene
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="r" id="r2" checked>
                    <label class="form-check-label" for="r2">
                        3 - 5 sene
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="r" id="r3" checked>
                    <label class="form-check-label" for="r3">
                        5 seneden fazla
                    </label>
                </div>

                <br>
                <label for="">Alacağınız projelere haftada kaç saat zaman ayırabilirsiniz?</label>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="t" id="t1">
                    <label class="form-check-label" for="t1">
                        En fazla 8 saat
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="t" id="t2" checked>
                    <label class="form-check-label" for="t2">
                        En fazla 18 saat
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="t" id="t3" checked>
                    <label class="form-check-label" for="t3">
                        En fazla 30 saat
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="radio" name="t" id="t4" checked>
                    <label class="form-check-label" for="t4">
                        40 saat ve fazlası
                    </label>
                </div>
                <br>
                <a href="profil.php" class="btn btn-primary">Kaydet</a>
            </form>
        </div>

    </div>
    <!--**hero image-->

    <!--footer-->
    <?php include("includes/footer.php");
    include("includes/scripts.php"); ?>
    <!--**footer**-->
</body>

</html>