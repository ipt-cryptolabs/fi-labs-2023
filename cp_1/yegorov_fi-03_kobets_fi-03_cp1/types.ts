export interface IData {
  data: string;
  amount: number;
}

export interface IFrequencyData {
  data: string;
  frequency: number;
}

export type Option = "letters" | "bigrams-no-crossing" | "bigrams-crossing";
