console.log('app.js loaded')

// twosum function
function twoSum(array, target) {
  var result = []
  for (var i = 0; i < array.length; i++) {
    for (var j = i + 1; j < array.length; j++) {
      if (array[i] + array[j] === target) {
        result.push(i)
        result.push(j)
      }
    }
  }
  return result
}

// test twosum
console.log(twoSum([1, 2, 3, 4, 5], 7))
console.log('should return [2, 4]')
console.log(twoSum([1, 2, 3, 4, 5], 9))
console.log('should return [3, 4]')

// i want to generate current year for footer, © 2024 Seltenet Technology. All rights reserved.
var currentYear = new Date().getFullYear()
var footer = document.querySelector('.footer')
footer.innerHTML = `© ${currentYear} Seltenet Technology. All rights reserved.`
console.log(currentYear)