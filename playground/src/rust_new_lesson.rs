use regex::Regex;
use std::fs;
use std::io::prelude::*;
use std::io::stdin;
use std::path::Path;
use std::process::Command;

pub fn find_lesson_dirs(number_of_commits: u32) -> Vec<String> {
    let output = Command::new("git")
        .arg("diff")
        .arg(format!("HEAD~{}", number_of_commits))
        .arg("--name-status")
        .arg("-r")
        .output()
        .expect("Failed to execute command");

    let re = Regex::new(r"^(\d{1,3})\. (.+)$").unwrap();
    let mut lesson_dirs = Vec::new();

    for line in String::from_utf8(output.stdout).unwrap().lines() {
        let split_line: Vec<&str> = line.split("\t").collect();
        if split_line.len() >= 2 {
            let status = split_line[0];
            let path = Path::new(split_line[1]).parent().unwrap();

            if (status.starts_with("A") || status.starts_with("M") || status.starts_with("R"))
                && path.is_dir()
            {
                if re.is_match(path.file_name().unwrap().to_str().unwrap()) {
                    lesson_dirs.push(String::from(path.to_str().unwrap()));
                }
            }
        }
    }
    lesson_dirs
}

pub fn find_lesson_ids(lesson_directories: Vec<String>) -> Vec<u32> {
    let re = Regex::new(r"^(\d{1,3})\. (.+)$").unwrap();
    let mut lesson_ids = Vec::new();
    for lesson_directory in lesson_directories {
        if let Some(captures) = re.captures(
            Path::new(&lesson_directory)
                .file_name()
                .unwrap()
                .to_str()
                .unwrap(),
        ) {
            lesson_ids.push(captures[1].parse().unwrap());
        }
    }
    lesson_ids
}

pub fn create_lesson_dir(lesson_id: u32, lesson_name: String) -> String {
    let lesson_dir_name = format!("{}. {}", lesson_id, lesson_name);
    match fs::create_dir(&lesson_dir_name) {
        Ok(_) => {} // Directory created successfully
        Err(err) => {
            eprintln!("Failed to create directory: {}", err);
            // Handle the error appropriately, such as returning an error or exiting the program
        }
    }
    let mut file = fs::File::create(format!("{}/main.rs", lesson_dir_name)).unwrap();
    file.write_all(format!("# {}\n", lesson_dir_name).as_bytes())
        .unwrap();
    lesson_dir_name
}

pub fn create_new_lesson() {
    let mut lesson_dirs = find_lesson_dirs(1);

    while lesson_dirs.is_empty() {
        let mut number_of_commits = String::new();
        stdin().read_line(&mut number_of_commits).unwrap();
        let number_of_commits: u32 = number_of_commits.trim().parse().unwrap();
        lesson_dirs = find_lesson_dirs(number_of_commits);
    }

    let lesson_ids = find_lesson_ids(lesson_dirs);
    let lesson_id = *lesson_ids.iter().max().unwrap();
    let new_lesson_id = lesson_id + 1;

    let mut lesson_name = String::new();
    stdin().read_line(&mut lesson_name).unwrap();
    let lesson_name = lesson_name.trim().to_string();

    let lesson_dir_name = create_lesson_dir(new_lesson_id, lesson_name);
    println!("\n\nCreated lesson directory:\n{} 🎉", lesson_dir_name);
}
