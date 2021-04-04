//#region testCase
// convertToRoman(2) should return "II"
// convertToRoman(3) should return "III"
// convertToRoman(4) should return "IV"
// convertToRoman(5) should return "V"
// convertToRoman(9) should return "IX"
// convertToRoman(12) should return "XII"
// convertToRoman(16) should return "XVI"
// convertToRoman(29) should return "XXIX"
// convertToRoman(44) should return "XLIV"
// convertToRoman(45) should return "XLV"
// convertToRoman(68) should return "LXVIII"
// convertToRoman(83) should return "LXXXIII"
// convertToRoman(97) should return "XCVII"
// convertToRoman(99) should return "XCIX"
// convertToRoman(400) should return "CD"
// convertToRoman(500) should return "D"
// convertToRoman(501) should return "DI"
// convertToRoman(649) should return "DCXLIX"
// convertToRoman(798) should return "DCCXCVIII"
// convertToRoman(891) should return "DCCCXCI"
// convertToRoman(1000) should return "M"
// convertToRoman(1004) should return "MIV"
// convertToRoman(1006) should return "MVI"
// convertToRoman(1023) should return "MXXIII"
// convertToRoman(2014) should return "MMXIV"
// convertToRoman(3999) should return "MMMCMXCIX"
// convertToRoman(666) should return "DCLXVI"
//#endregion

function convertToRoman(num) {
	// 0 < num <= 10000
	const magnitudes = ((val) =>
		val
			.toString()
			.split('')
			.map((v) => parseInt(v, 10))
			.reduce(
				(acc, value, index, arr) =>
					acc.concat(value * 10 ** (arr.length - index - 1)),
				[],
			)
			.reverse())(num);

	const romanianNotation = {
		I: 1,
		V: 5,
		X: 10,
		L: 50,
		C: 100,
		D: 500,
		M: 1000,
		ↁ: 5000,
		ↂ: 10000,
	};

	const findByValue = (value, objeto = romanianNotation) => {
		return Object.entries(objeto).find(
			(entrie) =>
				entrie[1] ===
				Object.values(objeto).find((val) => val === value),
		);
	};

	const miniumDif = (suma = true, magnitud, _COUNTER = 0) => {
		const archivo = Object.entries(romanianNotation).filter((v) =>
			suma ? v[1] <= magnitud : v[1] >= magnitud,
		);
		return archivo
			.map((actual) => {
				const key = actual[0];
				const dif = Math.abs(actual[1] - magnitud + _COUNTER);
				return [key, dif];
			})
			.sort((a, b) => {
				return a[1] - b[1];
			})
			.shift(); //?? ['M', 1000]
	};

	const getZeros = (v) => Math.pow(10, Math.trunc(Math.log10(v)));

	const isRestable = (difWithMinus, difWithPlus) => {
		const difWithMinusValue = difWithMinus[1];
		const difWithMinusZeros =
			difWithMinusValue / getZeros(difWithMinusValue);
		return difWithMinusZeros !== 2 && difWithMinus[1] < difWithPlus[1];
	};

	return magnitudes
		.reduce((output, magnitud) => {
			let _COUNTER = 0;
			let _ACCOUTPUT = '';

			while (_COUNTER !== magnitud) {
				const difWithMinus = miniumDif(false, magnitud, _COUNTER);
				const difWithPlus = miniumDif(true, magnitud, _COUNTER);
				if (isRestable(difWithMinus, difWithPlus)) {
					_ACCOUTPUT +=
						findByValue(difWithMinus[1])[0] + difWithMinus[0];
					_COUNTER += magnitud;
				} else {
					_ACCOUTPUT += difWithPlus[0];

					_COUNTER += Object.entries(romanianNotation).find(
						(v) => v[0] === difWithPlus[0],
					)[1];
				}
			}
			return output.concat(_ACCOUTPUT);
		}, [])
		.reverse()
		.join('');
}
