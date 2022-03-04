fn main() {
    let res = convert_secs(3);
    println!("seconds from minutes {}", res);
}

fn convert_secs(mins: u32) -> u32 {
    return mins * 60;
}
