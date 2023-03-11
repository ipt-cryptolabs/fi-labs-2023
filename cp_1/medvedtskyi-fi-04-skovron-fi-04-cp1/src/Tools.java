import java.io.*;
import java.util.*;

// Война и мир

public class Tools {
    private final static String FILE_PATH = "cp_1/medvedtskyi-fi-04-skovron-fi-04-cp1/src/Война и мир all in.txt";

    private final Map<Character, Integer> mapMonoGram;
    private final Map<Character, Integer> mapWithSpacesMonoGram;

    private final Map<String, Integer> mapBiGram;
    private final Map<String, Integer> mapBiGramCross;

    private final Map<String, Integer> mapBiGramWithSpaces;
    private final Map<String, Integer> mapBiGramCrossWithSpaces;

    private final Map<Character, Double> mapFrequencyMonoGram;
    private final Map<Character, Double> mapFrequencyWithSpacesMonoGram;

    private final Map<String, Double> mapFrequencyBiGram;
    private final Map<String, Double> mapFrequencyBiGramCross;

    private final Map<String, Double> mapFrequencyBiGramWithSpaces;
    private final Map<String, Double> mapFrequencyBiGramCrossWithSpaces;

    public Tools() throws IOException {
        mapMonoGram = calGram(filter());
        mapWithSpacesMonoGram = calGram(filterWithSpaces());

        mapBiGram = calBiGram(filter());
        mapBiGramCross = calBiGramCross(filter());

        mapBiGramWithSpaces = calBiGram(filterWithSpaces());
        mapBiGramCrossWithSpaces = calBiGramCross(filterWithSpaces());

        mapFrequencyMonoGram = calGramFrequency(mapMonoGram);
        mapFrequencyWithSpacesMonoGram = calGramFrequency(mapWithSpacesMonoGram);

        mapFrequencyBiGram = calBiGramFrequency(mapBiGram);
        mapFrequencyBiGramCross = calBiGramFrequency(mapBiGramCross);

        mapFrequencyBiGramWithSpaces = calBiGramFrequency(mapBiGramWithSpaces);
        mapFrequencyBiGramCrossWithSpaces = calBiGramFrequency(mapBiGramCrossWithSpaces);
    }

    public void run() {
        System.out.println("\n\nMonograms without spaces:");
        mapMonoGram.forEach((key, value) -> System.out.println(key + ": " + value));

        System.out.println("\n\nMonograms with spaces:");
        mapWithSpacesMonoGram.forEach((key, value) -> System.out.println(key + ": " + value));

        System.out.println("\n\nMonogram frequency without spaces:");
        mapFrequencyMonoGram.forEach((key, value) -> System.out.println(key + ": " + (value * 100.0) + " %"));

        System.out.println("\n\nMonogram frequency with spaces:");
        mapFrequencyWithSpacesMonoGram.forEach((key, value) -> System.out.println(key + ": " + (value * 100.0) + " %"));

        System.out.println("\n\nBiGram with no crossing and no spaces:");
        mapBiGram.forEach((key, value) -> System.out.println(key + ": " + value));

        System.out.println("\n\nBiGram with crossing and without spaces:");
        mapBiGramCross.forEach((key, value) -> System.out.println(key + ": " + value));

        System.out.println("\n\nBiGram with no crossing and with spaces:");
        mapBiGramWithSpaces.forEach((key, value) -> System.out.println(key + ": " + value));

        System.out.println("\n\nBiGram with crossing and spaces:");
        mapBiGramCrossWithSpaces.forEach((key, value) -> System.out.println(key + ": " + value));

        System.out.println("\n\nBigram frequency without spaces and crossing:");
        mapFrequencyBiGram.forEach((key, value) -> System.out.println(key + ": " + (value * 100.0) + " %"));

        System.out.println("\n\nBigram frequency with crossing and without spaces:");
        mapFrequencyBiGramCross.forEach((key, value) -> System.out.println(key + ": " + (value * 100.0) + " %"));

        System.out.println("\n\nBigram frequency with spaces and no crossing:");
        mapFrequencyBiGramWithSpaces.forEach((key, value) -> System.out.println(key + ": " + (value * 100.0) + " %"));

        System.out.println("\n\nBigram frequency with spaces and crossing:");
        mapFrequencyBiGramCrossWithSpaces.forEach((key, value) -> System.out.println(key + ": " + (value * 100.0) + " %"));

        System.out.println("\n\nEntropy MonoGram without spaces: " + entropyMonoGram(mapFrequencyMonoGram));

        System.out.println("\n\nEntropy MonoGram with spaces: " + entropyMonoGram(mapFrequencyWithSpacesMonoGram));

        System.out.println("\n\nEntropy BiGram without spaces and crossing: " + entropyBiGram(mapFrequencyBiGram));

        System.out.println("\n\nEntropy BiGram without spaces and with crossing: " + entropyBiGram(mapFrequencyBiGramCross));

        System.out.println("\n\nEntropy BiGram with spaces and without crossing: " + entropyBiGram(mapFrequencyBiGramWithSpaces));

        System.out.println("\n\nEntropy BiGram with spaces and crossing: " + entropyBiGram(mapFrequencyBiGramCrossWithSpaces));
    }

    private String filter() throws IOException {
        InputStream srcFile = new FileInputStream(Tools.FILE_PATH);
        String temp = readFromInputStream(srcFile);

        temp = temp.replaceAll("ё", "e").replaceAll("ъ", "ь");
        temp = temp.replaceAll("[^^а-яА-Я]", "");
        temp = temp.replaceAll("\n", "");
        temp = temp.toLowerCase();

        return temp;
    }

    private String filterWithSpaces() throws IOException {
        InputStream srcFile = new FileInputStream(Tools.FILE_PATH);
        String temp = readFromInputStream(srcFile);

        temp = temp.replaceAll("ё", "e").replaceAll("ъ", "ь");
        temp = temp.replaceAll("[^^а-яА-Я\\s]", "");
        temp = temp.replaceAll("\\s+", " ");
        temp = temp.replaceAll("\n", "");
        temp = temp.toLowerCase();

        return temp;
    }

    private String readFromInputStream(InputStream inputStream) throws IOException {
        StringBuilder resultStringBuilder = new StringBuilder();
        try (BufferedReader br = new BufferedReader(new InputStreamReader(inputStream))) {
            String line;
            while ((line = br.readLine()) != null) {
                resultStringBuilder.append(line).append("\n");
            }
        }
        return resultStringBuilder.toString();
    }

    private Map<Character, Integer> calGram(String input) {
        Map<Character, Integer> letters = new HashMap<>();

        for (int i = 0; i < input.length(); i++) {
            char c = input.charAt(i);
            if (!letters.containsKey(c)) {
                letters.put(c, 1);
            } else {
                int n = letters.get(c);
                letters.put(c, (n + 1));
            }
        }

        List<Map.Entry<Character, Integer>> listForSort = new ArrayList<>(letters.entrySet());
        listForSort.sort(Map.Entry.comparingByValue(Comparator.reverseOrder()));

        Map<Character, Integer> sortedLetters = new LinkedHashMap<>();
        for (Map.Entry<Character, Integer> entry : listForSort) {
            sortedLetters.put(entry.getKey(), entry.getValue());
        }

        return sortedLetters;
    }

    private Map<Character, Double> calGramFrequency(Map<Character, Integer> map) {
        Map<Character, Double> frequency = new HashMap<>();

        int letterSummary = 0;
        for (Integer value : map.values()) {
            letterSummary += value;
        }

        for (Map.Entry<Character, Integer> entry : map.entrySet()) {
            Character key = entry.getKey();
            Integer value = entry.getValue();
            double percentage = ((double) value) / ((double) letterSummary);
            frequency.put(key, percentage);
        }

        List<Map.Entry<Character, Double>> listForSort = new ArrayList<>(frequency.entrySet());
        listForSort.sort(Map.Entry.comparingByValue(Comparator.reverseOrder()));

        Map<Character, Double> sortedFrequency = new LinkedHashMap<>();
        for (Map.Entry<Character, Double> entry : listForSort) {
            sortedFrequency.put(entry.getKey(), entry.getValue());
        }

        return sortedFrequency;
    }

    private Map<String, Integer> calBiGram(String input) {
        Map<String, Integer> bigram = new TreeMap<>();

        for (int i = 0; i < input.length() - 1; i += 2) {
            char c1 = input.charAt(i);
            char c2 = input.charAt(i + 1);
            String temp = c1 + String.valueOf(c2);

            if (!bigram.containsKey(temp)) {
                bigram.put(temp, 1);
            } else {
                int n = bigram.get(temp);
                bigram.put(temp, (n + 1));
            }
        }

        List<Map.Entry<String, Integer>> listForSort = new ArrayList<>(bigram.entrySet());
        listForSort.sort(Map.Entry.comparingByValue(Comparator.reverseOrder()));

        Map<String, Integer> sortedBigram = new LinkedHashMap<>();
        for (Map.Entry<String, Integer> entry : listForSort) {
            sortedBigram.put(entry.getKey(), entry.getValue());
        }

        return sortedBigram;
    }

    private Map<String, Integer> calBiGramCross(String input) {
        Map<String, Integer> bigram = new TreeMap<>();

        for (int i = 0; i < input.length() - 1; i++) {
            char c1 = input.charAt(i);
            char c2 = input.charAt(i + 1);
            String temp = c1 + String.valueOf(c2);

            if (!bigram.containsKey(temp)) {
                bigram.put(temp, 1);
            } else {
                int n = bigram.get(temp);
                bigram.put(temp, (n + 1));
            }
        }

        List<Map.Entry<String, Integer>> listForSort = new ArrayList<>(bigram.entrySet());
        listForSort.sort(Map.Entry.comparingByValue(Comparator.reverseOrder()));

        Map<String, Integer> sortedBigram = new LinkedHashMap<>();
        for (Map.Entry<String, Integer> entry : listForSort) {
            sortedBigram.put(entry.getKey(), entry.getValue());
        }

        return sortedBigram;
    }

    private Map<String, Double> calBiGramFrequency(Map<String, Integer> map) {
        Map<String, Double> frequency = new TreeMap<>();

        int letterSummary = 0;
        for (Integer value : map.values()) {
            letterSummary += value;
        }

        for (Map.Entry<String, Integer> entry : map.entrySet()) {
            String key = entry.getKey();
            Integer value = entry.getValue();
            double percentage = ((double) value) / ((double) letterSummary);
            frequency.put(key, percentage);
        }

        List<Map.Entry<String, Double>> listForSort = new ArrayList<>(frequency.entrySet());
        listForSort.sort(Map.Entry.comparingByValue(Comparator.reverseOrder()));

        Map<String, Double> sortedFrequency = new LinkedHashMap<>();
        for (Map.Entry<String, Double> entry : listForSort) {
            sortedFrequency.put(entry.getKey(), entry.getValue());
        }

        return sortedFrequency;
    }

    private double entropyMonoGram(Map<Character, Double> map) {
        double entropy = 0;
        double[] freq = map.values().stream().mapToDouble(Double::doubleValue).toArray();

        for (double i : freq) {
            entropy += i * Math.log(i);
        }

        return -entropy;
    }

    private double entropyBiGram(Map<String, Double> map) {
        double entropy = 0;
        double[] freq = map.values().stream().mapToDouble(Double::doubleValue).toArray();

        for (double i : freq) {
            entropy += i * Math.log(i);
        }

        return -entropy / 2.0;
    }

}
