<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Verification</title>
</head>
<body>
    <label>Enter the email:</label>
    <input type="text" id="data">
    <button id="btn">Submit</button>

    <script>
        const butn=document.getElementById('btn');
        const inp1=document.getElementById('data');

        butn.addEventListener('click',()=>
        {
            const email=inp1.value;

            const regEx=/^[^\s@]+@[^\s@]+\.[^\s@]+$/

            if(regEx.test(email)==true)
            {
                alert("valid email id");
            }
            else
            {
                alert("inavlid email id");
            }

        })
    </script>

</body>
</html>
