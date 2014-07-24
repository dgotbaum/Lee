$(document).ready( function () {
   $('#nameBtn').click( function() {
     var fullName = $("input[id=name]").val();
     var firstInitial = fullName.charAt(0).toLowerCase();
     var lastname = fullName.split(" ")[1].toLowerCase();
     var index = "../directory/index.html#" + firstInitial + lastname;
     console.log(index);
     window.location = index; 
   });
});
var substringMatcher = function(strs) {
  return function findMatches(q, cb) {
    var matches, substringRegex;
 
    // an array that will be populated with substring matches
    matches = [];
 
    // regex used to determine if a string contains the substring `q`
    substrRegex = new RegExp(q, 'i');
 
    // iterate through the pool of strings and for any string that
    // contains the substring `q`, add it to the `matches` array
    $.each(strs, function(i, str) {
      if (substrRegex.test(str)) {
        // the typeahead jQuery plugin expects suggestions to a
        // JavaScript object, refer to typeahead docs for more info
        matches.push({ value: str });
      }
    });
 
    cb(matches);
  };
};
 
var states = ['James Wacht', 'Joel Herskowitz', 'Peter Braus', 'Howard Rosen', 'John Cannon',
  'Henry Goldfarb', 'Dennis Someck', 'Mitchell Kunikoff', 'Robert Kunikoff', 'Sidney Rosenthal', 'Jonathan Miller',
  'Alan Weisman', 'Stanley Lindenfeld', 'Brad Schwarz', 'Kenneth Salzman', 'Peter Levitan', 'Gabe Isaacs', 'Garry Steinberg',
  'Peter Shakalis', 'Richard Kave', 'Adam Frisch', 'Adam Courtney', 'Jackie RocMurphy',
  'JP Sutro', 'Justin Myers'
];
 
$('#names .typeahead').typeahead({
  hint: true,
  highlight: true,
  minLength: 1
},
{
  name: 'states',
  displayKey: 'value',
  source: substringMatcher(states)
});

