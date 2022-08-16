<nav class="navbar-desktop navbar navbar-expand-sm navbar-light bg-light py-3">
    <div class="container">
        <a class="navbar-brand" href="index.php"><img src="images/logo.png" alt="yapbikariyer logo" width="60"></a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="index.php">Anasayfa</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link active" href="ilanlar.php">İlanlar</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link active" href="uzmanlar.php">Uzmanlar</a>
                </li>

            </ul>
            <form class="d-flex">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">

                    <li class="nav-item dropdown">
                        <a class="nav-link active dropdown-toggle" href="#" id="navbarDropdown" role="button"
                            data-bs-toggle="dropdown" aria-expanded="false">
                            Hesabım
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <li><a class="dropdown-item" href="profil.php">Profil</a></li>
                            <li><a class="dropdown-item" href="basvurularim.php">Başvurularım</a></li>
                            <li><a class="dropdown-item" href="ilanlarim.php">İlanlarım</a></li>
                            <li><a class="dropdown-item" href="gelenkutusu.php">Gelen kutusu</a></li>
                            <li><a class="dropdown-item" href="izleme.php">İzleme Listem</a></li>
                        </ul>
                    </li>

                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Bakiye: 50₺</a>
                    </li>


                </ul>
            </form>
        </div>
    </div>
</nav>

<!--**navbar for desktop**-->

<!--navbar for mobile-->
<nav class="navbar-mobile navbar navbar-light bg-light py-3">
    <div class="container-fluid">
        <a class="navbar-brand" href="index.php"><img src="images/logo.png" alt="yapbikariyer logo" width="40"></a>

        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
                <a class="nav-link active" href="#">
                    İlanlar
                </a>
            </li>
        </ul>
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
                <a class="nav-link active" href="#">
                    Uzmanlar
                </a>
            </li>
        </ul>
        <form class="d-flex">
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">

                <li class="nav-item">
                    <a class="nav-link active" href="#">
                        Hesabım (50₺)
                    </a>

                </li>
            </ul>

        </form>
    </div>
</nav>