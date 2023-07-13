#!/usr/bin/env ./node_modules/.bin/tsx

import * as fs from "fs";
import * as path from "path";
import { execSync } from "child_process";
import * as readline from "readline";

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// ...

async function findLessonDirs(numberOfCommits: number = 1): Promise<string[]> {
  const diffOutput = execSync(
    `git diff HEAD~${numberOfCommits} --name-status -r`
  ).toString();

  const lessonDirs: string[] = [];
  for (let line of diffOutput.split("\n")) {
    const [status, p] = line.split("\t");

    if (
      status &&
      p &&
      (status.startsWith("A") ||
        status.startsWith("M") ||
        status.startsWith("R"))
    ) {
      let absPath = path.resolve(p);
      absPath = path.dirname(absPath);

      const basename = path.basename(absPath);
      const match = basename.match(/^(\d{1,3})\. (.+)$/);

      if (match) {
        lessonDirs.push(absPath);
      }
    }
  }

  return lessonDirs;
}

async function findLessonIds(lessonDirectories: string[]): Promise<number[]> {
  const lessonIds: number[] = [];
  for (let lessonDirectory of lessonDirectories) {
    const basename = path.basename(lessonDirectory);
    const match = basename.match(/^(\d{1,3})\. (.+)$/);

    if (match) {
      const lessonId = parseInt(match[1]);
      lessonIds.push(lessonId);
    }
  }
  return lessonIds;
}

async function createLessonDir(
  lessonId: number,
  lessonName: string
): Promise<string> {
  const lessonDirName = `${lessonId}. ${lessonName}`;
  fs.mkdirSync(lessonDirName);
  fs.writeFileSync(path.join(lessonDirName, "main.py"), `# ${lessonDirName}\n`);

  return lessonDirName;
}

// Usage example

let numberOfCommits = 1;
let lessonDirs = await findLessonDirs(numberOfCommits);

while (lessonDirs.length === 0) {
  if (numberOfCommits === 1) {
    await new Promise((resolve, reject) => {
      rl.question(
        "No lesson ID found. Enter the number of commits to search: ",
        (answer) => {
          numberOfCommits = parseInt(answer);
          resolve(void 0);
        }
      );
    });
  }

  lessonDirs = await findLessonDirs(numberOfCommits);
}

const lessonIds = await findLessonIds(lessonDirs);
const lessonId = Math.max(...lessonIds);
const newLessonId = lessonId + 1;

if (lessonId) {
  console.log(`Found previous lesson ID: ${lessonId}`);
  console.log(`New lesson ID: ${newLessonId}`);

  const lessonDirName = await createLessonDir(
    newLessonId,
    await new Promise((resolve, reject) => {
      rl.question("Enter the lesson name: ", (answer) => {
        resolve(answer);
      });
    })
  );

  console.log(`\n\nCreated lesson directory:\n${lessonDirName} 🎉`);
} else {
  console.log("Could not find previous lesson ID.");

  const lessonId = await new Promise((resolve, reject) => {
    rl.question("Enter the lesson ID: ", (answer) => {
      resolve(parseInt(answer));
    });
  });

  const lessonName = await new Promise((resolve, reject) => {
    rl.question("Enter the lesson name: ", (answer) => {
      resolve(answer);
    });
  });

  const lessonDirName = await createLessonDir(lessonId, lessonName);

  console.log(`\n\nCreated lesson directory:\n${lessonDirName} 🎉`);
}

rl.close();
