//javascript program to extract the date from the sentence

let sentence = "Today is the date: 10/10/2022";

let date = / (\d{1,2}\/\d{1,2}\/\d{4}) | (\d{1,2}\/\d{1,2}\/\d{2}) /g;

let res = sentence.match(date);

alert(res);