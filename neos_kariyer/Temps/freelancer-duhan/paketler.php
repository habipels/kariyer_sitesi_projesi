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
        margin-top: 140px;
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
            <div class="col-4"><img src="images/standard.png" style="width:100%"></div>
            <div class="col-4"><img src="images/premium.png" style="width:100%"></div>
            <div class="col-4"><img src="images/premiumplus.png" style="width:100%"></div>
        </div>
    </div>


    <!--footer-->
    <?php include("includes/footer.php"); include("includes/scripts.php"); ?>
    <!--**footer**-->


</body>

</html>