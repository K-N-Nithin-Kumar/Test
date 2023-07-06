<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hospital</title>
</head>
<body>

    <!--(very easy just check whether blood composition is subseuqnece of virus composition) -->
    <script>

        let viruscomposition=prompt("Enter the virus composition:");
        let bloodcomposition=prompt("Enter the blood composition:");

        function obtainResults(virus,blood)
        {
            let i=0;
            let j=0;
            
            while(i<virus.length && j<blood.length)
            {
                if(virus[i]==blood[j])
                {
                    i=i+1;
                    j=j+1;
                }
                else
                {
                    i=i+1;
                }
            }


            if(j==blood.length)
            {
                return "Positive";
            }else
            {
                return "Negative";
            }
        }

        
        
        
        const res=obtainResults(viruscomposition,bloodcomposition);
        alert(`He/She is ${res}`);

    </script>
    
</body>
</html>
