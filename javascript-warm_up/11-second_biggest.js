#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
if (args.length <= 1) {
  console.log(0);
} else {
  const sortedArgs = args.sort((a, b) => b - a);
  // Using a Set to handle duplicate biggest numbers if necessary, 
  // though basic sort works for standard cases
  const uniqueSorted = [...new Set(sortedArgs)];
  if (uniqueSorted.length <= 1) {
    console.log(0);
  } else {
    console.log(uniqueSorted[1]);
  }
}
