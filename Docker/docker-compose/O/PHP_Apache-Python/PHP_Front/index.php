<html>
    <head>
        <title>Frontend App</title>
    </head>

    <body>
        <h1>Docker Based PHP Frontend</h1>
        <ul>
            <?php
            $json = file_get_contents('http://product-services-api/');
            $obj = json_decode($json);
            $products = $obj->products;
            foreach ($products as $product) {
                echo "<li>$product</li>";
            }
            ?>
        </ul>
    </body>
</html>
