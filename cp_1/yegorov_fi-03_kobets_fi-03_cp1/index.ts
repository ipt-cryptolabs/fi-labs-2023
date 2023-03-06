import { FileService } from "./file";
import { IData, Option, IFrequencyData } from "./types";

const filePath = "./Bible.txt";

class FrequencyService {
  private readonly fileService: FileService = new FileService(filePath);
  private readonly textClean = this.fileService.deleteSpacesAndSymbols();
  private readonly textWithSpaces = this.fileService.deleteSymbols();
  private readonly lettersDataset: IData[] = [];
  private readonly bigramsDataset: IData[] = [];
  private readonly bigramsWithoutCrossingDataset: IData[] = [];

  public createDataset(option: Option) {
    if (option == "letters") {
      for (let i = 0; i < this.textClean.length; i++) {
        if (
          this.lettersDataset.find(
            (dataset) => dataset.data === this.textClean[i]
          )
        ) {
          continue;
        }

        let letterAmount = 0;

        for (let j = 0; j < this.textClean.length; j++) {
          if (this.textClean[i] === this.textClean[j]) {
            letterAmount++;
          }
        }

        this.lettersDataset.push({
          data: this.textClean[i],
          amount: letterAmount,
        });
      }

      return this.lettersDataset.sort((a, b) =>  b.amount - a.amount);
    }

    if (option === "bigrams-crossing") {
      let bigram: string;

      for (let i = 0; i < this.textClean.length - 1; i++) {
        bigram = this.textClean[i] + this.textClean[i + 1];

        if (this.bigramsDataset.find((dataset) => dataset.data === bigram)) {
          continue;
        }

        let bigramRegExp = new RegExp(bigram, "g");
        let bigramAmount = Array.from(
          this.textClean.matchAll(bigramRegExp)
        ).length;

        this.bigramsDataset.push({
          data: bigram,
          amount: bigramAmount,
        });
      }

      return this.bigramsDataset.sort((a, b) =>  b.amount - a.amount);
    }

    if (option === "bigrams-no-crossing") {
      let bigram: string;

      for (let i = 0; i < this.textWithSpaces.length - 1; i++) {
        bigram = this.textWithSpaces[i] + this.textWithSpaces[i + 1];

        if (
          this.bigramsWithoutCrossingDataset.find(
            (dataset) => dataset.data === bigram
          ) ||
          this.textWithSpaces[i + 1] === " " ||
          this.textWithSpaces[i] === " "
        ) {
          continue;
        }

        let bigramRegExp = new RegExp(bigram, "g");
        let bigramAmount = Array.from(
          this.textWithSpaces.matchAll(bigramRegExp)
        ).length;

        this.bigramsWithoutCrossingDataset.push({
          data: bigram,
          amount: bigramAmount,
        });
      }

      return this.bigramsWithoutCrossingDataset.sort((a, b) =>  b.amount - a.amount);
    }
  }

  public countFrequency(dataset: IData[]) {
    const totalAmount = dataset.reduce((acc, data) => acc + data.amount, 0);

    const frequencyDataset: IFrequencyData[] = dataset.map((data) => {
      return {
        data: data.data,
        frequency: data.amount / totalAmount,
      };
    });

    return frequencyDataset.sort((a, b) =>  b.frequency - a.frequency);
  }

  public entropy(dataset: IFrequencyData[], n: number = 1) {
    const log = (arg: number) => Math.log2(arg);

    return (
      (-1 *
        dataset.reduce(
          (acc, data) => data.frequency * log(data.frequency) + acc,
          0
        )) /
      n
    );
  }
}

const frequencyService = new FrequencyService();

//Datasets
const lettersDataset = frequencyService.createDataset("letters");
const bigramsDataset = frequencyService.createDataset("bigrams-crossing");
const bigramsWithoutCrossingDataset = frequencyService.createDataset(
  "bigrams-no-crossing"
);

//Frequency datasets
const lettersFrequencyDataset = frequencyService.countFrequency(
  lettersDataset!
);
const bigramsFrequencyDataset = frequencyService.countFrequency(
  bigramsDataset!
);
const bigramsWithoutCrossingFrequencyDataset = frequencyService.countFrequency(
  bigramsWithoutCrossingDataset!
);

//Entropy
const lettersEntropy = frequencyService.entropy(lettersFrequencyDataset);
const bigramsEntropy = frequencyService.entropy(bigramsFrequencyDataset, 2);
const bigramsWithoutCrossingEntropy = frequencyService.entropy(
  bigramsWithoutCrossingFrequencyDataset,
  2
);

console.log(lettersDataset);
console.log(bigramsDataset);
console.log(bigramsWithoutCrossingDataset);

console.log(lettersFrequencyDataset);
console.log(bigramsFrequencyDataset);
console.log(bigramsWithoutCrossingFrequencyDataset);

console.log(lettersEntropy);
console.log(bigramsEntropy);
console.log(bigramsWithoutCrossingEntropy);
