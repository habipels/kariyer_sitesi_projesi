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
            <div class="col-lg-3 col-md-5 col-12">
                <div class="vertical-card-div filtre" style="top: 10%;">
                    <?php include("includes/uzman-filtre.php"); ?>
                </div>
            </div>
            <!--**filtre**-->


            <div class="col-lg-9 col-md-7 col-12">
                <!--sıralama-->
                <div class="row">
                    <div class="col">
                        <select class="form-select  form-select" id="kategori">
                            <option selected>Sırala</option>
                            <option value="1">En çok deneyimli</option>
                            <option value="2">En az deneyimli</option>
                            <option value="3">En yüksek puan</option>
                            <option value="4">Akıllı sıralama</option>
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

                <!--uzmanlar-->
                <div class="row justify-content-center">
                    <div class="col-lg-3 col-6 ">
                        <div class="card uzman-card">
                            <img src="images/pp.jpg" class="card-img-top" alt="...">
                            <div class="card-body">
                                <h6 class="card-title">Siber Güvenlik Uzmanı</h6>
                                <h6 class="card-subtitle text-muted" style="font-size:13px;">Habip E.</h6>
                                <div class="kisisel-bilgiler">
                                    <div style="display:inline;"><img src="images/ikonlar/1.png"><small>Antalya</small>
                                    </div>
                                    <div style="display:inline;margin-left:5px;"><img
                                            src="images/ikonlar/7.png"><small>5
                                            yıl
                                        </small>
                                    </div>
                                </div>
                                <p class="card-text uzman-text">Web sitenizin
                                    siber
                                    saldırılara karşı güvenliğini sağlayabilirim
                                </p>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-6 ">
                        <div class="card uzman-card">
                            <img src="images/pp.jpg" class="card-img-top" alt="...">
                            <div class="card-body">
                                <h6 class="card-title">Siber Güvenlik Uzmanı</h6>
                                <h6 class="card-subtitle text-muted" style="font-size:13px;">Habip E.</h6>
                                <div class="kisisel-bilgiler">
                                    <div style="display:inline;"><img src="images/ikonlar/1.png"><small>Antalya</small>
                                    </div>
                                    <div style="display:inline;margin-left:5px;"><img
                                            src="images/ikonlar/7.png"><small>5
                                            yıl
                                        </small>
                                    </div>
                                </div>
                                <p class="card-text uzman-text">Web sitenizin
                                    siber
                                    saldırılara karşı güvenliğini sağlayabilirim
                                </p>
                            </div>
                        </div>
                    </div>

                    <div class="col-lg-3 col-6 ">
                        <div class="card uzman-card">
                            <img src="images/duhan.jpeg" class="card-img-top" alt="...">
                            <div class="card-body">
                                <h6 class="card-title">Front End Web Geliştirici</h6>
                                <h6 class="card-subtitle text-muted" style="font-size:13px;">Duhan G.</h6>
                                <div class="kisisel-bilgiler">
                                    <div style="display:inline;"><img src="images/ikonlar/1.png"><small>İstanbul</small>
                                    </div>
                                    <div style="display:inline;margin-left:5px;"><img
                                            src="images/ikonlar/7.png"><small>10
                                            yıl
                                        </small>
                                    </div>
                                </div>
                                <p class="card-text uzman-text">Web
                                    projelerinizin front end
                                    kodlamasını ve arayüz tasarımını yapabilirim
                                </p>
                            </div>
                        </div>
                    </div>
                    <div class="col-lg-3 col-6 ">
                        <div class="card uzman-card">
                            <img src="images/pp.jpg" class="card-img-top" alt="...">
                            <div class="card-body">
                                <h6 class="card-title">Front End Geliştirici</h6>
                                <h6 class="card-subtitle text-muted" style="font-size:13px;">Habip E.</h6>
                                <div class="kisisel-bilgiler">
                                    <div style="display:inline;"><img src="images/ikonlar/1.png"><small>İstanbul</small>
                                    </div>
                                    <div style="display:inline;margin-left:5px;"><img
                                            src="images/ikonlar/7.png"><small>2
                                            yıl
                                        </small>
                                    </div>
                                </div>
                                <p class="card-text uzman-text">Web, mobil ve
                                    grafik
                                    tasarım projelerinizde görev alabilirim
                                </p>
                            </div>
                        </div>
                    </div>

                </div>


                <!--**uzmanlar**-->
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