<!DOCTYPE html>
<html lang="en">

<?php include("includes/head.php") ?>

<body>
    <!--navbar-->
    <?php include("includes/nav.php") ?>
    <!--**navbar**-->
    <div class="hero-image-short">
        <div class="hero-text-left">
            <h3><b>"Tüm ilanlar" </b> kategorisindesiniz</h3>
        </div>
        <div class="hero-text-right">
            <!--Eğer giriş/kayıt yapılmadıysa bu buton gösterilir-->
            <a class="btn btn-block" href="uyelik1.php" style="background-color:#004aad"><b
                    style="color:white;">Kazanmaya
                    başla</b></a>
            <!--****-->
        </div>
    </div>
    <!--content-->
    <div class="container-lg">

        <div class="row">
            <!--filtre-->
            <div class="col-lg-4 col-md-5 col-12">
                <div class="vertical-card-div filtre" style="position: -webkit-sticky; position: sticky; top: 10%;">
                    <?php include("includes/ilan-filtre.php"); ?>
                </div>
            </div>
            <!--**filtre**-->


            <div class="col-lg-8 col-md-7 col-12">
                <!--sıralama-->
                <div class="row">
                    <div class="col">
                        <select class="form-select  form-select" id="kategori">
                            <option selected>Sırala</option>
                            <option value="1">En yüksek ücret</option>
                            <option value="2">En düşük ücret</option>
                            <option value="3">En çok teklif alan</option>
                            <option value="4">En az teklif alan</option>
                        </select>
                    </div>
                    <div class="col">
                        <div class="input-group mb-3">
                            <input type="text" class="form-control" placeholder="web geliştirici" aria-label="ara"
                                aria-describedby="button-addon2">
                            <button class="btn btn-outline-secondary" type="button" id="button-addon2">Ara</button>
                        </div>
                    </div>
                </div>
                <!--**sıralama**-->

                <!--ilanlar-->
                <div class="card">
                    <h6 class="card-header">Web sitemiz için optimizasyon
                    </h6>
                    <div class="card-body py-1">
                        <div class="row">
                            <div class="col-12 col-lg-2 text-center"><img src="images/dijital.png" class="kategori-img">
                            </div>
                            <div class="col-12 col-lg-10">
                                <p class="card-text">
                                    Web sitemizin içeriklerinin optimize edilerek Google reklamlarına çıkartılması
                                    için
                                    deneyimli dijital pazarlama uzmanı arıyoruz
                                </p>
                                <small class="card-text"><span class="detay">109 Teklif | Son 4 Gün | Deneyim: Farketmez
                                        | </span> <b class="price">1.200₺ - 1.400₺</b> | <img src="images/fav.png"
                                        alt="favori" style="max-width:20px;margin-bottom:5px;"
                                        onmouseover="this.src='images/fav-sari.png';"
                                        onmouseout="this.src='images/fav.png';">
                                </small>
                                <a href="ilan-detay.php" class="btn btn-sm apply-button btn-outline-primary">İncele</a>
                            </div>
                        </div>
                    </div>
                </div>
                <!--**ilanlar**-->
            </div>
        </div>
    </div>

    <!--offcanvas filtre-->
    <nav class="navbar navbar-light bg-light fixed-bottom mycanvas">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Detaylı arama</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasNavbar"
                aria-controls="offcanvasNavbar">
                <span><img src="images/filter.png" style="width:40px"></span>
            </button>
            <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvasNavbar"
                aria-labelledby="offcanvasNavbarLabel">
                <div class="offcanvas-header">
                    <h5 class="offcanvas-title" id="offcanvasNavbarLabel">Offcanvas</h5>
                    <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas"
                        aria-label="Close"></button>
                </div>
                <div class="offcanvas-body">
                    <?php include("includes/ilan-filtre.php"); ?>
                </div>
            </div>
        </div>
    </nav>
    <!--**offcanvas filtre**-->

    <!--footer-->
    <?php include("includes/footer.php");
    include("includes/scripts.php"); ?>
    <!--**footer**-->
</body>

</html>