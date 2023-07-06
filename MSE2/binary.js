function insertelemets()
{
    let a=[];
    let n=prompt("Enter the number of elements");
    for(let i=0;i<n;i++)
    {
        let element=parseInt(prompt("Enter the number at position"+(i+1)));
        a.push(element);
    }
    return a;
}
function binarysearch(a,target)
{
    let left=0;
    let right=a.length-1;
    while(left<=right)
    {
        let mid=Math.floor((left+right)/2);
        if(a[mid]==target)
        {
            return mid;

        }
        else if(a[mid]<target)
        {
            left=mid+1;
        }
        else
        {
         right=mid-1;
        }
    }
    return -1;
    
}
var input=insertelemets();
var target=parseInt(prompt("Enter the element"));
var result=binarysearch(input,target);
if(result==-1)
{
    alert("Not found");
}
else
{
    alert("Element found at\n"+result);
}

