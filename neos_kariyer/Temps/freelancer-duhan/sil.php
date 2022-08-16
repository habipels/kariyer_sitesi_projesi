<!DOCTYPE html>
<html lang="en">

<head>
    <!-- Required meta tags -->
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <!--Jquery-->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.1/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-F3w7mX95PdgyTmZZMECAngseQB83DfGTowi0iMjiWaeVhAn4FJkqJByhZMI3AhiU" crossorigin="anonymous" />

    <link rel="stylesheet" type="text/css" href="style.css" />

    <title>Neos Kariyer</title>
</head>

<body>
    <!--navbar-->
    <?php include("includes/nav.php") ?>
    <!--**navbar**-->

    <!--hero image-->
    <div class="hero-image-short">
        <div class="hero-text-left">
            <h2>Kolayca başvur, hemen başla</h2>
        </div>
        <div class="hero-text-right">
            <form style="background-color:white;padding:20px 40px;color:black;width:400px">
                <div class="mb-3">
                    <label for="exampleInputEmail1" class="form-label">Email/Telefon</label>
                    <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                </div>
                <div class="mb-3">
                    <label for="exampleInputPassword1" class="form-label">Parola</label>
                    <input type="password" class="form-control" id="exampleInputPassword1">
                </div>
                <div class="mb-3">
                    <button type="submit" class="btn btn-outline-danger w-100"><img src="images/google.png"
                            style="width:20px">
                        Google
                        ile oturum
                        aç</button>
                </div>
                <div class="mb-3">
                    <button type="submit" class="btn btn-success w-100">Kaydol</button>
                </div>

            </form>
        </div>
    </div>
    <!--**hero image-->

    <!--content-->
    <div class="container" style="margin-top:40px">
        <div class="row">
            <!--sağ dikey kartlar-->

            <div class="col-md-4 col-12 vertical-card-div p-3" style="margin-top:55px">

                <label for="kategori" class="form-label">Kategori</label>
                <select class="form-select" id="kategori">
                    <option selected>Tümü</option>
                    <option value="1">Grafik tasarım uzmanı</option>
                    <option value="2">Yazılım uzmanı</option>
                    <option value="3">Kameraman</option>
                    <option value="3">Video editörü</option>
                    <option value="3">Metinsel içerik üretici</option>
                    <option value="3">Sosyal medya uzmanı</option>
                    <option value="3">Satış ve pazarlama uzmanı</option>
                    <option value="3">Dijital pazarlama uzmanı</option>
                    <option value="3">3D Tasarımcı</option>
                    <option value="3">Siber güvenlik uzmanı</option>
                    <option value="3">Video içerik üretici</option>
                    <option value="3">Video içerik üretici</option>
                    <option value="3">Fotoğrafçı</option>
                    <option value="3">Eğitmen</option>
                </select>

                <br>

                <label for="lokasyon" class="form-label">Lokasyon</label>
                <div class="input-group mb-3">
                    <input type="text" class="form-control" aria-describedby="button-addon2" value="Farketmez">
                </div>

                <br>

                <label>Deneyim süresi</label>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                    <label class="form-check-label" for="flexCheckDefault">
                        0-1 yıl
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                    <label class="form-check-label" for="flexCheckDefault">
                        1-3 yıl
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                    <label class="form-check-label" for="flexCheckDefault">
                        3-5 yıl
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                    <label class="form-check-label" for="flexCheckDefault">
                        5+ yıl
                    </label>
                </div>

                <br>

                <label>Çalışma beklentisi</label>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                    <label class="form-check-label" for="flexCheckDefault">
                        Tam zamanlı çalışma arayışında
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                    <label class="form-check-label" for="flexCheckDefault">
                        Yarı zamanlı çalışma arayışında
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                    <label class="form-check-label" for="flexCheckDefault">
                        Proje bazlı çalışma arayışında
                    </label>
                </div>

                <br>

                <label>Ekip</label>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                    <label class="form-check-label" for="flexCheckDefault">
                        Kendi ekibi var
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                    <label class="form-check-label" for="flexCheckDefault">
                        Bireysel çalışıyor
                    </label>
                </div>

                <br>

                <label>Haftalık çalışabileceği süre</label>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                    <label class="form-check-label" for="flexCheckDefault">
                        2-8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;saat
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                    <label class="form-check-label" for="flexCheckDefault">
                        8-16&nbsp;&nbsp;&nbsp;saat
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                    <label class="form-check-label" for="flexCheckDefault">
                        16-32 saat
                    </label>
                </div>
                <div class="form-check">
                    <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                    <label class="form-check-label" for="flexCheckDefault">
                        40+&nbsp;&nbsp;&nbsp;&nbsp;saat
                    </label>
                </div>

                <br>

                <div class="btn btn-primary w-100">Ara</div>
            </div>
            <!--**sağ dikey kartlar**-->
            <div class="col-1"></div>
            <!--sol yatay kartlar-->
            <div class="col-md-7 col-12">
                <h5>Tüm uzmanları görüntülüyorsunuz</h5>
                <br>
                <div class="row">
                    <div class="col-6">

                        <select class="form-select  form-select-lg" id="kategori">
                            <option selected>Sırala</option>
                            <option value="1">En yüksek ücret</option>
                            <option value="2">En düşük ücret</option>
                        </select>
                    </div>

                    <div class="col-6">
                        <div class="input-group mb-3">
                            <input type="text" class="form-control" placeholder="web geliştirici" aria-label="ara"
                                aria-describedby="button-addon2">
                            <button class="btn btn-outline-secondary btn-lg" type="button"
                                id="button-addon2">Ara</button>
                        </div>
                    </div>
                </div>


                <div class="card">
                    <h5 class="card-header">Front end web geliştirici</h5>
                    <div class="card-body">
                        <div class="row">
                            <div class="col-4 col-lg-2"><img src="images/ilan-avatar.png" style="width:100%"></div>
                            <div class="col-8 col-lg-10">
                                <p class="card-text">
                                    Projemizin tasarımını ve front end kodlamasını yapmak üzere
                                    takım arkadaşı arıyoruz
                                </p>
                                <small class="card-text">Bütçe: 300-600 TL | Kategori: Web Geliştirme | Proje
                                    Kapsamı:
                                    Geniş <br />
                                    Aranan Nitelikler: HTML, CSS, JS</small>
                                <a href="#" class="btn btn-sm btn-outline-success apply-button">Teklif al</a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card">
                    <h5 class="card-header">Front end web geliştirici</h5>
                    <div class="card-body">
                        <div class="row">
                            <div class="col-4 col-lg-2"><img src="images/ilan-avatar.png" style="width:100%"></div>
                            <div class="col-8 col-lg-10">
                                <p class="card-text">
                                    Projemizin tasarımını ve front end kodlamasını yapmak üzere
                                    takım arkadaşı arıyoruz
                                </p>
                                <small class="card-text">Bütçe: 300-600 TL | Kategori: Web Geliştirme | Proje
                                    Kapsamı:
                                    Geniş <br />
                                    Aranan Nitelikler: HTML, CSS, JS</small>
                                <a href="#" class="btn btn-sm btn-outline-success apply-button">Teklif al</a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card">
                    <h5 class="card-header">Front end web geliştirici</h5>
                    <div class="card-body">
                        <div class="row">
                            <div class="col-4 col-lg-2"><img src="images/ilan-avatar.png" style="width:100%"></div>
                            <div class="col-8 col-lg-10">
                                <p class="card-text">
                                    Projemizin tasarımını ve front end kodlamasını yapmak üzere
                                    takım arkadaşı arıyoruz
                                </p>
                                <small class="card-text">Bütçe: 300-600 TL | Kategori: Web Geliştirme | Proje
                                    Kapsamı:
                                    Geniş <br />
                                    Aranan Nitelikler: HTML, CSS, JS</small>
                                <a href="#" class="btn btn-sm btn-outline-success apply-button">Teklif al</a>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <!--**sol yatay kartlar**-->



        </div>
        <!--offcanvas filtre-->
        <nav class="navbar navbar-light bg-light fixed-bottom mycanvas">
            <div class="container-fluid">
                <a class="navbar-brand" href="#">Filtrele</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas"
                    data-bs-target="#offcanvasNavbar" aria-controls="offcanvasNavbar">
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

                        <label for="kategori" class="form-label">Kategori</label>
                        <select class="form-select" id="kategori">
                            <option selected>Tümü</option>
                            <option value="1">Grafik tasarım uzmanı</option>
                            <option value="2">Yazılım uzmanı</option>
                            <option value="3">Kameraman</option>
                            <option value="3">Video editörü</option>
                            <option value="3">Metinsel içerik üretici</option>
                            <option value="3">Sosyal medya uzmanı</option>
                            <option value="3">Satış ve pazarlama uzmanı</option>
                            <option value="3">Dijital pazarlama uzmanı</option>
                            <option value="3">3D Tasarımcı</option>
                            <option value="3">Siber güvenlik uzmanı</option>
                            <option value="3">Video içerik üretici</option>
                            <option value="3">Video içerik üretici</option>
                            <option value="3">Fotoğrafçı</option>
                            <option value="3">Eğitmen</option>
                        </select>

                        <br>

                        <label for="lokasyon" class="form-label">Lokasyon</label>
                        <div class="input-group mb-3">
                            <input type="text" class="form-control" aria-describedby="button-addon2" value="Farketmez">
                        </div>

                        <br>

                        <label>Deneyim süresi</label>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                            <label class="form-check-label" for="flexCheckDefault">
                                0-1 yıl
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                            <label class="form-check-label" for="flexCheckDefault">
                                1-3 yıl
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                            <label class="form-check-label" for="flexCheckDefault">
                                3-5 yıl
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                            <label class="form-check-label" for="flexCheckDefault">
                                5+ &nbsp;yıl
                            </label>
                        </div>

                        <br>

                        <br>

                        <label>Ekip</label>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                            <label class="form-check-label" for="flexCheckDefault">
                                Kendi ekibi var
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                            <label class="form-check-label" for="flexCheckDefault">
                                Bireysel çalışıyor
                            </label>
                        </div>

                        <br>

                        <label>Haftalık çalışabileceği süre</label>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                            <label class="form-check-label" for="flexCheckDefault">
                                2-8&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;saat
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                            <label class="form-check-label" for="flexCheckDefault">
                                8-16&nbsp;&nbsp;&nbsp;saat
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                            <label class="form-check-label" for="flexCheckDefault">
                                16-32 saat
                            </label>
                        </div>
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" value="" id="flexCheckDefault">
                            <label class="form-check-label" for="flexCheckDefault">
                                40+&nbsp;&nbsp;&nbsp;&nbsp;saat
                            </label>
                        </div>

                        <br>

                        <div class="btn btn-primary w-100">Ara</div>

                    </div>
                </div>
            </div>
        </nav>
        <!--**offcanvas filtre**-->
    </div>

    <!--footer-->
    <?php include("includes/footer.php"); include("includes/scripts.php"); ?>
    <!--**footer**-->
</body>

</html>