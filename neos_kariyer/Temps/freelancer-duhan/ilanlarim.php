<!DOCTYPE html>
<html lang="en">

<?php include("includes/head.php") ?>

<body>
    <!--navbar-->
    <?php include("includes/nav.php") ?>
    <!--**navbar**-->

    <!--content-->
    <div class="container-lg">

        <div class="row">

            <div class="col-12">
                <!--sıralama-->
                <div class="row">
                    <div class="col">
                        <select class="form-select  form-select" id="kategori">
                            <option selected>Hepsi</option>
                            <option value="1">Yalnızca aktif ilanlarım</option>
                            <option value="2">Yalnızca kapalı ilanlarım</option>
                        </select>
                    </div>
                    <div class="col">
                        <div class="input-group mb-3">
                            <input type="text" class="form-control" placeholder="neos yazılım" aria-label="ara"
                                aria-describedby="button-addon2">
                            <button class="btn btn-outline-secondary" type="button" id="button-addon2">Ara</button>
                        </div>
                    </div>
                </div>
                <!--**sıralama**-->
                <h5>Oluşturduğunuz ilanlar</h5>
                <table class="table">
                    <thead>
                        <tr>
                            <th scope="col">Başlık</th>
                            <th scope="col">Teklif sayısı</th>
                            <th scope="col">En düşük teklif</th>
                            <th scope="col">Kalan süre</th>
                            <th scope="col">Yayın tarihi</th>

                        </tr>
                    </thead>
                    <tbody>

                        <tr class="table-success" onclick="window.location='ilan-detay.php';">
                            <th scope="row">Web tasarım uzmanı</th>
                            <td>102</td>
                            <td>720₺/ay</td>
                            <td>21 gün</td>
                            <td>1 Ocak</td>
                        </tr>

                        <tr class="table-secondary" onclick="window.location='ilan-detay.php';">
                            <th scope="row">Ürün fotoğrafçısı</th>
                            <td>223</td>
                            <td>1720₺/proje</td>
                            <td>7 gün</td>
                            <td>1 Ocak</td>
                        </tr>
                        <tr class="table-secondary" onclick="window.location='ilan-detay.php';">
                            <th scope="row">SEO uzmanı</th>
                            <td>32</td>
                            <td>12300₺/ay</td>
                            <td>3 gün</td>
                            <td>1 Ocak</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>


    <!--footer-->
    <?php include("includes/footer.php");
    include("includes/scripts.php"); ?>
    <!--**footer**-->
</body>

</html>