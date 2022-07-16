/**
 * Numbers to Words:
 * Provides a code example that will convert a long string of numbers into text. 
 *
 * https://en.wikipedia.org/wiki/Names_of_large_numbers - Standard dictionary 
 * to:vigintillion 
 *
 * Note: This is sample source code. It does work but is not optimized or
 *       otherwise intended for use in production.
 *
 * @author: Jon L. Boynton
 */
 
const SMALL_NUMBERS = [
	"",
	"one",
	"two",
	"three",
	"four",
	"five",
	"six",
	"seven",
	"eight",
	"nine",
	"ten",
	"eleven",
	"twelve",
	"thirteen",
	"fourteen",
	"fifteen",
	"sixteen",
	"seventeen",
	"eighteen",
	"nineteen",
	"twenty",
	"thirty",
	"forty",
	"fifty",
	"sixty",
	"seventy",
	"eighty",
	"ninety"];
	
const LARGE_NUMBERS = [
	"",
	"hundred",
	"thousand",
	"million",
	"billion",
	"trillion",
	"quadrillion",
	"quintillion",
	"sextillion",
	"septillion",
	"octillion",
	"nonillion",
	"decillion",
	"undecillion",
	"duodecillion",
	"tredecillion",
	"quattuordecillion",
	"quindecillion",
	"sexdecillion",
	"septendecillion",
	"octodecillion",
	"novemdecillion",
	"vigintillion"];
	
const ZERO = "zero";
	
		
function isDecimal(charCode){
    return charCode > 47 && charCode < 58; // between 0 - 9    
}

  
class NumberString {
	
	constructor(spec, offset=0){
		this.spec = spec;
		this.offset = offset;
		
		while (offset < spec.length && !isDecimal(spec.charCodeAt(offset))){
			offset++;
		}
		let end = offset;
		
		while (end < spec.length){
			let c = spec.charCodeAt(end);
	
			// check for  0-9 and ","	
			if (!isDecimal(c) && c !== 44){
				break;
			}
			end++;		
		}
		
		this.rawLength = end - offset;
		this.isNegative = Boolean(this.rawLength && spec.charCodeAt(offset-1) === 45);
		
		let s = spec.substring(offset, end);
		this.value = s.replace(/,/g, "");
		
		if (this.value.length > 66){
			throw Error("number >= '1000 vigintillion'");
		}	
	}
	
	
	getTokens(){
		let ta = [];
		
		if (!this.value){
			return ta;
		}
		let pos = 0;
		let len = Math.ceil(this.value.length/3);
		let rem = this.value.length % 3 || 3;
		
		do {
			ta.push(parseInt(this.value.substring(pos, pos + rem)));
			pos += rem;
			rem = 3;
		} while (--len > 0);
		
		return ta;		
	}
	
	formatSmallNumber(numbr){
		let n = "";
		numbr %= 1000;
		
		if (numbr > 99){
			n = SMALL_NUMBERS[Math.floor(numbr/100)] + " " + LARGE_NUMBERS[1];
			numbr %= 100;
			
			if (numbr){
				n += " and ";
			}
		}		
		
		if (numbr > 20){
			n += SMALL_NUMBERS[18 + Math.floor(numbr/10)];
			numbr %= 10;
			
			if (numbr){
				n += "-"+SMALL_NUMBERS[numbr];
			}
							
		} else if (numbr){
			n += SMALL_NUMBERS[numbr];			
		}			
		return n;		
	}
	
	toString(){
		let ta = this.getTokens();
		
		if (ta.length === 1 && !ta[0]){
			return ZERO;
		}
		
		let buf = "";
		
		for (let i = 0; i < ta.length; i++){
			let n = this.formatSmallNumber(ta[i]);
			
			if (n){
				if (buf){
					buf += ", ";
				} else if (this.isNegative){
					buf = "minus ";
				}
				if (i < ta.length - 1){
					n += " " + LARGE_NUMBERS[ta.length - i];
				}					
				buf += n;
			}			
		}
		return buf;		
	}	
}

let n = new NumberString("my big number is 431,541,056,545,003,000,102");

console.log(n.toString());
