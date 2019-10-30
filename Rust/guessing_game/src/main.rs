use std::io;									// Permet d'utiliser la librairie io contenue dans le namespace std, la librairie standard.
use std::cmp::Ordering;
use rand::Rng;

fn main() {										// Point d'entrée du programme. fn sert à déclarer une fonction.
    println!("Guess the number !");				// Permet d'afficher un texte.

    let secret_number = rand::thread_rng().gen_range(1, 101);

    // println!("The secret number is {}", secret_number);

    loop {
        println!("Please input your guess.");

        let mut guess = String::new();				// let sert à déclarer une variable. mut signifie qu'elle est mutable.
    
        io::stdin().read_line(&mut guess)			// Assez chiant à comprendre, alors ce sera expliqué plus bas.
    	    .expect("Failed to read line");
    
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };
    	
        println!("You guessed : {}", guess);		// Les {} permettent d'indiquer quelle valeur afficher, ici guess.

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small !!"),
            Ordering::Greater => println!("Too big !!"),
            Ordering::Equal => {
                println!("You win !!");
                break;
            }
        }
    }

}
