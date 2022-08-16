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

    <style>
    .container {
        background-color: #474e5d;
        margin-top: 150px;
        color: white;
        padding: 40px;
    }
    </style>
</head>

<body>

    <!--navbar-->
    <?php include("includes/nav.php") ?>
    <!--**navbar**-->


    <!--content-->
    <div class="container">
        <div class="row">
            <div class="col-sm-2">
                <!--profil sol sütun-->


                <image id="profileImage" src="images/pp.png" style="width:100%" />
                <input id="imageUpload" type="file" name="profile_photo" placeholder="Photo" required="" capture>



                <div class="col-12">
                    <small class="card-text">
                        Üst düzey deneyimli <br />

                        Teslimat: Hızlı <br />
                        Konum: İstanbul <br />
                    </small>
                    <div class="form-group">
                        <div class="text-right">
                            <button type="submit" class="btn btn-sm btn-success w-100">Teklif iste</button>
                        </div>
                    </div>
                </div>

            </div>

            <div class="col-sm-10">
                <!--biyografi ve yetenekler-->
                <div class="row">
                    <div class="col-sm-6">
                        <h5>Genel bilgiler</h5>
                        <hr>
                        <form class="row g-3">
                            <div class="col-md-6">
                                <label for="isimsoyisim" class="form-label">İsim soyisim</label>
                                <input type="text" class="form-control" id="isimsoyisim">
                            </div>
                            <div class="col-md-6">
                                <label for="yetenek" class="form-label">Öne çıkan yetenek</label>
                                <input type="text" class="form-control" id="yetenek"
                                    placeholder="Full stack geliştirici">
                            </div>
                            <div class="col-md-12">
                                <label for="biyo">Ön Yazı</label>
                                <textarea class="form-control" id="biyo" rows="10"></textarea>
                            </div>
                        </form>
                    </div>
                    <div class="col-sm-6 yetenekler">
                        <h5>YETENEKLER</h5>
                        <hr>
                        <div class="col-6">
                            <input type="text" class="form-control py-0" aria-label="Sizing example input"
                                aria-describedby="inputGroup-sizing-sm" value="HTML">
                        </div>

                        <div class="col-6">
                            <button class="btn btn-success btn-sm" id="yetenekEkle">Yetenek ekle</button>

                        </div>


                    </div>

                    <div class="row">

                        <div class="col-sm-12">
                            <br>
                            <h5 class="text-center">DENEYİMLER VE ÖZGEÇMİŞ</h5>
                            <hr>
                            <form class="row g-3">
                                <div class="col-md-6">
                                    <div class="col-md-12">
                                        <label for="sirket" class="form-label">Şirket</label>
                                        <input type="text" class="form-control" id="sirket" placeholder="Neos Yazılım">
                                    </div>
                                    <div class="col-md-12">
                                        <label for="pozisyon" class="form-label">Pozisyon</label>
                                        <input type="text" class="form-control" id="pozisyon"
                                            placeholder="Front end geliştirici">
                                    </div>
                                    <div class="row">
                                        <div class="col-md-6">
                                            <label for="inputState" class="form-label">Başlangıç</label>
                                            <select id="inputState" class="form-select">
                                                <option selected>2021</option>
                                                <option>...</option>
                                            </select>
                                        </div>
                                        <div class="col-md-6">
                                            <label for="inputState" class="form-label">Bitiş</label>
                                            <select id="inputState" class="form-select">
                                                <option selected>2021</option>
                                                <option>...</option>
                                            </select>
                                        </div>
                                    </div>
                                </div>
                                <div class="col-6">
                                    <div class="col-12">
                                        <label for="aciklama" class="form-label">Açıklama</label>
                                        <textarea class="form-control" id="aciklama" rows="7"></textarea>
                                    </div>
                                </div>

                                <div class="col-12">
                                    <button type="submit" class="btn btn-primary">Kaydet</button>
                                </div>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>

    <!--footer-->
    <?php include("includes/footer.php");
    include("includes/scripts.php"); ?>
    <!--**footer**-->


</body>

</html>