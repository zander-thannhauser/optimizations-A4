fn pre_example(x: int, y: int, z: *int) {
	let a = 4;
	while (x < 5) {
		*z = 4;
		*z = y + a;
		x += 1;
	}
	print(*z);
}

fn main() {
	let num = 0;
	pre_example(3, 2, &num);
}
