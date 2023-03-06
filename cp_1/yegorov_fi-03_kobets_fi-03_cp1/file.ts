import * as fs from "fs";

export class FileService {
  private fileData: string = "";

  readFile(filePath: string) {
    this.fileData = fs.readFileSync(filePath, { encoding: "utf-8", flag: "r" });
  }

  deleteSpacesAndSymbols(){
    return this.fileData.replace(/[^А-Я]/ig, "").toUpperCase();
  }

  deleteSymbols(){
    return this.fileData.replace(/[^А-Я ]/ig, "").toUpperCase();
  }

  constructor(filePath: string){
    this.readFile(filePath);
  }
}
